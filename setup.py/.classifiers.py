#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["classifiers"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

# entry_points
file = join(dir,"classifiers.txt")
if exists(file) and isfile(file):
    lines = open(file).read().splitlines()
    lines = filter(lambda l:l.lstrip().rstrip(),lines)
    classifiers=lines

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))
