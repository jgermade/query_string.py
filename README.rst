.. image:: https://img.shields.io/pypi/v/query_string.svg
   :target: https://pypi.python.org/pypi/query_string

.. image:: https://img.shields.io/pypi/pyversions/query_string.svg
   :target: https://pypi.python.org/pypi/query_string

.. image:: https://img.shields.io/pypi/dm/query_string.svg
   :target: https://pypi.python.org/pypi/query_string

	

Install
~~~~~~~

github.com_: :code:`pip install git+git://github.com/russianidiot/query_string.py.git`

pypi.python.org_: :code:`pip install query_string`

download_: :code:`[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

.. _github.com: http://github.com/russianidiot/query_string.py
.. _pypi.python.org: https://pypi.python.org/pypi/query_string.py
.. _download: https://github.com/russianidiot/query_string.py/archive/master.zip

	

	

	

Usage
~~~~~

**query_string(string)** function

.. code-block:: python

	>>> from query_string import *

	>>> query_string('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
	{'k': 'v','k2': 'v2', 'k3': 'v3'}

	>>> query_string('k=v&k2=v2&k3=v3#anchor')
	{'k': 'v','k2': 'v2', 'k3': 'v3'}

Links
~~~~~

*	Query string - Wikipedia	- `en.wikipedia.org/wiki/Query_string <https://en.wikipedia.org/wiki/Query_string>`_

----

Feedback
~~~~~~~~

|github_issues| - Github Issues

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/query_string.py.svg
	:target: https://github.com/russianidiot/query_string.py/issues

|gitter| - **Chat** with me (english/russian) 

.. |gitter| image:: https://badges.gitter.im/russianidiot/query_string.py.svg
	:target: https://gitter.im/russianidiot/query_string.py

`russianidiot.github.io/python/`_  - my Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/