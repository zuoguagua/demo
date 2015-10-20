"""
	Autotest command parser

"""
DEBUG = False


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
