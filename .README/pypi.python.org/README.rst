.. image:: https://img.shields.io/badge/language-python-blue.svg

.. image:: https://img.shields.io/pypi/pyversions/query_string.svg
   :target: https://pypi.python.org/pypi/query_string

|codacy| |landscape| |codeclimate| |scrutinizer|

.. |scrutinizer| image:: https://scrutinizer-ci.com/g/russianidiot/query_string.py/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/russianidiot/query_string.py/master
   :alt: scrutinizer-ci.com

.. |codacy| image:: https://img.shields.io/codacy/9f7c296290b84b60801f3ad5bf7c4596.svg
   :target: https://www.codacy.com/app/russianidiot-github/query_string-py/dashboard
   :alt: codacy.com

.. |codeclimate| image:: https://img.shields.io/codeclimate/github/russianidiot/query_string.py.svg
   :target: https://codeclimate.com/github/russianidiot/query_string.py
   :alt: codeclimate.com

.. |landscape| image:: https://landscape.io/github/russianidiot/query_string.py/master/landscape.svg?style=flat
   :target: https://landscape.io/github/russianidiot/query_string.py/master
   :alt: landscape.io

Install
```````

:code:`[sudo] pip install query_string`

Usage
`````

.. code:: python
	
	>>> from query_string import query_string
	
	>>> query_string(url)

Example
```````

.. code:: python
	
	>>> query_string('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
	{'k': 'v','k2': 'v2', 'k3': 'v3'}
	
	>>> query_string('k=v&k2=v2&k3=v3')
	{'k': 'v','k2': 'v2', 'k3': 'v3'}
	```

`Examples/`_

.. _Examples/: https://github.com/russianidiot/query_string.py/tree/master/Examples

Sources:

*	`py_modules/query_string.py`_

.. _`py_modules/query_string.py`: https://github.com/russianidiot/query_string.py/blob/master/py_modules/query_string.py

Feedback |github_issues| |gitter| |github_follow|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/query_string.py.svg
	:target: https://github.com/russianidiot/query_string.py/issues

.. |github_follow| image:: https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

.. |gitter| image:: https://badges.gitter.im/russianidiot/query_string.py.svg
	:target: https://gitter.im/russianidiot/query_string.py

----

`russianidiot.github.io/python/`_  - Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/

`russianidiot.github.io/cli/`_  - command line scripts

.. _russianidiot.github.io/cli/: http://russianidiot.github.io/cli/

`README.rst`_  - generated with `readmemako.py`_ (python+ `mako`_ templates) and `.README`_ dotfiles

.. _README.rst: https://github.com/russianidiot/query_string.py/blob/master/.README/pypi.python.org/README.rst
.. _readmemako.py: http://github.com/russianidiot/readmemako.py/
.. _mako: http://www.makotemplates.org/
.. _.README: https://github.com/russianidiot-dotfiles/.README
