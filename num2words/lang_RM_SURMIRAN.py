# -*- coding: utf-8 -*-
# Copyright (c) 2021, Virginie Holm, recapp IT AG. All Rights Reserved.
# Based on lang_IT template from Filippo Costa.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

# Globals
# -------

ZERO = "nolla"

CARDINAL_WORDS = [
    ZERO, "en", "dus", "treis", "quatter", "tschintg", "seis", "set", "otg",
    "nov", "diesch", "endesch", "dodesch", "tredesch", "quittordesch",
    "quindesch", "sedesch", "dischset", "dischdotg", "dischnov"
]

ORDINAL_WORDS = [
    ZERO, "amprem", "sagond", "terz", "quart", "tschintgavel", "seisavel",
    "settavel", "otgavel", "novavel", "dieschavel", "endeschavel",
    "dodeschavel", "tredeschavel", "quittordeschavel", "quindeschavel",
    "sedeschavel", "dischsettavel", "dischdotgavel", "dischnovavel",
    "vantgavel"
]

# "20" = "ventg"
STR_TENS = {2: "vantga", 3: "trenta", 4: "curanta", 5: "tschuncanta",
            6: "sessanta", 7: "settanta", 8: "otganta", 9: "novanta"}

# These prefixes are used for extremely big numbers.
EXPONENT_PREFIXES = [
    ZERO, "m", "b", "tr", "quadr", "quint", "sest", "sett", "ott", "nov", "dec"
]


# Utils
# =====

def phonetic_contraction(string):
    ''' _ is a marker for "empty", i.e. no following unit

    NOTE: two forms of 1 exist (cardinal 'en' and pronoun 'egn') - form 'egn'
    is used within complex numbers, i.e. > 20
    '''
    return (string
            .replace("aen", "egn")   # ex. "trentaen" -> "trentegn"
            .replace("aotg", "otg")  # ex. "curantaotg" -> "curantotg"
            .replace("tga_", "tg")   # ex. "vantga" -> "vantg"
            .replace("_", "")
            )


def adapt_hundred(string):
    '''apply surface modifications:
         - 2: dus -> du, 3: treis -> tre
         - a/ad phonotactic adaptation
    '''
    return (string
            .replace("dustschent", "dutschent")
            .replace("treistschent", "tretschent")
            .replace("aendesch", "adendesch")
            .replace("aen", "adegn")
            .replace("aotg", "adotg")
            )


def adapt_thousand(string):
    '''apply surface modifications:
         - 2: dus -> du, 3: treis -> tre
         - a/ad phonotactic adaptation
    '''
    return (string
            .replace("dusmella", "dumella")
            .replace("treismella", "tremella")
            .replace("aendesch", "adendesch")
            .replace("aaen", "adegn")
            .replace("aaotg", "adotg")
            .replace("aa", "a")
            )


def adapt_milliarda(string):
    '''apply surface modifications:
         - article gender agreement
         - e/ed phonotactic adaptation
    '''
    string = " " + string + " "
    return (string
            .replace(" en milliarda ", " ena milliarda ")
            .replace(" a endesch", " ad endesch")
            .replace(" a en", " ad egn")
            .replace(" a otg", " ad otg")
            )


def exponent_length_to_string(exponent_length):
    # We always assume `exponent` to be a multiple of 3. If it's not true, then
    # Num2Word_RM_SURMIRAN.big_number_to_cardinal did something wrong.
    prefix = EXPONENT_PREFIXES[exponent_length // 6]
    if exponent_length % 6 == 0:
        return prefix + "illiun"
    else:
        return prefix + "illiarda"


def omitt_if_zero(number_to_string):
    return "" if number_to_string == ZERO else number_to_string


def empty_if_zero(number_to_string):
    return "_" if number_to_string == ZERO else number_to_string


# Main class
# ==========

class Num2Word_RM_SURMIRAN:
    MINUS_PREFIX_WORD = "minus "
    FLOAT_INFIX_WORD = " comma "

    def __init__(self):
        pass

    def float_to_words(self, float_number, ordinal=False):
        if ordinal:
            prefix = self.to_ordinal(int(float_number))
        else:
            prefix = self.to_cardinal(int(float_number))
        float_part = str(float_number).split('.')[1]
        postfix = " ".join(
            # Drops the trailing zero and comma
            [self.to_cardinal(int(c)) for c in float_part]
        )
        return prefix + Num2Word_RM_SURMIRAN.FLOAT_INFIX_WORD + postfix

    def tens_to_cardinal(self, number):
        tens = number // 10
        units = number % 10
        if tens in STR_TENS:
            prefix = STR_TENS[tens]
        else:
            prefix = CARDINAL_WORDS[tens][:-1] + "anta"
        # we keep track of 0 using '_' -- removed in phonetic_contraction
        postfix = empty_if_zero(CARDINAL_WORDS[units])
        return phonetic_contraction(prefix + postfix)

    def hundreds_to_cardinal(self, number):
        hundreds = number // 100
        tens = number % 100
        prefix = "tschent"
        if hundreds != 1:
            prefix = CARDINAL_WORDS[hundreds] + prefix
        postfix = omitt_if_zero(self.to_cardinal(tens))
        # "a/ad" is inserted if tens <= 13 or = 15, 16, 20, 30
        # distribution may seem unusual but it was reviewed by a native speaker
        # surmiran's "and" is normally "e/ed", but in numbers, "a/ad" is used
        infix = ""
        if (tens > 0 and tens <= 13) or tens in [15, 16, 20, 30]:
            infix = "a"
        return adapt_hundred(prefix + infix + postfix)

    def thousands_to_cardinal(self, number):
        thousands = number // 1000
        hundreds = number % 1000
        prefix = "mella"
        if thousands != 1:
            prefix = self.to_cardinal(thousands) + "mella"
        postfix = omitt_if_zero(self.to_cardinal(hundreds))
        # "a/ad" is inserted if tens <= 100
        infix = ""
        if hundreds <= 100 and postfix != "":
            infix = "a"
        return adapt_thousand(prefix + infix + postfix)

    def big_number_to_cardinal(self, number):
        digits = [c for c in str(number)]
        length = len(digits)
        if length >= 66:
            raise NotImplementedError("The given number is too large.")
        # This is how many digits come before the "illion" term.
        #   tschent milliardas => 3
        #   diesch milliuns => 2
        #   ena milliarda => 1
        predigits = length % 3 or 3
        multiplier = digits[:predigits]
        exponent = digits[predigits:]
        infix = exponent_length_to_string(len(exponent))
        if multiplier == ["1"]:
            prefix = "en "
        else:
            prefix = self.to_cardinal(int("".join(multiplier)))
            # Plural form
            infix = " " + infix + "s"
        # Read as: Does the value of exponent equal 0?
        if set(exponent) != set("0"):
            exponent_str = "".join(exponent)
            postfix = self.to_cardinal(int(exponent_str))
            # we introduce "e" if 3-digits gap before next value
            if exponent_str.startswith('000'):
                infix += " a "
            else:
                infix += " "
        else:
            postfix = ""
        return adapt_milliarda(prefix + infix + postfix).strip()

    def to_cardinal(self, number):
        if number < 0:
            string = (Num2Word_RM_SURMIRAN.MINUS_PREFIX_WORD +
                      self.to_cardinal(-number))
        elif isinstance(number, float):
            string = self.float_to_words(number)
        elif number < 20:
            string = CARDINAL_WORDS[number]
        elif number < 100:
            string = self.tens_to_cardinal(number)
        elif number < 1000:
            string = self.hundreds_to_cardinal(number)
        elif number < 1000000:
            string = self.thousands_to_cardinal(number)
        else:
            string = self.big_number_to_cardinal(number)
        return string

    def to_ordinal(self, number):
        if number < 0:
            ordinal = (Num2Word_RM_SURMIRAN.MINUS_PREFIX_WORD +
                       self.to_ordinal(-number))
            return ordinal
        elif number % 1 != 0:
            return self.float_to_words(number, ordinal=True)
        elif number <= 20:
            return ORDINAL_WORDS[number]
        else:
            cardinal = self.to_cardinal(number)
            if cardinal[-1] == 'a':
                suffix = 'vel'
            elif cardinal.endswith('set'):
                suffix = 'tavel'
            else:
                suffix = 'avel'
            return cardinal + suffix
