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


class Num2Word_SV(lang_EU.Num2Word_EU):
    GIGA_SUFFIX = "iljarder"
    MEGA_SUFFIX = "iljoner"

    def set_high_numwords(self, high):
        cap = 3 + 6 * len(high)

        for word, n in zip(high, range(cap, 3, -6)):
            if self.GIGA_SUFFIX:
                self.cards[10 ** n] = word + self.GIGA_SUFFIX

            if self.MEGA_SUFFIX:
                self.cards[10 ** (n - 3)] = word + self.MEGA_SUFFIX

    def setup(self):
        super(Num2Word_SV, self).setup()

        self.negword = "minus "
        self.pointword = "komma"
        self.exclude_title = ["och", "komma", "minus"]

        self.mid_numwords = [(1000, "tusen"), (100, "hundra"),
                             (90, "nittio"), (80, "\åttio"), (70, "sjuttio"),
                             (60, "sextio"), (50, "femtio"), (40, "förtio"),
                             (30, "trettio")]
        self.low_numwords = ["tjugo", "nitton", "arton", "sjutton",
                             "sexton", "femton", "fjorton", "tretton",
                             "tolv", "elva", "tio", "nio", "åtta",
                             "sju", "sex", "fem", "fyra", "tre", "två",
                             "ett", "noll"]
        self.ords = {"noll": "nollte",
                     "ett": "första",
                     "två": "andra",
                     "tre": "tredje",
                     "fyra": "fjärde",
                     "fem": "femte",
                     "sex": "sjätte",
                     "sju": "sjunde",
                     "åtta": "åttonde",
                     "nio": "nionde",
                     "tio": "tionde",
                     "elva": "elfte",
                     "tolv": "tolfte",
                     "tjugo": "tjugonde"}

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s%s" % (ltext, rtext), lnum + rnum)
        elif rnum >= 1000000 and lnum == 1:
            return ("%s %s" % ('en', rtext[:-2]), lnum + rnum)
        elif rnum >= 1000000 and lnum > 1:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s%s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-2:] == "tio":
                lastword = lastword + "onde"
            else:
                lastword += "de"
        lastwords[-1] = self.title(lastword)
        outwords[-1] = "".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, longval=True):
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="hundra", jointxt="och",
                                longval=longval)

    def to_currency(self, val, longval=True):
        return self.to_splitnum(val, hightxt="krone/r", lowtxt="öre/n",
                                jointxt="och", longval=longval, cents=True)
