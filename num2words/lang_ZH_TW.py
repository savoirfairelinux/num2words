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
from .lang_ZH import Num2Word_ZH

from .compat import strtype, to_s






class Num2Word_ZH_TW(Num2Word_ZH):
    # CURRENCY_FORMS = {
    #     "NTD": (("元", "ㄩㄢˊ"), ()),
    # }
    

    def to_year(self, value, capital=False, era=False, reading=False):
        if not era:
            return super().to_year(value, capital)
        
        if not value == int(value):
            raise TypeError(self.errmsg_floatyear % value)
        
        min_year = 1912
        if value < min_year:
            raise ValueError("Can't convert years less than %s to ROC era" % min_year)
        era_year = abs(int(value - min_year + 1))

        if reading == "arabic":
            era_year_words = era_year
        elif era_year == 1:
            era_year_words = "元"
        elif era_year < 101:
            era_year_words = self.to_cardinal(era_year)
        else:
            era_year_words = "".join([self.cards[int(s)] for s in str(era_year)])
        
        return "民國%s年" % (era_year_words)

