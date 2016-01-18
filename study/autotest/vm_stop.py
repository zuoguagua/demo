#!/usr/bin/env python
import time

from autotest.client import test
from autotest.client import vm_api

vm_status = vm_api.getvm_status()

class vm_stop(test.test):
    version = 1.0
    
    
    def run_once(self):
        global vm_status
        print "mytest"
        print vm_status
        if vm_status == "up":
            vm_api.vm_stop()
            time.sleep(120)
            vm_status = vm_api.getvm_status()
            print vm_status+"oo"
            if vm_status == "DOWN":
                print "PASS"
            else:
                print "Failed"
        else:
            print "Block"
