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

from __future__ import print_function, unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_LU(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('Euro', 'Euro'), ('Cent', 'Cent')),
        'GBP': (('Pond', 'Pond'), ('Penny', 'Pence')),
        'USD': (('Dollar', 'Dollar'), ('Cent', 'Cent')),
    }

    GIGA_SUFFIX = "illiard"
    MEGA_SUFFIX = "illion"

    def setup(self):
        self.negword = "minus "
        self.pointword = "Komma"

        lows = ["Non", "Okt", "Sept", "Sext", "Quint", "Quadr", "Tr", "B", "M"]
        units = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept",
                 "okto", "novem"]
        tens = ["dez", "vigint", "trigint", "quadragint", "quinquagint",
                "sexagint", "septuagint", "oktogint", "nonagint"]

        self.high_numwords = (
            ["zent"] + self.gen_high_numwords(units, tens, lows)
        )
        self.mid_numwords = [(1000, "dausend"), (100, "honnert"),
                             (90, "nonzeg"), (80, "achtzeg"), (70, "siwwenzeg"),
                             (60, "sechzeg"), (50, "fofzeg"),
                             (40, "véierzeg"), (30, "drësseg")]
        self.low_numwords = ["zwanzeg", "nonzéng", "uechtzéng", "siwwenzéng",
                             "siechzéng", "fofzéng", "véierzéng", "dräizéng",
                             "zwielef", "eelef", "zéng", "néng", "aacht",
                             "siwen", "sechs", "fënnef", "véier", "dräi",
                             "zwee", "eent", "null"]
        self.ords = {
            "eent": "éisch",
            "dräi": "drët",
            "aacht": "aach",
            "zéng": "zéng",
            "eg": "egs",
            "ert": "erts",
            "end": "ends",
            "oun": "ouns",
            "ard": "ards",
            "ion": "ions",
        }

    def merge(self, curr, next):
        """Merging numbers according to the following rules:
        https://www.languagesandnumbers.com/how-to-count-in-luxembourgish/en/ltz/#numbering-rules
        """
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum == 100 or nnum == 1000:
                return ("een" + ntext, nnum)
            elif nnum < 10 ** 6:
                return next
            ctext = "eng"

        if cnum == 2:
            if nnum == 100 or nnum == 1000:
                return ("zwee" + ntext, nnum)
            elif nnum < 10 ** 6:
                return next
            ctext = "zwou"

        if nnum > cnum:
            if nnum == 10 ** 6:
                ntext = "Millioun"

            if nnum >= 10 ** 6:
                if cnum > 1:
                    ntext += "en"
                ctext += " "

            val = cnum * nnum
        else:
            if nnum == 1:
                ntext = "een"

            if nnum < 10 < cnum < 100:
                # Eifel rule ("Eifeler Regel")
                if ctext[0] in 'n d t z h'.split():
                    ntext, ctext = ctext, ntext + "an"
                else:
                    ntext, ctext = ctext, ntext + "a"

            elif cnum >= 10 ** 6:
                ctext += " "
                # Remove `een` if word starts with `eenhonnert` or `eendausend`
                if ntext.startswith("eenhonnert") or ntext.startswith("eendausend"):
                    ntext = ntext[3:]

            val = cnum + nnum

        word = ctext + ntext
        return (word, val)

    def to_cardinal(self, value):
        result = super().to_cardinal(value)

        # Remove `een` if string starts with `eenhonnert` or `eendausend`
        if result.startswith("eenhonnert") or result.startswith("eendausend"):
            result = result[3:]

        # Add `t` at the end if ending with `een`
        if result.endswith("een"):
            result += 't'

        return result

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outword = self.to_cardinal(value).lower()

        for key in self.ords:
            if outword.endswith(key):
                outword = outword[:len(outword) - len(key)] + self.ords[key]
                break

        return outword + 't'

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "."

    def to_currency(self, val, currency='EUR', cents=True, separator=' an',
                    adjective=False):
        result = super(Num2Word_LU, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # Handle exception, in Luxembourgish it is "een Euro" and not "eent Euro"
        return result.replace("eent ", "een ")

    def to_year(self, val, longval=True):
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="honnert", longval=longval)\
            .replace(' ', '')
