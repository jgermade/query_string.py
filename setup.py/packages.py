#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["packages"]
import os
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

# packages
names = os.listdir(dir)
names = filter(lambda _:_.lower()!="tests",names) # exclude "tests"
names = filter(lambda name:name.find(".")<0,names) # exclude *.* names with dot
fullpaths = map(lambda name:join(dir,name),names)
dirs = filter(lambda path:isdir(path),fullpaths)
packages = filter(lambda path:exists(join(path,"__init__.py")),dirs)
packages = map(basename,packages)

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
