#!/usr/bin/env python


import optparse

class AutotestLocalOptionParser(optparse.OptionParser):
	def __init__(self):
		print "Optparser!"
		optparse.OptionParser.__init__(self,usage='',description="")
		
	def myfunction(self):
		print "Myfunction."

if __name__ == "__main__":
	opt_parser = AutotestLocalOptionParser()
	opt_parser.myfunction()
	options,args = opt_parser.parse_args()
	print "options:",options
	print "args:",args

