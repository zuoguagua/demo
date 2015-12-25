#!/usr/bin/python

import urllib

def get_urlopen():
    r = urllib.urlopen("http://www.python.org")
    print r.fp.read()


if __name__=="__main__":
    get_urlopen()
