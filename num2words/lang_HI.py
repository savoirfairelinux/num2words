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
        self.low_numwords = ["निन्यानवे", "अट्ठानवे", "सतानवे", "छियानवे",
                             "पचानवे", "चौरानवे", "तिरानवे", "बानवे",
                             "इक्यानवे", "नब्बे", "नवासी", "अट्ठासी",
                             "सतासी", "छियासी", "पचासी", "चौरासी",
                             "तिरासी", "बयासी", "इक्यासी",
                             "अस्सी", "उन्नासी", "अठहतर", "सतहतर",
                             "छिहतर", "पचहतर", "चौहतर", "तिहतर",
                             "बहतर", "इकहतर", "सत्तर", "उनहतर",
                             "अड़सठ", "सड़सठ", "छियासठ", "पैंसठ",
                             "चौंसठ", "तिरसठ", "बासठ", "इकसठ",
                             "साठ", "उनसठ", "अठावन", "सतावन",
                             "छप्पन", "पचपन", "चौवन", "तिरपन",
                             "बावन", "इक्यावन", "पचास", "उनचास",
                             "अड़तालीस", "सैंतालीस", "छयालिस",
                             "पैंतालीस", "चवालीस", "तैतालीस", "बयालीस",
                             "इकतालीस", "चालीस", "उनतालीस", "अड़तीस",
                             "सैंतीस", "छतीस", "पैंतीस", "चौंतीस",
                             "तैंतीस", "बतीस", "इकतीस", "तीस",
                             "उनतीस", "अट्ठाइस", "सताइस", "छब्बीस",
                             "पच्चीस", "चौबीस", "तेइस", "बाईस",
                             "इकीस", "बीस", "उन्नीस", "अठारह",
                             "सत्रह", "सोलह", "पंद्रह", "चौदह",
                             "तेरह", "बारह", "ग्यारह", "दस",
                             "नौ", "आठ", "सात", "छह", "पांच",
                             "चार", "तीन", "दो", "एक", "शून्य"]
        self.mid_numwords = [(100, "सौ")]
        self.high_numwords = [(7, "करोड़"),
                              (5, "लाख"),
                              (3, "हज़ार")]
        self.pointword = 'दशमलव'
