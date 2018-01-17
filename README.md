<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->


[![](https://img.shields.io/badge/Language-Python-blue.svg?style=plastic)]()
[![](https://img.shields.io/pypi/pyversions/query_string.svg)](https://pypi.org/pypi/query_string)
[![](https://img.shields.io/pypi/v/query_string.svg)](https://pypi.org/pypi/query_string)

[![](https://api.codacy.com/project/badge/Grade/da7cca99ede548f9aa1ac583d39f4afd)](https://www.codacy.com/app/russianidiot/query_string-py)
[![](https://codeclimate.com/github/russianidiot/query_string.py/badges/gpa.svg)](https://codeclimate.com/github/russianidiot/query_string.py)
[![](https://landscape.io/github/russianidiot/query_string.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/query_string.py)
[![](https://scrutinizer-ci.com/g/russianidiot/query_string.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/query_string.py/)

[![](https://scrutinizer-ci.com/g/russianidiot/query_string.py/badges/build.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/query_string.py/)
[![](https://semaphoreci.com/api/v1/russianidiot/query_string-py/branches/master/badge.svg)](https://semaphoreci.com/russianidiot/query_string-py)
[![](https://api.travis-ci.org/russianidiot/query_string.py.svg?branch=master)](https://travis-ci.org/russianidiot/query_string.py/)
[![](https://app.wercker.com/status/41a0b06a61890066f9102fcde8e111cb/s/master)](https://app.wercker.com/russianidiot/query_string.py)



### Install

`[sudo] pip install query_string`




### Usage

```python
>>> from query_string import query_string

>>> query_string(url)
```


### Examples

```python
>>> query_string('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
{'k': 'v','k2': 'v2', 'k3': 'v3'}

>>> query_string('k=v&k2=v2&k3=v3')
{'k': 'v','k2': 'v2', 'k3': 'v3'}
```





Feedback
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/query_string.py.svg)](https://github.com/russianidiot/query_string.py/issues)

