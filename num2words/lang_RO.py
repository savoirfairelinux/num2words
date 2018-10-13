# -*- encoding: utf-8 -*-
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


class Num2Word_RO(lang_EU.Num2Word_EU):
    GIGA_SUFFIX = "iliard"
    MEGA_SUFFIX = "ilion"

    def setup(self):
        super(Num2Word_RO, self).setup()

        self.negword = "minus "
        self.pointword = "virgulă"
        self.exclude_title = ["și", "virgulă", "minus"]
        self.errmsg_toobig = "Numărul e prea mare pentru a"
                             " fi convertit în cuvinte."
        self.mid_numwords = [(1000, "mie"), (100, "sută"),
                             (90, "nouăzeci"), (80, "optzeci"),
                             (70, "șaptezeci"), (60, "șaizeci"),
                             (50, "cincizeci"), (40, "patruzeci"),
                             (30, "treizeci")]
        self.low_numwords = ["douăzeci", "nouăsprezece", "optsprezece",
                             "șaptesprezece", "șaisprezece", "cincisprezece",
                             "paisprezece", "treisprezece", "doisprezece",
                             "unsprezece", "zece", "nouă", "opt", "șapte",
                             "șase", "cinci", "patru", "trei", "doi",
                             "unu", "zero"]
        self.high_numwords = ["o", "două", "trei", "patru", "cinci",
                              "șase", "șapte", "opt", "nouă"]
        self.ords = {"unu": "primul",
                     "doi": "al doilea",
                     "three": "al treilea",
                     "cinci": "al cincilea",
                     "opt": "al optulea",
                     "nouă": "al nouălea",
                     "doisprezece": "al doisprezecelea"}

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        with_prefix = (100, 1000, 1000000, 1000000000)
        if lnum == 1:
            if rnum not in with_prefix:
                return (rtext, rnum)
            else:
                return ("o %s" % rtext, rnum)
        else:
            if 10 < lnum < 100:
                return ("%s și %s" % (ltext, rtext), lnum + rnum)
            else:
                return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 1:
            return "primul"
        else:
            value = self.to_cardinal(value)
        return "al %slea" % (value)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        if value == 1:
            return "1-ul"
        return "al %s-lea" % (value)

    def inflect(self, value, text):
        text = text.split("/")
        if value == 1:
            return text[0]
        if text[0][-1] in "aeiou":
            text[0] = text[0][:-1]
        return "".join(text)

    def to_currency(self, val, longval=True, old=False):
        cents = int(round(val*100))
        return self.to_splitnum(cents, hightxt="de leu/i", lowtxt="de ban/i",
                                divisor=100, jointxt="și", longval=longval)

    def to_year(self, val, suffix=None, longval=True):
        suffix = 'î.Hr.' if not suffix else suffix
        result = super(Num2Word_RO, self).to_year(val, suffix, longval)
        return result
