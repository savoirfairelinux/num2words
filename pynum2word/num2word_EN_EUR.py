'''
Module: num2word_EN_EUR.py
Requires: num2word_EN.py
Version: 1.0

Author:
   Taro Ogawa (tso@users.sourceforge.org)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Data from:
    http://www.uni-bonn.de/~manfear/large.php
    
Usage:
    from num2word_EN import n2w, to_card, to_ord, to_ordnum
    to_card(1234567890)
    n2w.is_title = True
    to_card(1234567890)
    to_ord(1234567890)
    to_ordnum(1234567890)
    to_year(1976)
    to_currency(euros*100 + cents)
    to_currency((euros,cents))
    

'''

from num2word_EN import Num2Word_EN

    
class Num2Word_EN_EUR(Num2Word_EN):
    def to_currency(self, val, longval=True, cents=True, jointxt="and"):
        return self.to_splitnum(val, hightxt="euro/s", lowtxt="cents",
                                jointxt=jointxt, longval=longval, cents = cents)


n2w = Num2Word_EN_EUR()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num
to_year = n2w.to_year
to_currency = n2w.to_currency

def main():
    for val in [ 1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
             180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
             8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
             -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)
    n2w.test(1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730)
    for val in [1,120,1000,1120,1800, 1976,2000,2010,2099,2171]:
        print val, "is", n2w.to_currency(val)
        print val, "is", n2w.to_year(val)
    

if __name__ == "__main__":
    main()
