#!/usr/bin/env python

class attrtest(object):
	
	def __init__(self):
		print "initialization"

	def trygetattr1(self):
		self.name = 'trygetattr1'
		print self.name
		print getattr(self,'name')
	
	def attribute1(self,args,options):
		print 'attribute1 args is:'+args+" and options is:"+options+'is passed in as a parameter'
		return None
	def trygetattr2(self):
		args = "run"
		options = "--verbose"
		age = getattr(self,'attribute1')(args,options)
		#print type(fun)
		#fun('crown')
		print age
	
	
	
if __name__ == "__main__":
	test = attrtest()
	test.trygetattr1()

	test.trygetattr2()

	#test.attribute1('tomato')


