#!/usr/bin/env python

import sys,getopt

def usage(self):
	print "Help"

opts,args = getopt.getopt(sys.argv[1:],"hi:o:")

input_file = ""
output_file = ""

for op,value in opts:
	if op == "-i":
		input_file = value
	elif op == "-o":
		output_file = value
	elif op == "-h":
		usage("")
		sys.exit()

print "input_file:",input_file
print "output_fule:",output_file
