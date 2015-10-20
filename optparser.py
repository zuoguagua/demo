"""
	Autotest client/local option parser
"""

import sys
import optparse

from cmdparser import CommandParser
__all__ = ['AutotestLocalOptionParser']

class AutotestLocalOptionParser(optparse.OptionParser):
	def __init__(self):
		command_info = ('[command]\t\tOne of:%s'%",".join(CommandParser.COMMAND_LIST))
		
		if sys.version_info[0:2] < (2,6):
			optparse.OptionParser.__init__(self,usage='Usage:%prog [options] [command] <control-file>',description=command_info)
		else:
			optparse.OptionParser.__init__(self,usage='Usage:%prog [options] [command] <control-file>',epilog=command_info)
	
		general = optparse.OptionGroup(self,'GENERAL JOB CONTROL')
		general.add_option("-a","--args",dest='args',help='additional args to pass to control file')


		print "OPTPARSER"


