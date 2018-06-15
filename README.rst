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

There's only one function to use::

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
* ``pt_BR`` (Portuguese - Brazilian)
* ``sl`` (Slovene)
* ``ru`` (Russian)
* ``tr`` (Turkish)
* ``th`` (Thai)
* ``vn`` (Vietnamese)
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

**ja (Japanese)**

**reading:** whether or not to return the reading of the converted number.
Also has the special value ``"arabic"`` when used with ``year``::

    >>> num2words(42, lang='ja', reading=True)
    よんじゅうに
    >>> num2words(2017, lang='ja', to='year', reading='arabic')
    平成29年

**prefer:** when there are multiple readings or (kanji) words available,
prefer those in the sequence ``prefer``::

    >>> num2words(0, lang='ja')
    零
    >>> num2words(0, lang='ja', prefer=['〇'])
    〇
    >>> num2words(42, lang='ja', reading=True, prefer=['し'])
    しじゅうに
    >>> num2words(74, lang='ja', reading=True)
    ななじゅうよん
    >>> num2words(74, lang='ja', reading=True, prefer=['し', 'しち'])
    しちじゅうし
    >>> num2words(1375, lang='ja', to="year")
    天授元年
    >>> num2words(1375, lang='ja', to="year", prefer=['えいわ'])
    永和元年

**era:** (``year`` only) whether or not to convert the year to the era
calendar format. Defaults to ``True``::

    >>> num2words(2017, lang='ja', to='year', era=True)
    平成二十九年
    >>> num2words(2017, lang='ja', to='year', reading=True, era=True)
    へいせいにじゅうくねん
    >>> num2words(2017, lang='ja', to='year', era=False)
    二千十七年

**counter:** (``ordinal`` and ``ordinal_num`` only) which counter to use with
the ordinal number. Defaults to ``番`` and only supports ``reading`` with
it::

    >>> num2words(0, lang='ja', to='ordinal')
    零番目
    >>> num2words(1, lang='ja', to='ordinal', counter='人')
    一人目
    >>> num2words(1, lang='ja', to='ordinal', reading=True, counter='人')
    NotImplementedError: Reading not implemented for 人

History
-------

``num2words`` is based on an old library, ``pynum2word``, created by Taro Ogawa
in 2003. Unfortunately, the library stopped being maintained and the author
can't be reached. There was another developer, Marius Grigaitis, who in 2011
added Lithuanian support, but didn't take over maintenance of the project.

I am thus basing myself on Marius Grigaitis' improvements and re-publishing
``pynum2word`` as ``num2words``.

Virgil Dupras, Savoir-faire Linux
