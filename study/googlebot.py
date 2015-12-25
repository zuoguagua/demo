#!/usr/bin/env python

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    image = re.compile(reg)
    imglist = re.findall(image,html)
    x = 0 
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        x+=1
    #return imglist
    

if __name__ == "__main__":
    html = getHtml("http://tieba.baidu.com/p/3545397417")
    print getImg(html)
