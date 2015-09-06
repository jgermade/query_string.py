#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["install_requires"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

install_requires = []
for name in ["requirements.txt","requires.txt","install_requires.txt"]:
    file = join(dir,name)
    if exists(file):
        lines = open(file).read().splitlines()
        lines = filter(lambda l:l.lstrip().rstrip(),lines)
        install_requires=lines

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))

