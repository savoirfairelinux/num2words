'''
Module: num2word.py
Requires: num2word_*.py
Version: 0.2

Author:
   Taro Ogawa (tso@users.sourceforge.org)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
    Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Usage:
    from num2word import to_card, to_ord, to_ordnum
    to_card(1234567890)
    to_ord(1234567890)
    to_ordnum(12)

Notes:
    The module is a wrapper for language-specific modules.  It imports the
    appropriate modules as defined by locale settings.  If unable to
    load an appropriate module, an ImportError is raised.

History:
    0.2: n2w, to_card, to_ord, to_ordnum now imported correctly
'''
from __future__ import unicode_literals

import num2word_EN
import num2word_EN_GB
import num2word_FR
import num2word_DE
import num2word_ES
import num2word_LT

CONVERTER_CLASSES = {
    'en': num2word_EN.Num2Word_EN(),
    'en_GB': num2word_EN_GB.Num2Word_EN_GB(),
    'fr': num2word_FR.Num2Word_FR(),
    'de': num2word_DE.Num2Word_DE(),
    'es': num2word_ES.Num2Word_ES(),
    'lt': num2word_LT.Num2Word_LT(),
}

def num2words(number, ordinal=False, lang='en'):
    # We try the full language first
    if lang not in CONVERTER_CLASSES:
        # ... and then try only the first 2 letters
        lang = lang[:2]
    if lang not in CONVERTER_CLASSES:
        raise NotImplementedError()
    converter = CONVERTER_CLASSES[lang]
    if ordinal:
        return converter.to_ordinal(number)
    else:
        return converter.to_cardinal(number)
