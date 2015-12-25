#!/usr/bin/env python

import urllib
import urlparse
import HTMLParser
import sgmllib

class CheckHtml(HTMLParser.HTMLParser):
    available = True
    def handle_data(self,data):
        if "404 Not Found" in data or "Error 404" in data:
            self.available = False

class LinkDemo(sgmllib.SGMLParser):
    def __init__(self):
        sgmllib.SGMLParser.__init__(self)
        self.links = []
    
    def start_a(self,attributes):
        for link in attributes:
            tag,attr = link[:2]
            if tag == "href":
                self.links.append(attr)

check_urls=[" index"," test"," help","news","faq","download"]

def check_url():

    for url in check_urls:
        new_url = urlparse.urljoin("http://www.python.org/",url)
        fp = urllib.urlopen(new_url)
        data = fp.read()
        fp.close()

        p = CheckHtml()
        p.feed(data)
        p.close()

        if p.available:
            print new_url," ==> OK"
        else:
            print new_url,"==> Not Found"

def link_demo():
    f = urllib.urlopen("http://www.baidu.com")
    data = f.read()
    f.close()

    ld = LinkDemo()
    ld.feed(data)
    

    for i,link in enumerate(ld.links):
        print i,"==>",link
    




if __name__ == "__main__":
    link_demo()
