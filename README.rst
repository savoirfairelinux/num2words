num2words - Convert numbers to words in multiple languages
==========================================================

.. image:: https://travis-ci.org/savoirfairelinux/num2words.svg?branch=master
    :target: https://travis-ci.org/savoirfairelinux/num2words

``num2words`` is a library that converts numbers like ``42`` to words like
``forty-two``. It supports multiple languages (see the list below for full list
of languages) and can even generate ordinal numbers like ``forty-second``
(although this last feature is a bit buggy for some languages at the moment).

The project is hosted on https://github.com/savoirfairelinux/num2words

Installation
------------

The easiest way to install ``num2words`` is to use pip::

    pip install num2words

Otherwise, you can download the source package and then execute::

    python setup.py install

The test suite in this library new, so it's rather thin, but it can be ran with::

    python setup.py test

Usage
-----

There's only one function to use::

    >>> from num2words import num2words
    >>> num2words(42)
    forty-two
    >>> num2words(42, ordinal=True)
    forty-second
    >>> num2words(42, lang='fr')
    quarante-deux

Besides the numerical argument, there's two optional arguments.

**ordinal:** A boolean flag indicating to return an ordinal number instead of a
cardinal one.

**lang:** The language in which to convert the number. Supported values are:

* ``en`` (English, default)
* ``ar`` (Arabic)
* ``de`` (German)
* ``dk`` (Danish)
* ``en_GB`` (English - Great Britain)
* ``en_IN`` (English - India)
* ``es`` (Spanish)
* ``es_CO`` (Spanish - Colombia)
* ``es_VE`` (Spanish - Venezuela)
* ``es_MX`` (Spanish - Mexico)
* ``eu`` (EURO)
* ``fr`` (French)
* ``fr_CH`` (French - Switzerland)
* ``fr_DZ`` (French - Algeria)
* ``he`` (Hebrew)
* ``id`` (Indonesian)
* ``it`` (Italian)
* ``lt`` (Lithuanian)
* ``lv`` (Latvian)
* ``no`` (Norwegian)
* ``pl`` (Polish)
* ``pt_BR`` (Brazilian Portuguese)
* ``ru`` (Russian)
* ``tr`` (Turkish)
* ``vn`` (Vietnamese)


You can supply values like ``fr_FR``, the code will be correctly interpreted. If
you supply an unsupported language, ``NotImplementedError`` is raised.
Therefore, if you want to call ``num2words`` with a fallback, you can do::

    try:
        return num2words(42, lang=mylang)
    except NotImplementedError:
        return num2words(42, lang='en')

History
-------

``num2words`` is based on an old library, ``pynum2word`` created by Taro Ogawa
in 2003. Unfortunately, the library stopped being maintained and the author
can't be reached. There was another developer, Marius Grigaitis, who in 2011
added Lithuanian support, but didn't take over maintenance of the project.

I am thus basing myself on Marius Grigaitis' improvements and re-publishing
``pynum2word`` as ``num2words``.

Virgil Dupras, Savoir-faire Linux
