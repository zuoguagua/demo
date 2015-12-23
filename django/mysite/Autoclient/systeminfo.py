#!/usr/bin/env python

import os

def systeminfo():
    msg = os.popen("uname -a")
    return msg.read()

