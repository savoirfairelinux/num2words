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

from __future__ import division, print_function, unicode_literals

from . import lang_EU


class Num2Word_IS(lang_EU.Num2Word_EU):
    GIGA_SUFFIX = "illjarðar"
    MEGA_SUFFIX = "illjónir"

    def setup(self):
        super(Num2Word_IS, self).setup()

        self.negword = "mínus "
        self.pointword = "komma"
        self.exclude_title = ["og", "komma", "mínus"]

        self.mid_numwords = [(1000, "þúsund"), (100, "hundrað"),
                             (90, "níutíu"), (80, "áttatíu"), (70, "sjötíu"),
                             (60, "sextíu"), (50, "fimmtíu"), (40, "fjörutíu"),
                             (30, "þrjátíu")]
        self.low_numwords = ["tuttugu", "nítján", "átján", "sautján",
                             "sextán", "fimmtán", "fjórtán", "þrettán",
                             "tólf", "ellefu", "tíu", "níu", "átta",
                             "sjö", "sex", "fimm", "fjögur", "þrjú", "tvö",
                             "eitt", "núll"]
        self.ords = {"eitt": "fyrsti",
                     "tvö": "annar",
                     "þrjú": "þriðji",
                     "fjögur": "fjórði",
                     "fimm": "fimmti",
                     "sex": "sjötti",
                     "sjö": "sjöundi",
                     "átta": "áttundi",
                     "níu": "níundi",
                     "tíu": "tíundi",
                     "ellefu": "ellefti",
                     "tólf": "tólfti"}

    def pluralize(self, n, forms):
        form = 0 if (n%10 == 1 and n%100 != 11) else 1
        return forms[form]

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        elif lnum > rnum and rnum in self.cards:
            return ("%s og %s" % (ltext, rtext), lnum + rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie"
            lastword += "th"
        lastwords[-1] = self.title(lastword)
        outwords[-1] = "-".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = 'BC' if not suffix else suffix
        high, low = (val // 100, val % 100)
        # If year is 00XX, X00X, or beyond 9999, go cardinal.
        if (high == 0
                or (high % 10 == 0 and low < 10)
                or high >= 100):
            valtext = self.to_cardinal(val)
        else:
            hightext = self.to_cardinal(high)
            if low == 0:
                lowtext = "hundred"
            elif low < 10:
                lowtext = "oh-%s" % self.to_cardinal(low)
            else:
                lowtext = self.to_cardinal(low)
            valtext = "%s %s" % (hightext, lowtext)
        return (valtext if not suffix
                else "%s %s" % (valtext, suffix))
