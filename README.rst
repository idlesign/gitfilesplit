gitfilesplit
============
https://github.com/idlesign/gitfilesplit

|release| |lic| |ci| |coverage|

.. |release| image:: https://img.shields.io/pypi/v/gitfilesplit.svg
    :target: https://pypi.python.org/pypi/gitfilesplit

.. |lic| image:: https://img.shields.io/pypi/l/gitfilesplit.svg
    :target: https://pypi.python.org/pypi/gitfilesplit

.. |ci| image:: https://img.shields.io/travis/idlesign/gitfilesplit/master.svg
    :target: https://travis-ci.org/idlesign/gitfilesplit

.. |coverage| image:: https://img.shields.io/coveralls/idlesign/gitfilesplit/master.svg
    :target: https://coveralls.io/r/idlesign/gitfilesplit


Description
-----------

*Command line helper to Git split one file into several preserving history*


Split `myhugefile.py` into three: `smaller.py`, `another.py` and `some.py` using command line:

.. code-block::

    $ gitfilesplit myhugefile.py smaller.py another.py some.py


The same in Python:

.. code-block::

    from gitfilesplit.toolbox import split

    split(
        source='myhugefile.py',
        targets=['smaller.py', 'another.py', 'some.py']
    )


Under the hood it will create several branches in which source file is moved to target locations.
After that octopus merge of these branches will be performed and temporary branches removed.


Requirements
------------

* Git
* Python 3.6+
