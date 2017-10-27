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


class Num2Word_AR(lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10 ** n] = word + "illion"

    def setup(self):
        self.negword = "سالب "
        self.pointword = "فاصلة"
        self.errmsg_nornum = "Only numbers may be converted to words."
        self.exclude_title = ["و", "فاصلة", "سالب"]

        self.mid_numwords = [(1000000, "مليون"), (1000, "ألف"), (100, "مئة"),
                             (90, "تسعين"), (80, "ثمانين"), (70, "سبعين"),
                             (60, "ستين"), (50, "خمسين"), (40, "أربعين"),
                             (30, "ثلاثين")]
        self.low_numwords = ["عشرين", "تسعة عشر", "ثمانية عشر", "سبعة عشر",
                             "ستة عشر", "خمسة عشر", "أربعة عشر", "ثلاثة عشر",
                             "اثناعشر", "أحد عشر", "عشرة", "تسعة", "ثمانية",
                             "سبعة", "ستة", "خمسة", "أربعة", "ثلاثة", "اثنين",
                             "واحد", "صفر"]
        self.ords = {"واحد": "أول",
                     "اثنين": "ثاني",
                     "ثلاثة": "ثالث",
                     "أربعة": "رابع",
                     "خمسة": "خامس",
                     "ثمانية": "ثامن",
                     "تسعة": "تاسع",
                     "اثناعشر": "ثاني عشر"}

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s و%s" % (rtext, ltext), rnum + lnum)
        elif lnum >= 100 > rnum:
            return ("%s و %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            if lnum == 1 and rnum in [100, 1000, 1000000]:
                return ("%s" % (rtext), rnum * lnum)
            if lnum == 2 and rnum == 100:
                return ("مئتين", rnum * lnum)
            if lnum == 2 and rnum in [100, 1000]:
                return ("%sين" % (rtext), rnum * lnum)
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s، %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            lastword += ""
        lastwords[-1] = self.title(lastword)
        outwords[-1] = "،".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, longval=True):
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="مئة", jointxt="و",
                                longval=longval)

    def to_currency(self, val, longval=True):
        return self.to_splitnum(val, hightxt="ريال", lowtxt="هللة",
                                jointxt="و", longval=longval, cents=True)


n2w = Num2Word_AR()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num
to_year = n2w.to_year


def main():
    for val in [1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
                180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
                8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
                -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)
    n2w.test(13253254360678768017687001076010010122121321432104732075403270573)
    for val in [1, 120, 1000, 1120, 1800, 1976, 2000, 2010, 2099, 2171]:
        print(val, "is", n2w.to_currency(val))
        print(val, "is", n2w.to_year(val))


if __name__ == "__main__":
    main()
