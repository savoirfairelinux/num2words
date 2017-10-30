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

from __future__ import print_function, unicode_literals

from .lang_FR import Num2Word_FR


class Num2Word_FR_CH(Num2Word_FR):
    def setup(self):
        Num2Word_FR.setup(self)

        self.mid_numwords = [(1000, "mille"), (100, "cent"), (90, "nonante"),
                             (80, "huitante"), (70, "septante"),
                             (60, "soixante"), (50, "cinquante"),
                             (40, "quarante"), (30, "trente")]

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next

        if cnum < 1000 and nnum != 1000 and\
                ntext[-1] != "s" and not nnum % 100:
            ntext += "s"

        if nnum < cnum < 100:
            if nnum % 10 == 1:
                return ("%s et %s" % (ctext, ntext), cnum + nnum)
            return ("%s-%s" % (ctext, ntext), cnum + nnum)
        if nnum > cnum:
            return ("%s %s" % (ctext, ntext), cnum * nnum)
        return ("%s %s" % (ctext, ntext), cnum + nnum)


n2w = Num2Word_FR_CH()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num


def main():
    for val in [1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
                180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
                8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
                -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)

    n2w.test(
        1325325436067876801768700107601001012212132143210473207540327057320950)
    print(n2w.to_currency(112121))
    print(n2w.to_year(1996))


if __name__ == "__main__":
    main()
