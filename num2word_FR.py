'''
Module: num2word_FR.py
Requires: num2word_EU.py
Version: 0.4

Author:
   Taro Ogawa (tso@users.sourceforge.org)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Data from:
    http://www.ouc.bc.ca/mola/fr/handouts/numbers.doc.
    http://www.realfrench.net/units/Interunit_63.html
    
Usage:
    from num2word_FR import to_card, to_ord, to_ordnum
    to_card(1234567890)
#    to_ord(1234567890)
#    to_ordnum(12)
'''
from num2word_EU import Num2Word_EU

#//TODO: correct orthographics
#//TODO: error messages in French
#//TODO: ords
class Num2Word_FR(Num2Word_EU):
    def setup(self):
        self.negword = "moins "
        self.pointword = "virgule"
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.errmsg_toobig = "Number is too large to convert to words."
        self.exclude_title = ["et", "virgule", "moins"]
        self.mid_numwords = [(1000, "mille"), (100, "cent"),
                             (80, "quatre-vingts"), (60, "soixante"),
                             (50, "cinquante"), (40, "quarante"),
                             (30, "trente")]
        self.low_numwords = ["vingt", "dix-neuf", "dix-huit", "dix-sept",
                             "seize", "quinze", "quatorze", "treize", "douze",
                             "onze", "dix", "neuf", "huit", "sept", "six",
                             "cinq", "quatre", "trois", "deux", "un", "ze'ro"]


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
        else:
            if (not (cnum - 80)%100 or not cnum%100) and ctext[-1] == "s":
                ctext = ctext[:-1]
            if (cnum<1000 and nnum <> 1000 and ntext[-1] <> "s"
            and not nnum%100):
                ntext += "s"

        if nnum < cnum < 100:
            if nnum % 10 == 1 and cnum <> 80:
                return (ctext + " et " + ntext, cnum + nnum)
            return (ctext + "-" + ntext, cnum + nnum)
        elif nnum > cnum:
            return (ctext + " " + ntext, cnum * nnum)
        return (ctext + " " + ntext, cnum + nnum)


    def to_ordinal(self,value):
        self.verify_ordinal(value)
        if value == 1:
            return "premier"
        word = self.to_cardinal(value)
        if word[-1] == "e":
            word = word[:-1]
        return word + "ie'me"


    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        out = str(value)
        out +=  {"1" : "er" }.get(out[-1], "me")
        return out


n2w = Num2Word_FR()
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
