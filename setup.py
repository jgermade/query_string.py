#!/usr/bin/env python
from distutils.core import setup # Python Standard Library
# from setuptools import setup # pypi.org/project/setuptools/ (python3.2 not supported)
try:
    from configparser import ConfigParser # python 3+
except ImportError:
    from ConfigParser import ConfigParser # python < 3.0

# ~/.pydistutils.cfg
# path/to/project.py/setup.cfg
# path/to/project.py/setup.py

def read_configuration(path):
    # setuptools.config.read_configuration read metadata/options ONLY
    result = dict()
    config = ConfigParser()
    config.read(path)
    for section in config.sections():
        for key, val in config.items(section):
            if val[0] == "\n":
                val = list(filter(None,val.splitlines()))
            result[key] = val
    return result

path = __file__.replace("setup.py","setup.cfg")
setup_cfg_data = read_configuration(path)
setup(**setup_cfg_data)
