#!/usr/bin/env python

def text_plain():
    print "Content-Type:text/plain\n\n"

    import datetime
    print datetime.datetime.now()
def text_html():
    
    import os
    print "Content-Type:text/html \n\n"
    
    remote_addr = os.environ["REMOTE_ADDR"]
    if remote_addr == "127.0.0.1":
        print "local"
    else:
        print "remote"

def cgi_environ():
    import cgi
    cgi.print_environ()

if __name__ == "__main__":
    cgi_environ()

