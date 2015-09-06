#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=[]
import os
from os.path import *
from imp import *
from setuptools import *
import sys

# https://docs.python.org/2/distutils/setupscript.html
# https://docs.python.org/3/distutils/setupscript.html

def pyfiles(dir):
    list = os.listdir(dir)
    list = filter(lambda l:splitext(l)[1]==".py",list)
    return list

def main():
    if not dirname(__file__): # python setup.py
        dir = getcwd()
    else: # setup.py, python /path/to/setup.py
        dir = dirname(dirname(__file__))

    sys.path.append(dir)
    kwargs=dict()

    sys.path.append(dirname(__file__))
    files = pyfiles(dirname(__file__))
    for file in files:
        try:
            mod = __import__(file.replace(".py",""))
            if not hasattr(mod,'__all__'):
                raise ValueError("ERROR: %s __all__ required" % file)
            for k in getattr(mod,"__all__"):
                if getattr(mod,k):
                    kwargs[k] = getattr(mod,k)
        except AttributeError: # variable from __all__ not initialized
            continue
        if len(sys.argv)==1 and len(getattr(mod,"__all__"))>0:
            print("%s: %s" % (file,mod.__all__))

    name = basename(dir).lower().replace(".py","")
    while name and name[-1]=="_": 
        name=name[0:-1]

    if len(sys.argv)==1 and kwargs:
        print('\nsetup(name="%s",' % name)
        for i,(k,v) in enumerate(sorted(kwargs.iteritems(),key=lambda (k,v):k),1):
            print("    %s = %s%s" % (k,'"%s"' % v if isinstance(v,(str,unicode)) else v,"," if i!=len(kwargs) else ""))
        print(')')  

    if len(sys.argv)==1: return
    setup(name=name,**kwargs)

if __name__=="__main__":
    main()
