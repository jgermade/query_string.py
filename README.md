<p align="center">
	<b>query_string(string) function - get url query string dict</b>
</p>

[![Build Status](https://travis-ci.org/russianidiot/query_string.py.svg?branch=master)](https://travis-ci.org/russianidiot/query_string.py)[![PyPI](https://img.shields.io/pypi/v/query_string.svg)](https://pypi.python.org/pypi/query_string)
[![PyPI](https://img.shields.io/pypi/pyversions/query_string.svg)](https://pypi.python.org/pypi/query_string)[![PyPI](https://img.shields.io/pypi/dm/query_string.svg)](https://pypi.python.org/pypi/query_string)[![PyPI](https://img.shields.io/pypi/dw/query_string.svg)](https://pypi.python.org/pypi/query_string)[![PyPI](https://img.shields.io/pypi/dd/query_string.svg)](https://pypi.python.org/pypi/query_string)

	

### Install

[github.com](http://github.com/russianidiot/query_string.py):
`pip install git+git://github.com/russianidiot/query_string.py.git`

[pypi.python.org](https://pypi.python.org/pypi/query_string/): `pip install query_string`

[download](https://github.com/russianidiot/query_string.py/archive/master.zip): `[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

	

	

	

### Usage

**query_string(string)** function

```python
>>> from query_string import *

>>> query_string('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
{'k': 'v','k2': 'v2', 'k3': 'v3'}

>>> query_string('k=v&k2=v2&k3=v3')
{'k': 'v','k2': 'v2', 'k3': 'v3'}
```

### Links

*	Query string - Wikipedia - [en.wikipedia.org/wiki/Query_string](https://en.wikipedia.org/wiki/Query_string)

* * *

### Feedback

[![GitHub issues](https://img.shields.io/github/issues/russianidiot/query_string.py.svg)](https://github.com/russianidiot/query_string.py/issues) - Github Issues

[![Join the chat at https://gitter.im/russianidiot/query_string.py](https://badges.gitter.im/russianidiot/query_string.py.svg)](https://gitter.im/russianidiot/query_string.py) - **Chat** with me (english/russian) 

* * *

<p align="center">
my Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
<img src="http://russianidiot.github.io/images/python/16.png" />
</p>

<p align="center">
	all my repos <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	follow me <a href="http://github.com/russianidiot">github.com/russianidiot</a>
<img src="http://russianidiot.github.io/images/github/16.png" />
</p>

<p align="center">
	README.md generated with <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> (python+mako, sh)
<img src="http://russianidiot.github.io/images/book/16.png">
</p>