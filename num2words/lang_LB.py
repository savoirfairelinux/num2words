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

# Luxembourgish implementation for num2words

from __future__ import print_function, unicode_literals

import re

from .lang_EU import Num2Word_EU

DOLLAR = ('Dollar', 'Dollar')
CENTS = ('Cent', 'Cent')

class Num2Word_LB(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('Euro', 'Euro'), CENTS),
        'AUD': (DOLLAR, CENTS),
        'CAD': (DOLLAR, CENTS),
        'USD': (DOLLAR, CENTS),
        'GBP': (('Pond', 'Pond'), ('Penny', 'Pennies')),
        'CHF': (('Schwäizer Frang', 'Schwäizer Frang'), ('Rappen', 'Rappen')),
    }
    
    GIGA_SUFFIX = "illiard"
    MEGA_SUFFIX = "illioun"

    def setup(self):
        super(Num2Word_LB, self).setup()
        self.negword = "minus "
        self.pointword = "Komma"
        self.exclude_title = ["a", "an", "Komma", "minus"]
        
        # "Cannot treat float %s as ordinal."
        self.errmsg_floatord = (
            "D'Kommazuel %s kann net an eng Ordnungszuel " +
            "ëmgewandelt ginn."
        )
        # "type(((type(%s)) ) not in [long, int, float]"
        self.errmsg_nonnum = (
            "Nëmmen Zuelen (type(%s)) kënnen a Wierder ëmgewandelt ginn."
        )
        # "Cannot treat negative num %s as ordinal."
        self.errmsg_negord = (
            "D'negativ Zuel %s kann net an eng Ordnungszuel " +
            "ëmgewandelt ginn."
        )
        # "abs(%s) must be less than %s."
        self.errmsg_toobig = "D'Zuel %s muss méi kleng si wéi %s."
        self.exclude_title = []

        lows = ["Non", "Okt", "Sept", "Sext", "Quint", "Quadr", "Tr", "B", "M"]
        units = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept",
                 "okto", "novem"]
        tens = ["dez", "vigint", "trigint", "quadragint", "quinquagint",
                "sexagint", "septuagint", "oktogint", "nonagint"]
        self.high_numwords = (
            ["zent"] + self.gen_high_numwords(units, tens, lows)
        )

        self.mid_numwords = [
            (1000, "dausend"), (100, "honnert"),
            (90, "nonzeg"), (80, "achtzeg"), (70, "siwwenzeg"),
            (60, "sechzeg"), (50, "fofzeg"), (40, "véierzeg"),
            (30, "drësseg")
        ]
        self.low_numwords = [
            "zwanzeg", "nonzéng", "uechtzéng", "siwwenzéng", "siechzéng",
            "fofzéng", "véierzéng", "dräizéng", "zwielef", "eelef", "zéng",
            "néng", "aacht", "siwen", "sechs", "fënnef", "véier", "dräi",
            "zwee", "eent", "null"
        ]

        self.ords = {
            "een": "éisch",
            "eng": "éisch",
            "eent": "éisch",
            "dräi": "drët",
            "aacht": "aach",
            "eg": "egs",
            "nen": "ns",
            "rden": "rds",
            "ert": "erts",
            "end": "ends",
            "ioun": "iouns",
            "iard": "iards"}

    def should_drop_n(self, following):
        return following[0] not in 'aeioundtzh'
      
    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum == 100 or nnum == 1000:
                return (ntext, nnum)
            elif nnum < 10 ** 6:
                return next
            ctext = "eng"

        if nnum > cnum:
            if nnum >= 10 ** 6:
                if cnum > 1:
                    if ntext.endswith("e"):
                        ntext += "n"
                    else:
                        ntext += "en"
                ctext += " "
            val = cnum * nnum
        else:
            if nnum < 10 < cnum < 100:
                conjunction = "an" if not self.should_drop_n(ctext) else "a"
                if nnum == 1:
                    ntext = "een"
                ntext, ctext = ctext, ntext + conjunction
            elif cnum >= 10 ** 6:
                ctext += " "
            val = cnum + nnum

        word = ctext + ntext
        
        return (word, val)
      
    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outword = self.to_cardinal(value).lower()
        for key in self.ords:
            if outword.endswith(key):
                outword = outword[:len(outword) - len(key)] + self.ords[key]
                break

        res = outword + "t"

        # Exception: "honnertst" is usually preferred over "eenthonnertst"
        if res in ["eendausendst", "eenhonnertst"]:
            res = res.replace("een", "", 1)
        # ... similarly for "milliounst" etc.
        res = re.sub(r'eng ([a-z]+(illioun|illiard)st)$',
                     lambda m: m.group(1), res)
        # Ordinals involving "Milliounst" etc. are written without a space.
        res = re.sub(r' ([a-zA-Z]+(illioun|illiard)st)$',
                     lambda m: m.group(1), res)

        return res

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "."

    def to_currency(self, val, currency='EUR', cents=True, separator=' an', adjective=False):
        result = super(Num2Word_LB, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        return result.replace("eent ", "een ")

    def to_year(self, val, longval=True):
        if val < 0:
            return self.to_cardinal(abs(val)) + ' viru Christus'
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="honnert", longval=longval).replace(' ', '')

