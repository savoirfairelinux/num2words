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
from .compat import strtype, to_s
from .currency import parse_currency_parts, prefix_currency


def select_text(text, reading=False, prefer=None):
    """Select the correct text from the Chinese, phonetic symbol (注音) or
        alternatives ('ㄧ' or '壹')"""
    
    if reading is True:
        text = text[1]
    else:
        text = text[0]

    # select the preferred one or the first one from multiple alternatives
    if not isinstance(text, strtype):
        common = set(text) & set(prefer or set())
        if len(common) == 1:
            text = common.pop()
        else:
            text = text[0]
    return text


class Num2Word_ZH_TW(Num2Word_Base):
    CURRENCY_FORMS = {
        "NTD": (("元", "ㄩㄢˊ"), ()),
    }

    MAXVAL = 10**73 

    def set_high_numwords(self, high):
        max = 4 * len(high)
        for word, n in zip(high, range(max, 0, -4)):
            self.cards[10 ** n] = word

    def setup(self):
        self.negword = ("負", "ㄈㄨˋ")
        self.pointword = ("點", "ㄉㄧㄢˇ")
        self.exclude_title = [self.negword, self.pointword]

        self.high_numwords = [
            ("萬", "ㄨㄢˋ"),    # 10**4
            ("億", "ㄧˋ"),      # 10**8
            ("兆", "ㄓㄠˋ"),    # 10**12
            ("京", "ㄐㄧㄥ"),   # 10**16
            ("垓", "ㄍㄞ"),     # 10**20
            ("秭", "ㄗˇ"),      # 10**24
            ("穣", "ㄖㄤ"),     # 10**28
            ("溝", "ㄍㄡ"),     # 10**32
            ("澗", "ㄐㄧㄢˋ"),  # 10**36
            ("正", "ㄓㄥˋ"),    # 10**40
            ("載", "ㄗㄞˇ"),    # 10**44
            ("極", "ㄐㄧˊ"),    # 10**48
            ("恆河沙", "ㄏㄥˊㄏㄜˊㄕㄚ"),     # 10**52
            ("阿僧祇", "ㄚㄙㄥㄑㄧˊ"),        # 10**56
            ("那由他", "ㄋㄚˋㄧㄡˊㄊㄚ"),     # 10**60
            ("不可思議", "ㄅㄨˋㄎㄜˇㄙㄧˋ"),  # 10**64
            ("無量", "ㄨˊㄌㄧㄤˋ"),           # 10**68
            ("不可說", "ㄅㄨˋㄎㄜˇㄕㄨㄛ")    # 10**72
        ]

        self.counters = {
            "個": "˙ㄍㄜ",
            "名": "ㄇㄧㄥˊ",
            "位": "ㄨㄟˋ"
        } 

        self.high_numwords.reverse()

        self.mid_numwords = [
            (1000, ("千", "ㄑㄧㄢ")),
            (100, ("百", "ㄅㄞˇ")),
        ]

        self.zero = ("零", "ㄌㄧㄥˊ")

        self.low_numwords = [
            (("十", "拾"), ("ㄕˊ")),      # 10
            (("九", "玖"), ("ㄐㄧㄡˇ")),  # 9
            (("八", "捌"), ("ㄅㄚ")),     # 8
            (("七", "柒"), ("ㄑㄧ")),     # 7
            (("六", "陸"), ("ㄌㄧㄡˋ")),  # 6
            (("五", "伍"), ("ㄨˇ")),      # 5
            (("四", "肆"), ("ㄙˋ")),      # 4
            (("三", "參"), ("ㄙㄢ")),     # 3
            (("二", "貳"), ("ㄦˋ")),      # 2
            (("一", "壹"), ("ㄧ")),       # 1
            self.zero,
        ]

    def merge(self, lpair, rpair, stuff_zero=False, reading=False):
        ltext, lnum = lpair
        rtext, rnum = rpair

        # ignore lpair if lnum is 1 and rnum is less than 10
        if lnum == 1 and rnum < 10:
            return rpair

        if lnum > rnum or lnum < rnum:
            # rnum is added to lnum
            if lnum > rnum:
                num = lnum + rnum
            # rnum is multiplied by lnum
            elif lnum < rnum:
                num = lnum * rnum
        
            if stuff_zero:
                zero = self.zero[1] if reading is True else self.zero[0]
                return ("%s%s%s" % (ltext, zero, rtext), num)
            else:
                return ("%s%s" % (ltext, rtext), num)

    def should_stuff_zero(self, left, right):
        # The logic of stuff zero refers to:
        # https://mathseed.ntue.edu.tw/hard/%E6%95%99%E5%AD%B8%E7%96%91%E9%9B%A3%E5%BD%99%E7%B7%A8/ch1/95Q-E08.pdf
        if len(str(left[1])) - len(str(right[1])) >= 2 \
            and len(str(right[1])) % 4 != 0:
            return True
        return False

    def clean(self, val, reading=False):
        out = val
        while len(val) != 1:
            out = []
            left, right = val[:2]
            if isinstance(left, tuple) and isinstance(right, tuple):
                if self.should_stuff_zero(left, right):
                    out.append(self.merge(left, right, stuff_zero=True,
                               reading=reading))
                else:
                    out.append(self.merge(left, right))
                if val[2:]:
                    out.append(val[2:])
            else:
                for elem in val:
                    if isinstance(elem, list):
                        if len(elem) == 1:
                            out.append(elem[0])
                        else:
                            out.append(self.clean(elem, reading=reading))
                    else:
                        out.append(elem)
            val = out
        return out[0]

    def _ordinal_prefix(self, reading):
        if reading is True:
            return "ㄉㄧˋ"
        else:
            return "第"

    def _ordinal_suffix(self, reading, counter):
        if reading is True:
            counter = self.counters.get(counter, "")
            if not counter:
                raise NotImplementedError(
                    "Reading not implemented for %s" % counter)
        return counter

    def to_ordinal(self, value, reading=False, prefer=None, counter="個"):
        self.verify_ordinal(value)
        base = self.to_cardinal(value, reading=reading, prefer=prefer)
        return "%s%s%s" % (
            self._ordinal_prefix(reading),
            base,
            self._ordinal_suffix(reading, counter)
        )

    def to_ordinal_num(self, value, reading=False, counter="個"):
        return "%s%s%s" % (
            self._ordinal_prefix(reading),
            value,
            self._ordinal_suffix(reading, counter)
        )

    def to_year(self, val, suffix=None, longval=True, reading=False,
                prefer=None, era=True):
        year = val
        if isinstance(year, float):
            raise NotImplementedError(
                "The value of year must be integer: %s" % year)

        # Gregorian calendar
        prefix = "ㄒㄧㄩㄢˊ" if reading is True else "西元"
        if year < 0:
            year = abs(year)
            prefix = "%s%s" % (prefix, "ㄑㄧㄢˊ" if reading is True else "前")

        if reading == "arabic":
            return "%s%s%s" % (prefix, year, "年")

        year_words = self.to_cardinal(year, reading=reading, prefer=prefer)
        suffix = "ㄋㄧㄢˊ" if reading is True else "年"
        return "%s%s%s" % (prefix, year_words, suffix)

    def to_currency(self, val, currency="NTD", cents=False, separator="",
                    adjective=False, reading=False, prefer=None):
        left, right, is_negative = parse_currency_parts(
            val, is_int_with_cents=cents)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]
            if (cents or abs(val) != left) and not cr2:
                raise ValueError('Decimals not supported for "%s"' % currency)
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            cr1 = prefix_currency(self.CURRENCY_ADJECTIVES[currency], cr1)

        minus_str = self.negword if is_negative else ("", "")
        minus_str = minus_str[1] if reading is True else minus_str[0]

        return "%s%s%s%s%s" % (
            minus_str,
            self.to_cardinal(left, reading=reading, prefer=prefer),
            cr1[1] if reading is True else cr1[0],
            self.to_cardinal(right, reading=reading, prefer=prefer)
            if cr2 else "",
            (cr2[1] if reading is True else cr2[0]) if cr2 else "",
        )

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
                    return [(
                        div * select_text(self.cards[elem], reading, prefer),
                        div * elem)]
                out.append(self.splitnum(div, reading, prefer))

            out.append((select_text(self.cards[elem], reading, prefer), elem))

            if mod:
                out.append(self.splitnum(mod, reading, prefer))

            return out

    def to_cardinal(self, value, reading=False, prefer=None):
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value, reading=reading,
                                          prefer=prefer)

        out = ""
        if value < 0:
            value = abs(value)
            out = self.negword[1] if reading is True else self.negword[0]

        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))

        val = self.splitnum(value, reading, prefer)
        words, _ = self.clean(val, reading=reading)
        # remove 'one' if word starts with ten and prefer is None
        if len(words) >= 2 and words[:2] in ["一十", "ㄧㄕ"]:
            words = words[1:]
        return self.title(out + words)

    def to_cardinal_float(self, value, reading=False, prefer=None):
        try:
            float(value) == value
        except (ValueError, TypeError, AssertionError):
            raise TypeError(self.errmsg_nonnum % value)

        pre, post = self.float2tuple(float(value))

        post = str(post)
        post = "0" * (self.precision - len(post)) + post

        out = [self.to_cardinal(pre, reading=reading, prefer=prefer)]
        if self.precision:
            out.append(self.title(self.pointword[1 if reading is True else 0]))

        for i in range(self.precision):
            curr = int(post[i])
            out.append(to_s(
                self.to_cardinal(curr, reading=reading, prefer=prefer)))

        minus_str = "" 
        if value < 0:
            minus_str = self.negword[1] if reading is True else self.negword[0]
        return "%s%s" % (minus_str, "".join(out))
