# -*- encoding: utf-8 -*-
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


class Num2Word_TA(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "தொண்ணூற்று ஒன்பது",
            "தொண்ணூற்று எட்டு",
            "தொண்ணூற்றி ஏழு,"
            "தொண்ணூற்று ஆறு",
            "தொண்ணுற்று ஐந்து",
            "தொண்ணூற்று நான்கு,"
            "தொண்ணுற்று மூன்று",
            "தொண்ணூற்று இரண்டு",
            "தொண்ணூறு ஒரு,"
            "தொண்ணூறு",
            "எண்பத்து ஒன்பது",
            "எண்பத்தி எட்டு",
            "எண்பத்தி ஏழு",
            "எண்பத்தி ஆறு",
            "எண்பத்தைந்து",
            "எம்பாட் நான்கு",
            "எம்பத் த்ரீ",
            "எண்பத்திரெண்டு",
            "எண்பத்தொன்று",
            "எண்பது",
            "எழுபத்து ஒன்பது",
            "எழுபத்தெட்டு",
            "எழுபத்தி ஏழு",
            "எழுபத்தாறு",
            "எழுபத்தி ஐந்து",
            "எழுபத்து நான்கு",
            "எழுபத்து மூன்று",
            "எழுபத்திரண்டு",
            "எழுபத்தி ஒன்று",
            "எழுபது",
            "அறுபத்து ஒன்பது",
            "அறுபத்தெட்டு",
            "அறுபத்தேழு",
            "அறுபத்து ஆறு",
            "அறுபத்தி ஐந்து",
            "அரவத் நான்கு",
            "அரவத் மூன்று",
            "அறுபத்திரெண்டு",
            "அறுபத்தொன்று",
            "அறுபது",
            "ஐம்பத்தி ஒன்பது",
            "ஐம்பத்து எட்டு",
            "ஐம்பது ஏழு",
            "ஐம்பத்தி ஆறு",
            "ஐம்பத்தி ஐந்து",
            "ஐந்து பதின்மூன்று",
            "ஐம்பது மூன்று",
            "ஐம்பது இரண்டு",
            "ஐம்பத்தி ஒன்று,"
            "ஐம்பது",
            "நாற்பத்தொன்பது",
            "நாற்பத்தி எட்டு",
            "நாற்பத்தி ஏழு",
            "நாற்பது ஆறு",
            "நாற்பத்தைந்து",
            "நாற்பத்தி நான்கு",
            "நாற்பத்து மூன்று",
            "நாற்பத்தி இரண்டு",
            "நாற்பத்து ஒன்று",
            "நாற்பது",
            "த்ரீத் ஒன்பது",
            "முப்பத்தெட்டு",
            "முப்பத்தி ஏழு",
            "மொவதாரு",
            "மூவத் ஐந்து",
            "மூன்று வாய் நான்கு",
            "திரைப்படம் மூன்று",
            "மூன்று முப்பத்தி இரண்டு",
            "மூவாட் ஒன்",
            "முப்பது",
            "இருபத்து ஒன்பது",
            "இருபத்தெட்டு",
            "இருபத்தி ஏழு",
            "இருபத்தி ஆறு",
            "இருபத்து ஐந்து",
            "இருபத்து நான்கு",
            "இருபத்து மூன்று",
            "இருபத்து இரண்டு",
            "இருபதாவது ஒன்று",
            "இருபது",
            "பத்தொன்பது",
            "பதினெட்டு",
            "பதினேழு",
            "பதினாறு",
            "பதினைந்து",
            "பதினான்கு",
            "பதின்மூன்று",
            "பன்னிரண்டு",
            "பதினொரு",
            "பத்து",
            "ஒன்பது",
            "எட்டு",
            "ஏழு",
            "ஆறு",
            "ஐந்து",
            "நான்கு",
            "மூன்று",
            "இரண்டு",
            "ஒன்று",
            "பூஜ்யம்",
        ]

        self.mid_numwords = [(100, "நூறு")]

        self.high_numwords = [(7, "கோடிகள்"), (5, "ஒரு லட்சம்"), (3, "ஆயிரம்")]

        self.pointword = "புள்ளி"

        self.modifiers = [

        ]

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s-%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            if ltext[-1] in self.modifiers:
                return ("%s %s" % (ltext[:-1], rtext), lnum + rnum)
            else:
                return ("%s %s" % (ltext + "", rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value))

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value)
        if outwords[-1] in self.modifiers:
            outwords = outwords[:-1]
        ordinal_num = outwords + "ம்"
        return ordinal_num
