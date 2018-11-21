import re
import time
import random
from urllib import request
from multiprocessing import Process
from multiprocessing import Semaphore
def getPage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = request.Request(url=url, headers=headers)
    html = request.urlopen(req).read()
    html = html.decode('utf-8') # 解码
    return html

def get_title(s):
    #获得标题转换为文件名
    com = re.search('<title>(?P<title>.*?)- SegmentFault 思否', s, re.S)
    return com.group("title").strip()

def setFileTitle(title):
    #去除文件名中的非法字符
    fileName = re.sub('[/\\\\:*?"<>|]', '-', title)  # 去掉非法字符
    file = str(fileName) + ".html"
    return file

def get_scr(url):
    com = re.compile('<img data-src="(?P<data_src>.*?)"', re.S)
    ret = com.finditer(url)
    for i in ret:
        yield  i.group('data_src')

def parsePage_1(s):
    com = re.compile('<a href="/a/(?P<url>.*?)"', re.S)
    ret = com.finditer(s)
    for i in ret:
        yield i.group("url")

def get_2(url):
    response_html = getPage(url)
    ret = parsePage_1(response_html)
    for k in ret:
        link = 'https://segmentfault.com/a/'+ k
        html = getPage(link)
        ret_1 = get_scr(html)
        for obj in ret_1:
            img_link = 'https://segmentfault.com' + obj
            html = str(html).replace(obj, img_link)
        html = html.replace('data-src', 'src')
        s = get_title(html)                           #获取标题
        filename = setFileTitle(s)
        try:
            with open('./html/' + str(i)+'.'+str(filename), 'w', encoding='utf-8') as f2:
                f2.write(html)
                print('正在下载:' + str(i)+'.'+ str(s))
        except:
            print('下载错误:' + str(i)+'.'+ str(s))
        time.sleep(random.randint(5,10)+random.random())

if __name__ == '__main__':
    global i
    for i in range(1,2):
        url = 'https://segmentfault.com/t/python/blogs?page=%s' % i
        get_2(url)


