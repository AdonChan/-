import re
import time
from lxml import html
from urllib import request
etree = html.etree #网上说的是python 3.5之后的lxml中不再有etree，但是其实这种说法是有问题的，虽然新版本无法直接from lxml import etree这样，但是它只不过是换了一个办法引出etree模块而已！
def getPage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = request.Request(url=url, headers=headers)
    html = request.urlopen(req).read()
    html = html.decode('utf-8') # 解码
    return html


if __name__ == '__main__':
    url = 'https://segmentfault.com/a/1190000017037224'
    s = getPage(url)
    Html = etree.parse(s)
    print(Html)


