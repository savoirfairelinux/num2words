'''
Module: num2word_DE.py
Requires: num2word_base.py
Version: 0.4

Author:
   Taro Ogawa (BLAHhydroxideBLAH_removetheBLAHs@inorbit.com)

Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Data from:
   - http://german4u2know.tripod.com/nouns/10.html
   - http://www.uni-bonn.de/~manfear/large.php

Usage:
    from num2word_DE import to_card, to_ord, to_ordnum
    to_card(1234567890)
    to_ord(1234567890)
    to_ordnum(12)
'''
from num2word_base import Num2Word_Base

#//TODO: Use orthographics
#//TODO: Use German error messages
class Num2Word_DE(Num2Word_Base):
    def set_high_numwords(self, high):
        max = 3 + 6*len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10**n] = word + "illiarde"
            self.cards[10**(n-3)] = word + "illion"


    def setup(self):
        self.negword = "minus "
        self.pointword = "Komma"
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.errmsg_toobig = "Number is too large to convert to words."
        self.exclude_title = []

        lows = ["non", "okt", "sept", "sext", "quint", "quadr", "tr", "b", "m"]
        units = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept",
                 "okto", "novem"]
        tens = ["dez", "vigint", "trigint", "quadragint", "quinquagint",
                "sexagint", "septuagint", "oktogint", "nonagint"]
        self.high_numwords = ["zent"]+self.gen_high_numwords(units, tens, lows)
        self.mid_numwords = [(1000, "tausand"), (100, "hundert"),
                             (90, "neunzig"), (80, "achtzig"), (70, "siebzig"),
                             (60, "sechzig"), (50, "fuenfzig"), (40, "vierzig"),
                             (30, "dreissig")]
        self.low_numwords = ["zwanzig", "neunzehn", "achtzen", "siebzehn",
                             "sechzehn", "fuenfzehn", "vierzehn", "dreizehn",
                             "zwoelf", "elf", "zehn", "neun", "acht", "sieben",
                             "sechs", "fuenf", "vier", "drei", "zwei", "eins",
                             "null"]
        self.ords = { "eins"    : "ers",
                      "drei"    : "drit",
                      "acht"    : "ach",
                      "sieben"  : "sieb",
                      "ig"      : "igs" }
        self.ordflag = False


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 10**6 or self.ordflag:
                return next
            ctext = "eine"

        if nnum > cnum:
            if nnum >= 10**6:
                if cnum > 1:
                    if ntext.endswith("e") or self.ordflag:
                        ntext += "s"
                    else:
                        ntext += "es"
                ctext += " "
            val = cnum * nnum
        else:
            if nnum < 10 < cnum < 100:
                if nnum == 1:
                    ntext = "ein"
                ntext, ctext =  ctext, ntext + "und"
            elif cnum >= 10**6:
                ctext += " "
            val = cnum + nnum

        word = ctext + ntext
        return (word, val)
            

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        self.ordflag = True
        outword = self.to_cardinal(value)
        self.ordflag = False
        for key in self.ords:
            if outword.endswith(key):
                outword = outword[:len(outword) - len(key)] + self.ords[key]
                break
        return outword + "te"


    # Is this correct??
    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "te"

            
n2w = Num2Word_DE()
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

