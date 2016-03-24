**query_string(string)** function

```python
>>> from query_string import *

>>> query_string('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
{'k': 'v','k2': 'v2', 'k3': 'v3'}

>>> query_string('k=v&k2=v2&k3=v3')
{'k': 'v','k2': 'v2', 'k3': 'v3'}
```