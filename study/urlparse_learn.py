#!/usr/bin/env python
import os

import urlparse

def urlparse_url(url):
    url_result = urlparse.urlparse(url)
    return url_result


def urlparse_join():
    r1 = urlparse.urljoin("http://100.1.8.111:8080","ics.html")
    print "r1:",r1

    r2 = urlparse.urljoin("http://100.1.8.111","ftp://10.166.15.160")
    print "r2:",r2

    r3 = urlparse.urljoin("http://100.1.8.111","http://www.baidu.com")
    print "r3:",r3


if __name__ == "__main__":
    #urlparse_join()

