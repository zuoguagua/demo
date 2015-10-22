"""
	Autotest command parser

"""
DEBUG = False
import os 
import re

LOCALDIRTEST = "tests"

class CommandParser(object):

	COMMAND_LIST = ['help','list','run','fetch','bootstrap']

	def __init__(self):
		print "CMDPARSER"
	
	def help():
		print "help."

	
	def parse_args(self,args,options):
		if len(args) and args[0] in self.COMMAND_LIST:
			cmd = args.pop(0)
		else:
			return args

		if cmd == 'list':
			cmd = 'list_tests'

		try:
			try:
				args = getattr(self,cmd)(args,options)
			except TypeError:
				args = getattr(self,cmd)()
		except SystemExit,return_code:
			sys.exit(return_code.code)
		except Exception,error_detail:
			if DEBUG:
				raise
			sys.stderr.write("Command failed:%s-%s\n"%(cmd,eror_detail))
			self.help()
			sys.exit(1)

		return args
	
	def run(self,args,options):
		print "run"
		if not len(args):
			self.help()

		test = args.pop(0)
		print "test:",test
		if not re.search("control",test):
			test = test+"/control"
	
		localdir = os.path.join(os.path.abspath(os.path.curdir),LOCALDIRTEST)
		print "localdir:",localdir
		if localdir:
			d = os.path.join(localdir,test)
			print "d:",d
			if os.path.isfile(d):
				args.insert(0,d)
				return args


