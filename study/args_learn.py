#!/usr/bin/env python
"""
def fun_var_args(farg,*args):
	print "arg:",farg
	for value in args:
		print "anther arg:",value


fun_var_args(1,"two",3)

"""

def fun_args(*args):
	for item in args:
		print item

fun_args()
