#!/usr/bin/env python


import sys

import optparser,cmdparser

class AutotestLocalApp:
	def __init__(self):
		self._set_parsers()

	def _set_parsers(self):
		self.opt_parser = optparser.AutotestLocalOptionParser()
		self.cmd_parser = cmdparser.CommandParser()

	def usage(self):
		self.opt_parser.print_help()
		sys.exit(1)

	def parse_cmdline(self):
		self.options,args = self.opt_parser.parse_args()

		self.args = self.cmd_parser.parse_args(args,self.options)

		if len(args) != 1 and self.options.client_test_setup is None:
			print "Missing control file!"
			self.usage()
		print args
		
	def main(self):
		print "OK"
		self.parse_cmdline()

if __name__ == "__main__":
	app = AutotestLocalApp()
	app.main()
