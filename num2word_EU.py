'''
Module: num2word_EU.py
Requires: num2word_base.py
Version: 1.0

Author:
   Taro Ogawa (BLAHhydroxideBLAH@inorbit.removeBLAHtwice.com)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Data from:
    http://www.uni-bonn.de/~manfear/large.php
'''
from num2word_base import Num2Word_Base

class Num2Word_EU(Num2Word_Base):
    def set_high_numwords(self, high):
        max = 3 + 6*len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10**n] = word + "illiard"
            self.cards[10**(n-3)] = word + "illion"

        
    def base_setup(self):
        lows = ["non","oct","sept","sext","quint","quadr","tr","b","m"]
        units = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept",
                 "octo", "novem"]
        tens = ["dec", "vigint", "trigint", "quadragint", "quinquagint",
                "sexagint", "septuagint", "octogint", "nonagint"]
        self.high_numwords = ["cent"]+self.gen_high_numwords(units, tens, lows)
