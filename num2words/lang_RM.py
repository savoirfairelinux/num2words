# -*- coding: utf-8 -*-
# Copyright (c) 2020, Virginie Holm, recapp IT AG. All Rights Reserved.
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

ZERO = "nulla"

CARDINAL_WORDS = [
    ZERO, "in", "dus", "trais", "quatter", "tschintg", "sis", "set", "otg",
    "nov", "diesch", "indesch", "dudesch", "tredesch", "quattordesch", "quindesch",
    "sedesch", "deschset", "deschdotg", "deschnov"
]

ORDINAL_WORDS = [
    ZERO, "emprim", "segund", "terz", "quart", "tschintgavel", "sisavel",
    "settavel", "otgavel", "novavel", "dieschavel", "indeschavel", "dudeschavel",
    "tredeschavel", "quattordeschavel", "quindeschavel", "sedeschavel",
    "deschsettavel", "deschdotgavel", "deschnovavel", "ventgavel"
]

# "20" = "ventg"
STR_TENS = {2: "ventga", 3: "trenta", 4: "quaranta", 5: "tschuncanta",
            6: "sessanta", 7: "settanta", 8: "otganta", 9: "novanta"}

# These prefixes are used for extremely big numbers.
EXPONENT_PREFIXES = [
    ZERO, "m", "b", "tr", "quadr", "quint", "sest", "sett", "ott", "nov", "dec"
]


# Utils
# =====

def phonetic_contraction(string):
    ''' _ is a marker for "empty", i.e. no following unit
    '''
    return (string
            .replace("ain", "in")    # ex. "trentain" -> "trentin"
            .replace("aotg", "otg")  # ex. "quarantaotg" -> "quarantotg"
            .replace("tga_", "tg")   # ex. "ventga" -> "ventg"
            .replace("_", "")
            )

def adapt_hundred(string):
    '''apply surface modifications:
         - collective plural
         - e/ed phonotactic adaptation
    '''
    return (string
            .replace("dustschient", "duatschient")
            .replace("traistschient", "traitschient")
            .replace("ein", "edin")
            .replace("eotg", "edotg")
            )

def adapt_thousand(string):
    '''apply surface modifications:
         - collective plural
         - e/ed phonotactic adaptation
    '''
    return (string
            .replace("dusmilli", "duamilli")
            .replace("traismilli", "traimilli")
            .replace("ein", "edin")
            .replace("eotg", "edotg")
            )

def adapt_milliarda(string):
    '''apply surface modifications:
         - article gender agreement
         - e/ed phonotactic adaptation
    '''
    string = " " + string + " "
    return (string
            .replace(" in milliarda ", " ina milliarda ")
            .replace("dus milliardas", "duas milliardas")
            .replace(" e in", " ed in")
            .replace(" e otg", " ed otg")
            )

def exponent_length_to_string(exponent_length):
    # We always assume `exponent` to be a multiple of 3. If it's not true, then
    # Num2Word_RM.big_number_to_cardinal did something wrong.
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

class Num2Word_RM:
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
        return prefix + Num2Word_RM.FLOAT_INFIX_WORD + postfix

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
        prefix = "tschient"
        if hundreds != 1:
            prefix = CARDINAL_WORDS[hundreds] + prefix
        postfix = omitt_if_zero(self.to_cardinal(tens))
        # "e/ed" is inserted if tens <= 13 or = 15, 16, 20, 30
        # distribution may seem unusual but it was reviewed by a native speaker
        infix = ""
        if (tens > 0 and tens <= 13) or tens in [15, 16, 20, 30]:
            infix = "e"
        return adapt_hundred(prefix + infix + postfix)

    def thousands_to_cardinal(self, number):
        thousands = number // 1000
        hundreds = number % 1000
        prefix = "milli"
        if thousands != 1:
            prefix = self.to_cardinal(thousands) + "milli"
        postfix = omitt_if_zero(self.to_cardinal(hundreds))
        # "e/ed" is inserted if tens >= 101
        infix = ""
        if hundreds <= 100 and postfix != "":
            infix = "e"
        return adapt_thousand(prefix + infix + postfix)

    def big_number_to_cardinal(self, number):
        digits = [c for c in str(number)]
        length = len(digits)
        if length >= 66:
            raise NotImplementedError("The given number is too large.")
        # This is how many digits come before the "illion" term.
        #   tschient milliardas => 3
        #   diesch milliuns => 2
        #   ina milliarda => 1
        predigits = length % 3 or 3
        multiplier = digits[:predigits]
        exponent = digits[predigits:]
        infix = exponent_length_to_string(len(exponent))
        if multiplier == ["1"]:
            prefix = "in "
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
                infix += " e "
            else:
                infix += " "
        else:
            postfix = ""
        return adapt_milliarda(prefix + infix + postfix).strip()

    def to_cardinal(self, number):
        if number < 0:
            string = Num2Word_RM.MINUS_PREFIX_WORD + self.to_cardinal(-number)
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
        tens = number % 100
        if number < 0:
            return Num2Word_RM.MINUS_PREFIX_WORD + self.to_ordinal(-number)
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
