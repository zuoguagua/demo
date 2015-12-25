#!/usr/bin/env python

import htmllib
import urllib
import formatter
import string

class LinkDemo(htmllib.HTMLParser):
    def __init__(self,verbose=0):
        self.links={}
        f = formatter.NullFormatter()
        htmllib.HTMLParser.__init__(self,f,verbose)
    
    def anchor_bgn(self,href,name,type):
        self.save_bgn()
        self.link = href

    def anchor_end(self):
        text = string.strip(self.save_end())
        if self.link and text:
            self.links[text] = self.links.get(text,[])+[self.link]

def link_demo():
    fp = urllib.urlopen("http://www.baidu.com")
    data = fp.read()
    fp.close()
    
    linkdemo = LinkDemo()
    linkdemo.feed(data)
    linkdemo.close()


    for href,link in linkdemo.links.items():
        print href,"==>",link


if __name__ == "__main__":
    link_demo()


    
