# gitfilesplit

<https://github.com/idlesign/gitfilesplit>

[![release](https://img.shields.io/pypi/v/gitfilesplit.svg)](https://pypi.python.org/pypi/gitfilesplit)
[![lic](https://img.shields.io/pypi/l/gitfilesplit.svg)](https://pypi.python.org/pypi/gitfilesplit)
[![coverage](https://img.shields.io/coveralls/idlesign/gitfilesplit/master.svg)](https://coveralls.io/r/idlesign/gitfilesplit)

## Description

*Command line helper to Git split one file into several preserving history*

Split `myhugefile.py` into three: `smaller.py`, `another.py` and `some.py` using command line:

```shell
$ gitfilesplit myhugefile.py smaller.py another.py some.py
```

The same in Python:

```python
from gitfilesplit.toolbox import split

split(
    source='myhugefile.py',
    # And with subdirectories:
    targets=['smaller.py', 'sub1/another.py', 'sub2/some.py']
)
```

Under the hood it will create several branches in which source file is moved to target locations.
After that octopus merge of these branches will be performed and temporary branches removed.

## Requirements

* Git
* Python 3.10+
