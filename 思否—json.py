import os
import json
import re
from bs4 import BeautifulSoup
path = 'D:\爬虫\爬虫—思否\html'
content ={}
def get_title(s):
    soup = BeautifulSoup(s,'html5lib')
    content['title'] = soup.title.string.replace('- SegmentFault 思否','')

def get_index(s):
    com = re.search('<meta name="keywords" content="(?P<index>.*?)"', s, re.S)
    content["index"] = com.group("index")

def get_context(s):
    com = re.search('<div class="article fmt article__content.*?>(?P<content>.*?)</div>', s, re.S)
    return com.group("content")

def mainLike(s):
    com = re.search('<span id="mainLikeNum">(?P<mainLikeNum>.*?)<.*?<span id="mainBookmarkNum">(?P<mainBookmarkNum>.*?)<', s, re.S)
    content["mainLikeNum"]=com.group("mainLikeNum"),
    content['mainBookmarkNum']=com.group('mainBookmarkNum')

if __name__ == '__main__':
    for i in os.listdir(path):
        exp = os.path.join(path,i)
        # print(exp)
        with open(exp,'r',encoding='utf-8') as f:
            try:
                file = f.read()
                get_title(file)
                get_index(file)
                content_html = get_context(file)
                con_soup = BeautifulSoup(content_html,'html5lib')
                content['content'] =con_soup.get_text()
                mainLike(file)
                # print(content)
                filename = content['title']
                with open(r'./json/'+str(filename),'w',encoding='utf-8') as f:
                    str_d = json.dumps(content, ensure_ascii=False)
                    f.write(str_d)
                    print('正在修改'+str(i))
            except:
                print('修改失败:'+str(i))
