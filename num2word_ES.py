'''
Module: num2word_ES.py
Requires: num2word_EU.py
Version: 0.2

Author:
   Taro Ogawa (BLAHhydroxideBLAH@inorbit.removeBLAHtwice.com)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php

Data from:
    http://www.smartphrase.com/Spanish/sp_numbers_voc.shtml

Usage:
    from num2word_ES import to_card, to_ord, to_ordnum
    to_card(1234567890)
#    to_ord(1234567890)
#    to_ordnum(12)
'''
from num2word_EU import Num2Word_EU

#//TODO: correct orthographics
#//TODO: error messages

class Num2Word_ES(Num2Word_EU):

    #//CHECK: Is this sufficient??
    def set_high_numwords(self, high):
        max = 3 + 6*len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10**(n-3)] = word + "illo'n"


    def setup(self):
        lows = ["cuatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menos "
        self.pointword = "punto"
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.errmsg_toobig = "Number is too large to convert to words."
        self.gender_stem = "o"
        self.exclude_title = ["y", "menos", "punto"]
        self.mid_numwords = [(1000, "mil"), (100, "cien"), (90, "noventa"),
                             (80, "ochenta"), (70, "setenta"), (60, "sesenta"),
                             (50,"cincuenta"), (40,"cuarenta")]
        self.low_numwords = ["vientinueve", "vientiocho", "vientisiete",
                             "vientise'is", "vienticinco", "vienticuatro",
                             "vientitre's", "vientido's", "vientiuno",
                             "viente", "diecinueve", "dieciocho", "diecisiete",
                             "dieciseis", "quince", "catorce", "trece", "doce",
                             "once", "diez", "nueve", "ocho", "siete", "seis",
                             "cinco", "cuatro", "tres", "dos", "uno", "cero"]
        self.ords = { 1  : "primer",
                      2  : "segund",
                      3  : "tercer",
                      4  : "cuart",
                      5  : "quint",
                      6  : "sext",
                      7  : "se'ptim",
                      8  : "octav",
                      9  : "noven",
                      10 : "de'cim" }


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "un"
        elif cnum == 100:
            ctext += "t" + self.gender_stem

        if nnum < cnum:
            if cnum < 100:
                return (ctext + " y " + ntext, cnum + nnum)
            return (ctext + " " + ntext, cnum + nnum)
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-3] + "ones"

        if nnum == 100:
            if cnum == 5:
                ctext = "quinien"
                ntext = ""
            elif cnum == 7:
                ctext = "sete"
            elif cnum == 9:
                ctext = "nove"
            ntext += "t" + self.gender_stem + "s"
        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)


    def to_ordinal(self, value):
        self.verify_ordinal(value)
        try:
            return self.ords[value] + self.gender_stem
        except KeyError:
            return self.to_cardinal(value)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        # Correct for fem?
        return str(value) + "^o"
    

n2w = Num2Word_ES()
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
