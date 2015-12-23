#!/usr/bin/env python 

import os

def job_list():
    msg = os.popen("autotest-local list")
    return msg.read()

if __name__ == "__main__":
    job_list()
