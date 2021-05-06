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


class Num2Word_AM(lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        high = ["տրիլիոն", "միլլիարդ", "միլիոն"]
        for word, n in zip(high, range(12, 3, -3)):
            self.cards[10 ** n] = word

    def setup(self):
        super(Num2Word_AM, self).setup()
        self.negword = "մինուս "
        self.pointword = "ամբողջ"
        self.exclude_title = ["և", "ամբողջ", "մինուս"]
        self.mid_numwords = [(1000, "հազար"), (100, "հարյուր"),
                             (90, "իննսուն"), (80, "ութսուն"),
                             (70, "յոթանասուն"), (60, "վաթսուն"),
                             (50, "հիսուն"), (40, "քառասուն"),
                             (30, "երեսուն")]
        self.low_numwords = ["քսան", "տասնինը", "տասնութ", "տասնյոթ",
                             "տասնվեց", "տասնհինգ", "տասնչորս", "տասներեք",
                             "տասներկու", "տասնմեկ", "տասը", "ինը", "ութ",
                             "յոթ", "վեց", "հինգ", "չորս", "երեք", "երկու",
                             "մեկ", "զրո"]
        self.ords = {"մեկ": "առաջին",
                     "եկու": "երկրորդ",
                     "երեք": "երրորդ",
                     "չորս": "չորրորդ",
                     "հինգ": "հինգերորդ",
                     "վեց": "վեցերորդ",
                     "յոթ": "յոթերորդ",
                     "ութ": "ութերորդ",
                     "ինը": "իններորդ",
                     "տաս": "տասներորդ",
                     "տասնմեկ": "տասնմեկերորդ",
                     "տասներկու": "տասներկուերորդ"}

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "":
                lastword = lastword[:-1] + ""
            lastword += "երորդ"
        lastwords[-1] = self.title(lastword)
        outwords[-1] = "".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = 'Ք․Ա․' if not suffix else suffix
        high, low = (val // 100, val % 100)
        # If year is 00XX, X00X, or beyond 9999, go cardinal.
        if (high == 0
                or (high % 10 == 0 and low < 10)
                or high >= 100):
            valtext = self.to_cardinal(val)
        else:
            hightext = self.to_cardinal(high)
            if low == 0:
                lowtext = "հարյուր"
            elif low < 10:
                lowtext = "oh-%s" % self.to_cardinal(low)
            else:
                lowtext = self.to_cardinal(low)
            valtext = "%s %s" % (hightext, lowtext)
        return (valtext if not suffix
                else "%s %s" % (valtext, suffix))
