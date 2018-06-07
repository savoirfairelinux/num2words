# -*- coding: utf-8 -*-
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

from __future__ import division, print_function, unicode_literals

from .base import Num2Word_Base

def select_text(text, reading=False, prefer=None):
    """Select the correct text from the Japanese number, reading and
    alternatives"""
    orig = text
    if reading:
        text = text[1]
    else:
        text = text[0]

    if not isinstance(text, str):
        if prefer:
            common = set(text) & set(prefer)
            if len(common) == 1:
                text = common.pop()
        else:
            text = text[0]
    return text

class Num2Word_JA(Num2Word_Base):
    CURRENCY_FORMS = {
        'JPY': (('円', '円'), ('', '')),
    }

    def set_high_numwords(self, high):
        max = 4 * len(high)
        for word, n in zip(high, range(max, 0, -4)):
            self.cards[10 ** n] = word

    def setup(self):
        self.negword = "マイナス"
        self.pointword = "点"
        self.exclude_title = ["点", "マイナス"]

        self.mid_numwords = [
            (1000, ("千", "せん")),
            (100, ("百", "ひゃく")),
        ]

        self.low_numwords = [
            ("十", "じゅう"),                 # 10 jū
            ("九", "きゅう"),                 # 9 kyū
            ("八", "はち"),                   # 8 hachi
            ("七", ("なな", "しち")),         # 7 nana, shichi
            ("六", "ろく"),                   # 6 roku
            ("五", "ご"),                     # 5 go
            ("四", ("よん", "し")),           # 4 yon, shi
            ("三", "さん"),                   # 3 san
            ("二", "に"),                     # 2 ni
            ("一", "いち"),                   # 1 ichi
            # both are alternatives, 零 doesn't map to ゼロ or vice versa
            (("零", "〇"), ("ゼロ", "れい")), # 0 ZERO, rei
        ]

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        fmt = "%s%s"
        # ignore lpair if lnum is 1 and rnum is less than 10000
        if lnum == 1 and rnum < 10000:
            return rpair
        # rnum is added to lnum
        elif lnum > rnum:
            return (fmt % (ltext, rtext), lnum + rnum)
        # rnum is multiplied by lnum
        elif lnum < rnum:
            # these hundreds are pronounced differently
            if lpair == ("さん", 3) and rpair == ("ひゃく", 100):
                rtext = "びゃく"
            elif lpair == ("ろく", 6) and rpair == ("ひゃく", 100):
                ltext = "ろっ"
                rtext = "ぴゃく"
            elif lpair == ("はち", 8) and rpair == ("ひゃく", 100):
                ltext = "はっ"
                rtext = "ぴゃく"
            # these thousands are pronounced differently
            elif lpair == ("さん", 3) and rpair == ("せん", 1000):
                rtext = "ぜん"
            elif lpair == ("さん", 8) and rpair == ("せん", 1000):
                ltext = "はっ"
            return (fmt % (ltext, rtext), lnum * rnum)

    def to_ordinal(self, value, reading=False, prefer=None):
        self.verify_ordinal(value)
        base = self.to_cardinal(value, reading=reading, prefer=prefer)
        ordinal_suffix = "ばんめ" if reading else "番目"
        return "%s%s" % (base, ordinal_suffix)

    def to_ordinal_num(self, value, reading=False):
        ordinal_suffix = "ばんめ" if reading else "番目"
        return "%s%s" % (value, ordinal_suffix)

    def to_year(self, val, suffix=None, longval=True):
        suffix = suffix or ""
        if val < 0:
            val = abs(val)
            suffix = suffix or " ennen ajanlaskun alkua"
        return self.to_cardinal(val).replace(" ", "") + suffix

    def to_currency(self, val, currency="JPY", cents=False, seperator="", adjective=False):
        raise NotImplementedError

    def base_setup(self):
        self.high_numwords = [
            ("万", "まん"),   # 10**4 man
            ("億", "おく"),   # 10**8 oku
            ("兆", "ちょう"), # 10**12 chō
            ("京", "けい"),   # 10**16 kei
            ("垓", "がい"),   # 10**20 gai
            ("秭", "し"),     # 10**24 shi
            ("穣", "じょう"), # 10**28 jō
            ("溝", "こう"),   # 10**32 kō
            ("澗", "かん"),   # 10**36 kan
            ("正", "せい"),   # 10**40 sei
            ("載", "さい"),   # 10**44 sai
            ("極", "ごく"),   # 10**48 goku
        ]
        self.high_numwords.reverse()

    def splitnum(self, value, reading, prefer):
        for elem in self.cards:
            if elem > value:
                continue

            out = []
            if value == 0:
                div, mod = 1, 0
            else:
                div, mod = divmod(value, elem)

            if div == 1:
                out.append((select_text(self.cards[1], reading, prefer), 1))
            else:
                if div == value:  # The system tallies, eg Roman Numerals
                    return [(div * select_text(self.cards[elem], reading, prefer),
                             div*elem)]
                out.append(self.splitnum(div, reading, prefer))

            out.append((select_text(self.cards[elem], reading, prefer), elem))

            if mod:
                out.append(self.splitnum(mod, reading, prefer))

            return out

    def to_cardinal(self, value, reading=False, prefer=None):
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        self.verify_num(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = self.negword

        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))

        val = self.splitnum(value, reading, prefer)
        words, _ = self.clean(val)
        return self.title(out + words)

    def to_cardinal_float(self, value):
        return super(Num2Word_JA, self).to_cardinal_float(value).replace(" ", "")
