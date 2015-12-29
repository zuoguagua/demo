#!/usr/bin/env python



import signal

def myHandler(signum,frame):
    print "I received:",signum

def myHandler_1(signum,frame):
    print " Now ,it's the time"
    exit()


def signal_sigtstp():
    signal.signal(signal.SIGTSTP,myHandler)
    signal.pause()
    print "End of Signal Demo"

def signal_sigalrm():
    signal.signal(signal.SIGALRM,myHandler_1)
    signal.alarm(5)
    while True:
        print "Not yet"


if __name__ == "__main__":
       signal_sigalrm()    
