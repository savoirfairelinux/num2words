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

import string

from num2words.base import Num2Word_Base


class Num2Word_GU(Num2Word_Base):
    """
    Gujarati (GU) Num2Word class
    """

    _irregular_ordinals = {
        1: "પ્રથમ",
        2: "બિજુ",
        3: "ત્રિજુ",
        4: "ચોથું",
        6: "છઠ્ઠું",
    }
    _irregular_ordinals_nums = {
        1: "૧લી",
        2: "૨જુ",
        3: "૩જુ",
        4: "૪થુ",
        6: "૬ઠુ",
    }
    _gujarati_digits = "૦૧૨૩૪૫૬૭૮૯"  # 0-9
    _digits_to_gujarati_digits = dict(zip(string.digits, _gujarati_digits))
    _regular_ordinal_suffix = "મું"

    def setup(self):
        # Note: alternative forms are informal
        self.low_numwords = [
            "નવ્વાણું",
            "અઠ્ઠાણું",
            "સત્તાણું",
            "છન્નું",
            "પંચાણું",
            "ચોરાણું",
            "ત્રાણું",
            "બાણું",
            "એકાણું",
            "નેવું",
            "નેવ્યાસી",
            "ઈઠ્યાસી",
            "સિત્યાસી",
            "છ્યાસી",
            "પંચાસી",
            "ચોર્યાસી",
            "ત્યાસી",
            "બ્યાસી",
            "એક્યાસી",
            "એંસી",
            "ઓગણાએંસી",
            "ઇઠ્યોતેર",
            "સિત્યોતેર",
            "છોતેર",
            "પંચોતેર",
            "ચુમોતેર",
            "તોતેર",
            "બોતેર",
            "એકોતેર",
            "સિત્તેર",
            "અગણોસિત્તેર",
            "અડસઠ",
            "સડસઠ",
            "છાસઠ",
            "પાંસઠ",
            "ચોસઠ",
            "ત્રેસઠ",
            "બાસઠ",
            "એકસઠ",
            "સાઈઠ",
            "ઓગણસાઠ",
            "અઠ્ઠાવન",
            "સત્તાવન",
            "છપ્પન",
            "પંચાવન",
            "ચોપન",
            "ત્રેપન",
            "બાવન",
            "એકાવન",
            "પચાસ",
            "ઓગણપચાસ",
            "અડતાલીસ",
            "સુડતાલીસ",
            "છેતાલીસ",
            "પિસ્તાલીસ",
            "ચુંમાલીસ",
            "ત્રેતાલીસ",
            "બેતાલીસ",
            "એકતાલીસ",
            "ચાલીસ",
            "ઓગણચાલીસ",
            "અડત્રીસ",
            "સડત્રીસ",
            "છત્રીસ",
            "પાંત્રીસ",
            "ચોત્રીસ",
            "તેત્રીસ",
            "બત્રીસ",
            "એકત્રીસ",
            "ત્રીસ",
            "ઓગણત્રીસ",
            "અઠ્ઠાવીસ",
            "સત્તાવીસ",
            "છવીસ",
            "પચ્ચીસ",
            "ચોવીસ",
            "તેવીસ",
            "બાવીસ",
            "એકવીસ",
            "વીસ",
            "ઓગણિસ",
            "અઢાર",
            "સત્તર",
            "સોળ",
            "પંદર",
            "ચૌદ",
            "તેર",
            "બાર",
            "અગિયાર",
            "દસ",
            "નવ",
            "આઠ",
            "સાત",
            "છ",
            "પાંચ",
            "ચાર",
            "ત્રણ",
            "બે",
            "એક",
            "શૂન્ય",
        ]

        self.mid_numwords = [(100, "સૌ")]
        self.high_numwords = [
            (7, "કરોડ઼"),  # alternative "करोड़"
            (5, "લખ"),
            (3, "હઝર"),  # alternative "हज़ार"
        ]
        self.pointword = "દશાંશ"
        self.negword = "માઈન્સ "

    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return rtext, rnum
        elif lnum >= 100 > rnum:
            return "%s %s" % (ltext, rtext), lnum + rnum
        elif rnum > lnum:
            return "%s %s" % (ltext, rtext), lnum * rnum
        return "%s %s" % (ltext, rtext), lnum + rnum

    def to_ordinal(self, value):
        if value in self._irregular_ordinals:
            return self._irregular_ordinals[value]

        # regular Gujarati ordinals are derived from cardinals
        # by modifying the last member of the expression.
        cardinal = self.to_cardinal(value)
        return cardinal + self._regular_ordinal_suffix

    def _convert_to_gujarati_numerals(self, value):
        return "".join(map(self._digits_to_gujarati_digits.__getitem__,
                           str(value)))

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        value = int(value)
        if value in self._irregular_ordinals_nums:
            return self._irregular_ordinals_nums[value]

        return self._convert_to_gujarati_numerals(value) \
            + self._regular_ordinal_suffix
