README
======

A Python 3 script for checking router firmware updates.

Supported Firmware
------------------

- `Asuswrt Merlin <https://asuswrt.lostrealm.ca>`__
- `DD-WRT (beta) <https://www.dd-wrt.com/>`__
- `Tomato (Shibby) <http://tomato.groov.pl>`__
- `OpenWRT <https://www.openwrt.org/>`__


Installation
------------

Requires Python >=3.2, with 3.5 or later preferred.

To get the latest stable version, install with pip:

::

    $ pip install routerchecker

If you want the latest development version, clone from Git and install with setuptools:

::

    $ git clone https://github.com/thurask/routerchecker.git
    $ cd routerchecker
    $ python setup.py install

Python Libraries
~~~~~~~~~~~~~~~~

This library requires the
`Requests <http://docs.python-requests.org/en/latest/user/install/>`__
and `Beautiful Soup 4 <https://www.crummy.com/software/BeautifulSoup/#Download>`__
libraries.


License
-------
Copyright 2016 Thurask <thuraski@hotmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the `LICENSE <LICENSE>`__ file for more details.
