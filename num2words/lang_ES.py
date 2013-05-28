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
from .lang_EU import Num2Word_EU

#//TODO: correct orthographics
#//TODO: error messages

class Num2Word_ES(Num2Word_EU):

    #//CHECK: Is this sufficient??
    def set_high_numwords(self, high):
        max = 3 + 6*len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10**(n-3)] = word + "ill\xf2n"


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
                             "vientis\xE8is", "vienticinco", "vienticuatro",
                             "vientitr\xE8s", "vientid\xF2s", "vientiuno",
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
                      7  : "s\xE8ptim",
                      8  : "octav",
                      9  : "noven",
                      10 : "d\xE8cim" }


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
                return ("%s y %s"%(ctext, ntext), cnum + nnum)
            return ("%s %s"%(ctext, ntext), cnum + nnum)
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
        return "%s\xB0"%value


    def to_currency(self, val, longval=True, old=False):
        if old:
            return self.to_splitnum(val, hightxt="peso/s", lowtxt="peseta/s",
                                    divisor=1000, jointxt="y", longval=longval)
        return super(Num2Word_ES, self).to_currency(val, jointxt="y",
                                                    longval=longval)


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
    print n2w.to_currency(1222)
    print n2w.to_currency(1222, old=True)
    print n2w.to_year(1222)

if __name__ == "__main__":
    main()
