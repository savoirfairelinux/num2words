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

ZERO = "nola"

CARDINAL_WORDS = [
    ZERO, "egn", "dus", "tres", "quater", "tschentg", "sis", "seat", "otg",
    "nov", "diesch", "endesch", "dudesch", "tredesch", "quitordesch",
    "quendesch", "sedesch", "gisseat", "schotg", "schenev"
]

ORDINAL_WORDS = [
    ZERO, "amprem", "savund", "tearz", "quart", "tschentgavel", "sisavel",
    "seatavel", "otgavel", "novavel", "dieschavel",  "endeschavel",
    "dudeschavel", "tredeschavel", "quitordeschavel", "quendeschavel",
    "sedeschavel", "gisseatavel", "schotgavel", "schenevavel", "veintgavel"
]

# "20" = "veintg" / surface form is restaured during phonetic adaptation phase
STR_TENS = {2: "veintga", 3: "trainta", 4: "curànta", 5: "tschuncànta",
            6: "sissànta", 7: "satànta", 8: "otgànta", 9: "novànta"}

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
            .replace("aegn", "egn")   # ex. "traintaegn" -> "traintegn"
            .replace("aotg", "otg")   # ex. "curàntaotg" -> "curàntotg"
            .replace("veintga_", "veintg")  # ex. "veintga" -> "veintg"
            .replace("_", "")
            )


def adapt_hundred(string):
    '''apply surface modifications:
         - dus/du, tres/tre
         - a/ad phonotactic adaptation
    '''
    return (string
            .replace("dustschient", "dutschient")
            .replace("trestschient", "tretschient")
            .replace("aend", "adend")
            .replace("aegn", "adegn")
            .replace("aotg", "adotg")
            )


def adapt_thousand(string):
    '''apply surface modifications:
         - dus/du, tres/tre
         - a/ad phonotactic adaptation
    '''
    return (string
            .replace("dusmeli", "dumeli")
            .replace("tresmeli", "tremeli")
            .replace("aend", "adend")
            .replace("aegn", "adegn")
            .replace("aotg", "adotg")
            )


def adapt_milliarda(string):
    '''apply surface modifications:
         - article gender agreement
         - a/ad phonotactic adaptation
    '''
    string = " " + string + " "
    return (string
            .replace(" egn miliarda ", " egna miliarda ")
            .replace("dus miliardas", "duas miliardas")
            .replace(" a end", " ad end")
            .replace(" a egn", " ad egn")
            .replace(" a otg", " ad otg")
            )


def exponent_length_to_string(exponent_length):
    # We always assume `exponent` to be a multiple of 3. If it's not true, then
    # Num2Word_RM_SUTSILV.big_number_to_cardinal did something wrong.
    prefix = EXPONENT_PREFIXES[exponent_length // 6]
    if exponent_length % 6 == 0:
        return prefix + "iliùn"
    else:
        return prefix + "iliarda"


def omitt_if_zero(number_to_string):
    return "" if number_to_string == ZERO else number_to_string


def empty_if_zero(number_to_string):
    return "_" if number_to_string == ZERO else number_to_string


# Main class
# ==========

class Num2Word_RM_SUTSILV:
    MINUS_PREFIX_WORD = "minus "
    FLOAT_INFIX_WORD = " coma "

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
        return prefix + Num2Word_RM_SUTSILV.FLOAT_INFIX_WORD + postfix

    def tens_to_cardinal(self, number):
        tens = number // 10
        units = number % 10
        if tens in STR_TENS:
            prefix = STR_TENS[tens]
        else:
            prefix = CARDINAL_WORDS[tens][:-1] + "ànta"
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
        # "a/ad" is inserted if tens <= 13 or = 15, 16, 20, 30
        # distribution may seem unusual but it was reviewed by a native speaker
        infix = ""
        if (tens > 0 and tens <= 13) or tens in [15, 16, 20, 30]:
            infix = "a"
        return adapt_hundred(prefix + infix + postfix)

    def thousands_to_cardinal(self, number):
        thousands = number // 1000
        hundreds = number % 1000
        prefix = "meli"
        if thousands != 1:
            prefix = self.to_cardinal(thousands) + "meli"
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
        #   tschient miliardas => 3
        #   diesch miliùns => 2
        #   egna miliarda => 1
        predigits = length % 3 or 3
        multiplier = digits[:predigits]
        exponent = digits[predigits:]
        infix = exponent_length_to_string(len(exponent))
        if multiplier == ["1"]:
            prefix = "egn "
        else:
            prefix = self.to_cardinal(int("".join(multiplier)))
            # Plural form
            infix = " " + infix + "s"
        # Read as: Does the value of exponent equal 0?
        if set(exponent) != set("0"):
            exponent_str = "".join(exponent)
            postfix = self.to_cardinal(int(exponent_str))
            # we introduce "a" if 3-digits gap before next value
            if exponent_str.startswith('000'):
                infix += " a "
            else:
                infix += " "
        else:
            postfix = ""
        return adapt_milliarda(prefix + infix + postfix).strip()

    def to_cardinal(self, number):
        if number < 0:
            string = (Num2Word_RM_SUTSILV.MINUS_PREFIX_WORD +
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
            ordinal = (Num2Word_RM_SUTSILV.MINUS_PREFIX_WORD +
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
            else:
                suffix = 'avel'
            return cardinal + suffix