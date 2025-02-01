# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

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

from .currency import parse_currency_parts
from .lang_EU import Num2Word_EU

SMALL_CARDINALS = (
    "zero un doî trei quattro çinque sëi sette eutto neuve dexe unze dozze"
    " trezze quattòrze chinze sezze dïsette dixeutto dixineuve"
).split()

TENS = (
    "zero dexe vinti trenta quaranta çinquanta sciuscianta settanta"
    " ottanta novanta"
).split()

HUNDREDS = "zero çento duxento trexento".split()

THOUSANDS = "zero mille doamia træmia".split()

EXPONENTS = (
    "mion miliardo bilion biliardo trilion triliardo quadrilion quadriliardo"
    " quintilion quintiliardo"
).split()

SMALL_ORDINALS = (
    "zero primmo segondo terso quarto quinto sesto setten otten noven dexen"
    " unzen dozzen trezzen quattorzen chinzen sezzen dïsetten dixotten"
    " dixinoven"
).split()

CENTS = ("citto", "citti")
DOLLAR = (("dòllao", "dòllai"), CENTS)
FRANC = (("franco", "franchi"), CENTS)
CURRENCIES_FEM = {"GBP", "INR", "ISK", "ITL"}


class Num2Word_LIJ(Num2Word_EU):
    CURRENCY_FORMS = {
        "AUD": DOLLAR,
        "CAD": DOLLAR,
        "CHF": FRANC,
        "CNY": (("yuan", "yuan"), ("fen", "fen")),
        "EUR": (("euro", "euro"), CENTS),
        "FRF": FRANC,
        "GBP": (("sterliña", "sterliñe"), ("penny", "pence")),
        "HKD": DOLLAR,
        "INR": (("rupia", "rupie"), ("paisa", "paise")),
        "ITL": (("lia", "lie"), CENTS),
        "JPY": (("yen", "yen"), ("sen", "sen")),
        "SGD": DOLLAR,
        "NZD": DOLLAR,
        "USD": DOLLAR,
    }
    CURRENCY_ADJECTIVES = {
        "AUD": ("australian", "australien"),
        "CAD": ("canadeise", "canadeixi"),
        "CHF": ("svissero", "svisseri"),
        "FRF": ("franseise", "franseixi"),
        "HKD": ("de Hong Kong", "de Hong Kong"),
        "ITL": ("italiaña", "italiañe"),
        "SGD": ("de Scingapô", "de Scingapô"),
        "NZD": ("neozelandeise", "neozelandeixi"),
        "USD": ("american", "americhen"),
    }
    MINUS_PREFIX_WORD = "meno "
    FLOAT_INFIX_WORD = " virgola "

    def setup(self):
        Num2Word_EU.setup(self)

    def __init__(self):
        pass

    def float_to_words(
        self, float_number, gender="m", plural=False, ordinal=False
    ):
        if ordinal:
            prefix = self.to_ordinal(int(float_number), gender, plural)
        else:
            prefix = self.to_cardinal(int(float_number), gender)
        float_part = str(float_number).split(".")[1]
        postfix = " ".join(
            # Drops the trailing zero and comma
            [self.to_cardinal(int(c)) for c in float_part]
        )
        return prefix + Num2Word_LIJ.FLOAT_INFIX_WORD + postfix

    def small_to_cardinal(self, number, gender):
        assert number < 20
        string = SMALL_CARDINALS[number]
        if gender == "f":
            if number == 1:
                string = string[:-1] + "ña"
            if number == 2:
                string = string[:-1] + "e"
            if number == 3:
                string = string[:-2] + "æ"
        return string

    def tens_to_cardinal(self, number, gender):
        assert 20 <= number < 100
        tens, units = number // 10, number % 10
        string = TENS[tens]
        # Bare tens
        if units == 0:
            return string
        # Tens + units, with phonetic contractions
        if tens != 2:
            string = string[:-1] + "e"
        if units in (1, 8):
            string = string[:-1]
        gender = gender if units != 1 else "m"
        string += self.small_to_cardinal(units, gender)
        return string

    def hundreds_to_cardinal(self, number, gender):
        assert 100 <= number < 1000
        hundreds, remainder = number // 100, number % 100
        if hundreds < len(HUNDREDS):
            string = HUNDREDS[hundreds]
            if 80 <= remainder <= 89:
                string = string[:-1]
        else:
            string = self.small_to_cardinal(hundreds, gender="m")
            string = string.replace("ë", "e")
            # Phonetic adjustment
            if 80 <= remainder <= 89:
                string += "çent"
            else:
                string += "çento"
        if not remainder:
            return string
        else:
            gender = gender if remainder != 1 else "m"
            return string + self.to_cardinal(remainder, gender)

    def thousands_to_cardinal(self, number, gender):
        assert 1000 <= number < 1000000
        thousands, remainder = number // 1000, number % 1000
        if thousands < len(THOUSANDS):
            string = THOUSANDS[thousands]
        else:
            string = self.to_cardinal(thousands, gender="m")
            # fossilised forms doa- and træ-
            string = string.replace("doî", "doa")
            string = string.replace("trei", "træ")
            # no length markers on "sëi"
            string = string.replace("ë", "e")
            # no grave accent on "quattòrze" since it isn't the main stress
            string = string.replace("ò", "o")
            string += "mia"
        if not remainder:
            return string
        else:
            gender = gender if remainder != 1 else "m"
            return string + self.to_cardinal(remainder, gender)

    def big_number_to_cardinal(self, number, gender):
        assert number >= 1000000
        mils, remainder = number // 1000000, number % 1000000
        rev_mils = str(mils)[::-1]
        triplets = [
            int(rev_mils[i:i + 3][::-1]) for i in range(0, len(rev_mils), 3)
        ]
        if len(triplets) > len(EXPONENTS):
            raise NotImplementedError("The given number is too large.")
        if remainder:
            gender = gender if remainder != 1 else "m"
            string = self.to_cardinal(remainder, gender)
        else:
            string = ""
        for triplet, exponent in zip(triplets, EXPONENTS):
            if triplet == 0:
                prefix = ""
            elif triplet == 1:
                prefix = "un " + exponent
            else:
                prefix = self.to_cardinal(triplet) + " "
                if exponent.endswith("n"):
                    prefix += exponent[:-1] + "in"
                elif exponent.endswith("o"):
                    prefix += exponent[:-1] + "i"
            if prefix:
                if string:
                    if " e " in string:
                        string = prefix + ", " + string
                    else:
                        string = prefix + " e " + string
                else:
                    string = prefix
        return string

    def to_cardinal(self, number, gender="m"):
        if number < 0:
            string = self.MINUS_PREFIX_WORD + self.to_cardinal(-number, gender)
        elif int(number) != number:
            string = self.float_to_words(number, gender)
        elif number < 20:
            string = self.small_to_cardinal(int(number), gender)
        elif number < 100:
            string = self.tens_to_cardinal(int(number), gender)
        elif number < 1000:
            string = self.hundreds_to_cardinal(int(number), gender)
        elif number < 1000000:
            string = self.thousands_to_cardinal(int(number), gender)
        else:
            string = self.big_number_to_cardinal(int(number), gender)
        return string

    def small_to_ordinal(self, number, gender, plural):
        assert number < 20
        string = SMALL_ORDINALS[int(number)]
        if gender == "f" and string != "zero":
            if string.endswith("o"):
                string = string[:-1] + "a"
            elif string.endswith("en"):
                string = string[:-1] + "ña"
        if plural and string != "zero":
            if string.endswith("o"):
                string = string[:-1] + "i"
            elif string.endswith("a"):
                string = string[:-1] + "e"
        return string

    def big_to_odinal(self, number, gender, plural):
        assert number >= 20
        string = self.to_cardinal(number)
        # Adjust diacritics and perform contractions
        if string.endswith("ëi") or string.endswith("ei"):
            string = string[:-2] + "ei"
        elif string.endswith("quattòrze"):
            string = string[:-4] + "orze"
        elif string.endswith("î"):
            string = string[:-1] + "i"
        elif string[-1] in "oeai":
            string = string[:-1]
        string += "eximo"
        # Additional phonetic adjustments
        if string.endswith("mieximo"):
            string = string[:-5] + "lleximo"
        elif string.endswith("oeutteximo"):
            string = string[:-10] + "otteximo"
        elif string.endswith("eutteximo"):
            string = string[:-9] + "otteximo"
        elif string.endswith("neuveximo"):
            string = string[:-8] + "oveximo"
        # Gender/number adjustment
        if gender == "f":
            if plural:
                string = string[:-1] + "e"
            else:
                string = string[:-1] + "a"
        elif plural:
            string = string[:-1] + "i"
        return string

    def to_ordinal(self, number, gender="m", plural=False):
        if number < 0:
            return self.MINUS_PREFIX_WORD + self.to_ordinal(
                -number, gender, plural
            )
        elif number % 1 != 0:
            return self.float_to_words(number, gender, plural, ordinal=True)
        elif number < 20:
            string = self.small_to_ordinal(number, gender, plural)
        else:
            string = self.big_to_odinal(number, gender, plural)
        return string

    def to_currency(
        self, val, currency="EUR", cents=True, separator=" e", adjective=False
    ):
        left, right, is_negative = parse_currency_parts(val)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]

        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"'
                % (currency, self.__class__.__name__)
            )

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            adjs = self.CURRENCY_ADJECTIVES[currency]
            cr1 = (
                "%s %s" % (cr1[0], adjs[0]),
                "%s %s" % (cr1[1], adjs[1]),
            )

        gender = "f" if currency in CURRENCIES_FEM else "m"
        minus_str = "%s " % self.negword.strip() if is_negative else ""
        money_str = self.to_cardinal(left, gender)
        cents_str = self.to_cardinal(right) if cents else "%02d" % right

        return "%s%s %s%s %s %s" % (
            minus_str,
            money_str,
            self.pluralize(left, cr1),
            separator,
            cents_str,
            self.pluralize(right, cr2),
        )
