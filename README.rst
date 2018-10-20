num2words - Convert numbers to words in multiple languages
==========================================================

.. image:: https://img.shields.io/pypi/v/num2words.svg
   :target: https://pypi.python.org/pypi/num2words

.. image:: https://travis-ci.org/savoirfairelinux/num2words.svg?branch=master
    :target: https://travis-ci.org/savoirfairelinux/num2words

.. image:: https://coveralls.io/repos/github/savoirfairelinux/num2words/badge.svg?branch=master
    :target: https://coveralls.io/github/savoirfairelinux/num2words?branch=master


``num2words`` is a library that converts numbers like ``42`` to words like ``forty-two``.
It supports multiple languages (see the list below for full list
of languages) and can even generate ordinal numbers like ``forty-second``
(although this last feature is a bit buggy for some languages at the moment).

The project is hosted on GitHub_. Contributions are welcome.

.. _GitHub: https://github.com/savoirfairelinux/num2words

Installation
------------

The easiest way to install ``num2words`` is to use pip::

    pip install num2words

Otherwise, you can download the source package and then execute::

    python setup.py install

The test suite in this library is new, so it's rather thin, but it can be run with::

    python setup.py test

Usage
-----
Command line::

    $ num2words 10001
    ten thousand and one
    $ num2words 10123123 --lang es
    diez millones ciento veintitrés mil ciento veintitrés
    $ num2words 24,120.10
    twenty-four thousand, one hundred and twenty point one
    $ num2words 24,120.10 -l es
    veinticuatro mil ciento veinte punto uno
    $num2words 2.14 -l es --to currency
    dos euros con catorce centimos

In code there's only one function to use::

    >>> from num2words import num2words
    >>> num2words(42)
    forty-two
    >>> num2words(42, to='ordinal')
    forty-second
    >>> num2words(42, lang='fr')
    quarante-deux

Besides the numerical argument, there are two main optional arguments.

**to:** The converter to use. Supported values are:

* ``cardinal`` (default)
* ``ordinal``
* ``ordinal_num``
* ``year``
* ``currency``

**lang:** The language in which to convert the number. Supported values are:

* ``en`` (English, default)
* ``ar`` (Arabic)
* ``cz`` (Czech)
* ``de`` (German)
* ``dk`` (Danish)
* ``en_GB`` (English - Great Britain)
* ``en_IN`` (English - India)
* ``es`` (Spanish)
* ``es_CO`` (Spanish - Colombia)
* ``es_VE`` (Spanish - Venezuela)
* ``eu`` (EURO)
* ``fi`` (Finnish)
* ``fr`` (French)
* ``fr_CH`` (French - Switzerland)
* ``fr_BE`` (French - Belgium)
* ``fr_DZ`` (French - Algeria)
* ``he`` (Hebrew)
* ``id`` (Indonesian)
* ``it`` (Italian)
* ``ja`` (Japanese)
* ``lt`` (Lithuanian)
* ``lv`` (Latvian)
* ``no`` (Norwegian)
* ``pl`` (Polish)
* ``pt`` (Portuguese)
* ``pt_BR`` (Portuguese - Brazilian)
* ``ro`` (Romanian)
* ``ru`` (Russian)
* ``sl`` (Slovene)
* ``tr`` (Turkish)
* ``th`` (Thai)
* ``vi`` (Vietnamese)
* ``nl`` (Dutch)
* ``uk`` (Ukrainian)

You can supply values like ``fr_FR``; if the country doesn't exist but the
language does, the code will fall back to the base language (i.e. ``fr``). If
you supply an unsupported language, ``NotImplementedError`` is raised.
Therefore, if you want to call ``num2words`` with a fallback, you can do::

    try:
        return num2words(42, lang=mylang)
    except NotImplementedError:
        return num2words(42, lang='en')

Additionally, some converters and languages support other optional arguments
that are needed to make the converter useful in practice.

Wiki
----
For additional information on some localization please check the Wiki_.
And feel free to propose wiki enhancement.

.. _Wiki: https://github.com/savoirfairelinux/num2words/wiki

History
-------

``num2words`` is based on an old library, ``pynum2word``, created by Taro Ogawa
in 2003. Unfortunately, the library stopped being maintained and the author
can't be reached. There was another developer, Marius Grigaitis, who in 2011
added Lithuanian support, but didn't take over maintenance of the project.

I am thus basing myself on Marius Grigaitis' improvements and re-publishing
``pynum2word`` as ``num2words``.

Virgil Dupras, Savoir-faire Linux
