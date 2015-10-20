#!/usr/bin/env python


DEBUG = False

class CommandParser(object):
	COMMAND_LIST = ['help','list','run']
	
	@classmethod
	def list_tests(cls):
		pass
	def run(self,args,options):
		print "run"
	def parse_args(self,args,options):
		print "parse_args"
		print len(args)
		print args[0]
		if len(args) and args[0] in self.COMMAND_LIST:
			cmd = args.pop(0)
		else:
			print  args

		#if cmd == 'list':
		#	cmd = 'list_tests' 
		args = getattr(self,cmd)
		print args
		


if __name__ == "__main__":
	print "Begin"
	app = CommandParser()
	name = ["run","control"]
	app.parse_args(name,'')
