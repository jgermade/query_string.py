#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["py_modules","package_dir"]
import os
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

path  = join(dir,"py_modules")
if exists(path) and isdir(path): # ./py_modules/
    list  = os.listdir(path)
    list = filter(lambda l:splitext(l)[1]==".py",list)
    files  = filter(lambda f:isfile(join(path,f)),list)
    py_modules  = map(lambda f:f.replace(".py",""),files)
    if py_modules:
        package_dir={'':"py_modules"}

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

