#!/usr/bin/env python

import sys

print "script name:",sys.argv[0]

for item in range(1,len(sys.argv)):
	print "option",item,sys.argv[item]


