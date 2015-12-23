#!/usr/bin/env python


import xml.dom.minidom

#dom = xml.dom.minidom.parse("catlog.xml")

#print dom

#root = dom.documentElement

#print root

#print root.nodeName

def _get_Vm():
    dom = xml.dom.minidom.parse("vm.xml")
    root = dom.documentElement
    return root

def getVm_Name():
    root = _get_Vm()
    bb = root.getElementsByTagName("name")
    b = bb[0]
    print b.firstChild.data

def getVm_ID():
    root = _get_Vm()
    vm_ids = root.getElementsByTagName("vm")
    vm_id = vm_ids[0]
    print vm_id.getAttribute("id")



if __name__ == "__main__":
    
    getVm_Name()    
    getVm_ID()



