#!/usr/bin/env python
import urllib2
import re
import xml.dom.minidom

top_level_url = "https://10.166.15.160/api"

def _urlopen_api():
    pd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    username = "admin@internal"
    password = "ovirt"
    pd_mgr.add_password(None,top_level_url,username,password)
    return pd_mgr

def _get_vm():
    dom = xml.dom.minidom.parse("/usr/lib/python2.7/site-packages/autotest/client/vm.xml")
    root = dom.documentElement
    return root

def get_page():
    pd_mgr = _urlopen_api()
    handler = urllib2.HTTPBasicAuthHandler(pd_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    #page = urllib2.urlopen(top_level_url+("/vms")).read()
    with open("vm.xml","wb") as code:
        code.write(urllib2.urlopen(top_level_url+("/vms")).read())  
    #return page    

def getvm_uuid():
    root = _get_vm()
    vm_ids = root.getElementsByTagName("vm")
    vm_id = vm_ids[0]
    return vm_id.getAttribute("id")
    

def getvm_status():
    root = _get_vm()
    vm_statuss = root.getElementsByTagName("state")
    vm_status = vm_statuss[0]
    return vm_status.firstChild.data

def vm_stop():
    uuid = getvm_uuid()
    print uuid
    pd_mgr = _urlopen_api()
    handler = urllib2.HTTPBasicAuthHandler(pd_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    stop = top_level_url+("/vms/")+uuid+("/stop")
    print stop
    result = urllib2.urlopen(top_level_url+("/vms/")+uuid+("/stop"),"stop")
    print result

if __name__ == "__main__":
    vm_stop()
