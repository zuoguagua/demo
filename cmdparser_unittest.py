#!/usr/bin/env python


import cmdparser


cp = cmdparser.CommandParser()

args = cp.run(["run","sleeptest"],["--verbose"])

print "args:",args
