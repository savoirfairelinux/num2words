'''
Module: num2word_EN_old.py
Requires: num2word_EN.py
Version: 0.3

Author:
   Taro Ogawa (tso@users.sourceforge.org)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Usage:
    from num2word_EN_old import to_card, to_ord, to_ordnum
    to_card(1234567890)
    to_ord(1234567890)
    to_ordnum(12)
'''
import num2word_EN

class Num2Word_EN_old(num2word_EN.Num2Word_EN):
    def base_setup(self):
        sclass = super(num2word_EN.Num2Word_EN, self)
        self.set_high_numwords = sclass.set_high_numwords
        sclass.base_setup()
        

n2w = Num2Word_EN_old()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num

def main():
    for val in [ 1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
             180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
             8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
             -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)

    n2w.test(1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730)

if __name__ == "__main__":
    main()
