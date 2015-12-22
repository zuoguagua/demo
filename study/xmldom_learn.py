#!/usr/bin/env python


import xml.dom.minidom

dom = xml.dom.minidom.parse("catlog.xml")

print dom

root = dom.documentElement

print root

print root.nodeName
