#!/usr/bin/env python

import string
import random

field = string.letters + string.digits

def getRandom():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == "__main__":
    print generate(20)
