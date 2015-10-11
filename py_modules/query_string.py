#!/usr/bin/env python
try:
    from urlparse import *
    from urlparse import parse_qs as _parse_qs
except ImportError:
    from urllib.parse import *
    from urllib.parse import parse_qs as _parse_qs
try:
    from collections import OrderedDict # python2.7+
except ImportError:
    # python 2.6 or earlier, use backport
    from ordereddict import OrderedDict
from dict import *
from public import *
from self import *

@public
def parse_qs(query):
    kwargs = dict()
    for k,v in _parse_qs(query).iteritems():
        if len(v)==1:
            v = v[0]
        kwargs[k] = v
    return kwargs

@public
class Query_string(object):
    __query__ = None

    def __init__(self,query=None):
        self.__query__ = query

    @property
    def __odict__(self):
        tuples = []
        for pair in str(self).split('&'):
            k,v = pair.split('=',1)
            tuples.append((k,v))
        return OrderedDict(tuples)

    @self
    def update(self,**kwargs):
        __odict__ = self.__odict__
        for k in __dict__:
            for kw in kwargs:
                if k==kw:
                    __dict__[k] = kwargs[kw]
                    break
        items = []
        for k,v in __odict__.iteritems():
            items.append("=".join([k,v]))
        self.__query__ = "&".join(items)

    @self
    def add(self,key,value=""):
        items = []
        for k,v in self.iteritems():
            items.append("=".join([k,v]))
        items.append("=".join([k,v]))
        self.__query__ = "&".join(items)

    @self
    def remove(self,keys):
        if not isinstance(keys,list):
            keys = [key]
        for key in keys:
            if key in self:
                for k,v in self.iteritems():
                    items.append("=".join([k,v]))
                items.append("=".join([k,v]))
                self.__query__ = "&".join(items)

    @property
    def args(self):
        return dict(parse_qs(str(self)))

    def get(self,key):
        if key in self:
            return self[key]

    def iteritems(self):
        for k,v in self.__odict__.iteritems():
            yield (k,v)

    def __add__(self, other):
        self.__query__ = str(self)+other
        return type(self)(str(self))

    def __contains__(self, item):
        return item in self.args

    def __delattr__(self, name):
        self.remove(name)

    def __eq__(self,other):
        if isdict(other):
            return self.args == other
        return str(self) == other

    def __getattribute__(self,name):
        if hasattr(type(self),name):
            return object.__getattribute__(self,name)
        else:
            if name in self.args:
                return self.args[name]

    def __getitem__(self,key):
        if key in self.args:
            return self.args[key]

    def __getslice__(self,i,j):
        return str(self)[i:j]

    def __iter__(self):
        for key in self.__odict__:
            yield key

    def __len__(self):
        return len(str(self))

    def __nonzero__(self):
        return bool(str(self))

    def __setattr__(self,name,value):
        if hasattr(type(self),name):
            super(type(self), self).__setattr__(name,value)
        else:
            if name in self:
                self.update(name=value)
            else:
                self.add(name,value)

    def __setitem__(self, key, value):
        self.update(key=value)

    def __repr__(self):
        return self.__query__

    def __unicode__(self):
        return str(self.__query__)

@public
def query_string(url):
    if not url: return
    scheme,netloc,path,params,query,fragment = urlparse(url)
    if query:
        return Query_string(query)
    else:
        if url.find("="):
            return Query_string(url)

#url = "http://127.0.0.1:8080/pkg_info.gui/bower_components/subl/cgi.py?k=v"
#url = "https://www.kernel.org/pub/software/scm/git/docs/git-show-branch.html"
#query = query_string(url)

if __name__=="__main__":
    pass # todo

