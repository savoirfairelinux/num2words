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

from __future__ import unicode_literals

from .base import Num2Word_Base


class Num2Word_HI(Num2Word_Base):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10 ** n] = word

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s-%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def setup(self):
        self.low_numwords = ["ninyanwe", "atthanve", "satanwe", "chhiyanwe",
                                "pachaanve", "chauraanve", "tiranve", "banwe",
                                "ikyanwe", "nabbe", "navasi", "atthasi",
                                "sataasi", "chhiyaasi", "pachaasi", "chauraasi",
                                "tirasi", "bayasi", "ikyasi",
                                "assi", "unnasi", "athhatar", "satahatar",
                                "chhihatar", "pachhatar", "chauhatar", "tihatar",
                                "bahatar", "ikhatar", "sattar", "unahatar",
                                "adsath", "sadsath", "chhiyasath", "painsath",
                                "chaunsath", "tirasath", "basath", "iksath",
                                "shath", "unsath", "athavan", "sathawan",
                                "chappan", "pachpan", "chauvan", "tirapan",
                                "baawan", "ikyavan", "pachaas", "unchaas",
                                "adtalis", "santalis", "chiyalis",
                                "paintalis", "chavalis", "taitalis", "bayalis",
                                "iktalis", "chalis", "untalis", "adtis",
                                "santis", "chhatis", "paytis", "chauntis",
                                "taintis", "battis", "ektis", "tees",
                                "untiis", "atthis", "sattaees", "chhabbees",
                                "pachchis", "choubees", "teis", "baees",
                                "ikkis", "bees", "unniis", "atharah",
                                "satraa", "solah", "pandrah", "chaudaa",
                                "teraa", "baarah", "gyaarah", "das",
                                "nau", "aath", "saat", "chah", "paanch",
                                "chaar", "teen", "do", "ek", "shunya"]
        self.mid_numwords = [(100, "so")]
        self.high_numwords = [(7, "crore"),
                              (5, "lakh"),
                              (3, "hazar")]
        self.pointword = 'dashamalav'
