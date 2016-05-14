![python](https://img.shields.io/badge/language-python-blue.svg)[![PyPI](https://img.shields.io/pypi/pyversions/query_string.svg)](https://pypi.python.org/pypi/query_string)

[![codacy.com](https://img.shields.io/codacy/9f7c296290b84b60801f3ad5bf7c4596.svg)](https://www.codacy.com/app/russianidiot-github/query_string-py/dashboard)[![landscape.io](https://landscape.io/github/russianidiot/query_string.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/query_string.py/master)[![Code Climate](https://img.shields.io/codeclimate/github/russianidiot/query_string.py.svg)](https://codeclimate.com/github/russianidiot/query_string.py)
[![Code Health](https://scrutinizer-ci.com/g/russianidiot/query_string.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/query_string.py)

[![Build Status](https://travis-ci.org/russianidiot/query_string.py.svg?branch=master)](https://travis-ci.org/russianidiot/query_string.py)[![drone.io](https://drone.io/github.com/russianidiot/query_string.py/status.png)](https://drone.io/github.com/russianidiot/query_string.py)[![Wercker](https://img.shields.io/wercker/ci/russianidiot/query_string.py.svg)](https://app.wercker.com/#applications/570bed743f1a891374045c2f/)
[![codecov.io](https://codecov.io/github/russianidiot/query_string.py/coverage.svg?branch=master)](https://codecov.io/github/russianidiot/query_string.py?branch=master)

[![PyPI](https://img.shields.io/pypi/v/query_string.svg)](https://pypi.python.org/pypi/query_string)
[![PyPI](https://img.shields.io/pypi/dm/query_string.svg)](https://pypi.python.org/pypi/query_string)
[![PyPI](https://img.shields.io/pypi/dd/query_string.svg)](https://pypi.python.org/pypi/query_string)

<p align="center">
    <b>query_string(string) function - get url query string dict</b>
</p>

#### Install

pip: 
`[sudo] pip install query_string`

#### Usage

```python
>>> from query_string import query_string

>>> query_string(url)
```

#### Example

```python
>>> query_string('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
{'k': 'v','k2': 'v2', 'k3': 'v3'}

>>> query_string('k=v&k2=v2&k3=v3')
{'k': 'v','k2': 'v2', 'k3': 'v3'}
```
```

[Examples/](https://github.com/russianidiot/query_string.py/tree/master/Examples)

Sources:
*	[py_modules/query_string.py](https://github.com/russianidiot/query_string.py/blob/master/py_modules/query_string.py)

### Links

*	Query string - Wikipedia - [en.wikipedia.org/wiki/Query_string](https://en.wikipedia.org/wiki/Query_string)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/query_string.py.svg)](https://github.com/russianidiot/query_string.py/issues)
[![Join the chat at https://gitter.im/russianidiot/query_string.py](https://badges.gitter.im/russianidiot/query_string.py.svg)](https://gitter.im/russianidiot/query_string.py)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)

* * *

<p align="center">
	Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
	<img src="http://russianidiot.github.io/images/python/16.png" />
</p>
<p align="center">
	cli packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/cli/</a>
<img src="http://russianidiot.github.io/images/cli/16.png" />
</p>

<p align="center">
	repos list <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	<a href="https://raw.githubusercontent.com/russianidiot/query_string.py/master/README.md">README.md</a> generated with <a href="https://github.com/russianidiot/readme-mako.py">readmemako.py</a> (python+<a href="http://www.makotemplates.org/">mako</a> templates) and <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> dotfiles 
<img src="http://russianidiot.github.io/images/book/16.png">
</p>
