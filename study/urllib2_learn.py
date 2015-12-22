#!/usr/bin/env python

import urllib2


def urlopen_learn_http():
	response = urllib2.urlopen("http://www.baidu.com")
	html = response.read()
	print html


def urlopen_learn_file():
	response = urllib2.urlopen("ftp://10.166.15.160")
	html = response.read()
	print html

def urlopen_learn_api():
	passwd_mgr=urllib2.HTTPPasswordMgrWithDefaultRealm()
	username = "admin@internal"
	password = "ovirt"
	top_level_url = "https://10.166.15.171/api"
	passwd_mgr.add_password(None,top_level_url,username,password)
	handler = urllib2.HTTPBasicAuthHandler(passwd_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	page = urllib2.urlopen(top_level_url).read()
	print page
	#response = urllib2.urlopen("https://10.166.15.171/api/vms")
	#html = response.read()
	#print html
top_level_url = "https://10.166.15.171/api"

def _urlopen_api():
	pd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	username = "admin@internal"
	password = "ovirt"
	#top_level_url = "https://10.166.15.171/api"
	pd_mgr.add_password(None,top_level_url,username,password)
	return pd_mgr


def urlopen_learn_vms():
	pd_mgr = _urlopen_api()
	print pd_mgr
	handler = urllib2.HTTPBasicAuthHandler(pd_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	#test = top_level_url+("/vms")
	#print test
	page = urllib2.urlopen(top_level_url+("/vms")).read()
	print page
	



if __name__ == "__main__":
	
	#urlopen_learn_http()
	#urlopen_learn_file()
	#urlopen_learn_api()
	urlopen_learn_vms()
