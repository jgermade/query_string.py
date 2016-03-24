#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["scripts"]
import os
from os.path import *

repo = abspath(dirname(dirname(__file__)))

file = join(repo,"scripts.txt")
if exists(file) and isfile(file): # ./url.txt
    scripts = open(file).read().lstrip().rstrip().splitlines()
else:
    path  = join(repo,"scripts")
    if exists(path) and isdir(path):
        scripts = list(map(lambda name:join("scripts",name),
            list(filter(lambda f:isfile(join(path,f)) and f.find(" ")<0,
                os.listdir(path)
            ))
        ))
    else:
        if __name__=="__main__":
            print("SKIP: scripts NOT EXISTS")

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
