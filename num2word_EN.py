'''
Module: num2word_EN.py
Requires: num2word_EU.py
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
'''
import num2word_EU

class Num2Word_EN(num2word_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        max = 3 + 3*len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10**n] = word + "illion"

    def setup(self):
        self.negword = "minus "
        self.pointword = "point"
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.exclude_title = ["and", "point", "minus"]

        self.mid_numwords = [(1000, "thousand"), (100, "hundred"),
                             (90, "ninety"), (80, "eighty"), (70, "seventy"),
                             (60, "sixty"), (50, "fifty"), (40, "forty"),
                             (30, "thirty")]
        self.low_numwords = ["twenty", "nineteen", "eighteen", "seventeen",
                             "sixteen", "fifteen", "fourteen", "thirteen",
                             "twelve", "eleven", "ten", "nine", "eight",
                             "seven", "six", "five", "four", "three", "two",
                             "one", "zero"]
        self.ords = { "one"    : "first",
                      "two"    : "second",
                      "three"  : "third",
                      "five"   : "fifth",
                      "eight"  : "eighth",
                      "nine"   : "ninth",
                      "twelve" : "twelfth" }


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1 and nnum < 100:
            return next
        elif 100 > cnum > nnum :
            return (ctext + "-" + ntext, cnum + nnum)
        elif cnum >= 100 > nnum:
            return (ctext + " and " + ntext, cnum + nnum)
        elif nnum > cnum:
            return (ctext + " " + ntext, cnum * nnum)
        return (ctext + ", " + ntext, cnum + nnum)


    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie" 
            lastword += "th"
        lastwords[-1] = self.title(lastword) 
        outwords[-1] = "-".join(lastwords)
        return " ".join(outwords)


    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        out = str(value)
        out +=  {"1" : "st",
                 "2" : "nd",
                 "3" : "rd" }.get(out[-1], "th")
        return out

n2w = Num2Word_EN()
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
