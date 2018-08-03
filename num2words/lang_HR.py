# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2015, Blaz Bregar. All Rights Reserved.

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


#numbers to Croatian words

#usage:

#from num2words import num2words
#number = 13547650.40
#split_num = '{:.2f}'.format(number).split('.')
#int_part = int(split_num[0])
#decimal_part = int(split_num[1])
#print(num2words(int_part,lang="hr") +  " kn i " + num2words(decimal_part,lang="hr") + " lp")

#this code was originally used from Slovenian colleague, and part of the code is obsolete, but I didn't have time to remove this code. 
#I have tested the code up to millions and it could work well for larger numbers, but not tested, sorry


# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_HR(Num2Word_EU):
    def set_high_numwords(self, high):
        max = 3 + 6*len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10**n] = word + "ilijardi"
            self.cards[10**(n-3)] = word + "ilijun"

    def setup(self):
        self.negword = "minus "
        self.pointword = "kn i"
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.errmsg_toobig = "Number is too large to convert to words."
        self.exclude_title = []

        self.mid_numwords = [(1000, "tisuća"), (900, "devetsto"),
                             (800, "osamsto"), (700, "sedamsto"),
                             (600, "šesto"), (500, "petsto"),
                             (400, "četiristo"), (300, "tristo"),
                             (200, "dvijesto"), (100, "sto"),
                             (90, "devedeset"), (80, "osamdeset"),
                             (70, "sedamdeset"), (60, "šezdeset"),
                             (50, "pedeset"), (40, "četrdeset"),
                             (30, "trideset")]
        self.low_numwords = ["dvadeset", "devetnaest", "osemnaest",
                             "sedemnaest", "šesnaest", "petnaest",
                             "četrnaest", "trinaest", "dvanaest",
                             "jedanaest", "deset", "devet", "osam", "sedam",
                             "šest", "pet", "četiri", "tri", "dvije", "jedna",
                             "nula"]
        self.ords = {"jedan": "prvi",
                     "dva": "drugi",
                     "tri": "treći",
                     "četiri": "četvrti",
                     "sedam": "sedmi",
                     "osam": "osmi",
                     "sto": "stoti",
                     "tisuća": "tisućiti",
                     "milijun": "milijunti"
                     }
        self.ordflag = False

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 10**6 or self.ordflag:
                return next
            ctext = ""

        if nnum > cnum:
            if nnum >= 10**3 and nnum<10**6:
                    if ctext.endswith("jed"):
                        ctext += "na"
                        ntext = "tisuća"
                    elif ctext.endswith("dvije") or ctext.endswith("tri") or ctext.endswith("tiri"):
                        ntext = "tisuće"
                    
                    else:
                        ntext = "tisuća"
                        
            if nnum >= 10**6 and nnum<10**9:
                    if ctext.endswith("dna"):
                        ctext = ctext[:len(ctext) - 3] + "dan"
                    elif cnum == 1:
                        ntext = "milijun"
                    
                    else:
                        ntext += "a"  
            if nnum >= 10**9 and nnum<10**12:
                    if ctext.endswith("jed"):
                        ctext += "na"                        
                                  
            if nnum >= 10**6:
                if self.ordflag:
                    ntext += "t"
                
                elif cnum == 1:
                    if ntext.endswith("n"):
                        ntext += ""
                    else:
                        ntext += "a"
                
                elif cnum == 2:
                    if ntext.endswith("d"):
                        ntext += "i"
                    else:
                        ntext += "a"

                elif 2 < cnum < 5:
                    if ntext.endswith("d"):
                        ntext += "e"
                    elif not ntext.endswith("d"):
                        ntext += "i"

                else:
                    if ntext.endswith("a"):
                        ntext += ""
                    elif ntext.endswith("n"):
                        ntext += ""
                    else:
                        ntext += "---"

            if nnum >= 10**2 and self.ordflag is False:
                ctext += ""

            val = cnum * nnum
        else:
            if nnum < 10 < cnum < 100:
                #if nnum == 1:
                #    ntext += "na"
                ntext, ctext = ntext, ctext 
            elif cnum >= 10**2 and self.ordflag is False:
                if ntext.endswith("jed"):
                        ntext += "na"   
                ctext += ""
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
        return outword + "i"

    # Is this correct??
    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "."

    def to_currency(self, val, longval=True, old=False):
        if old:
            return self.to_splitnum(val, hightxt="kn/a/a",
                                    lowtxt="stotin/a/e/a",
                                    jointxt="i", longval=longval)
        return super(Num2Word_HR, self).to_currency(val, jointxt="i",
                                                    longval=longval)

    def to_year(self, val, longval=True):
        if not (val//100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="hundert", longval=longval)


n2w = Num2Word_HR()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num


def main():
    for val in [1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
                180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
                8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
                -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)

    n2w.test(13253254360678768017687001076010010122121321432104732075403270573)
    print(n2w.to_currency(112121))
    print(n2w.to_year(2000))


if __name__ == "__main__":
    main()
