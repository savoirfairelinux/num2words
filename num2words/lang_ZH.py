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
from decimal import Decimal
from .base import Num2Word_Base

from .currency import parse_currency_parts

class Num2Word_ZH(Num2Word_Base):
    CURRENCY_FLOATS = ["角", "分"]

    CURRENCY_FORMS = {
        "XXX": "元", # Generic dollar
        "CNY": "人民幣",
        "NTD": "新台幣",
        "HKD": "港幣",
        "MOP": "澳門幣",
        "SGD": "新加坡元",
        "MYR": "馬來西亞令吉",
        "USD": "美元",
        "EUR": "歐元",
        "GBP": "英鎊",
        "JPY": "日元",
        "CHF": "瑞士法郎",
        "CAD": "加元",
        "AUD": "澳幣",
        "NZD": "紐西蘭元",
        "THB": "泰銖",
        "KRW": "韓元",
    }

    cheque_suffix = "正"
    
    def set_high_numwords(self, high):
        max = 4 * len(high)
        for word, n in zip(high, range(max, 0, -4)):
            self.cards[10 ** n] = word

    def num_to_str(self, value):
        #[int float] to string
        #return:string
        if not isinstance(value, str):
            val  = str(value)
            if isinstance(value, int):
                return val
            elif 'e' not in str(value) and len(str(value)) < 16:
                return val
            else:
                raise  TypeError('the float (%s) lens than 16,\
                dot not suppurt,use [string] to suppurt' % value)
        return value
    
    def to_cardinal(self, value, capital=False, stuff_zero=2):
        self.capital = capital
        self.stuff_zero = stuff_zero

        out = super().to_cardinal(value)
        out = self.zh_to_cap(out, capital)
        return out.replace(" ", "")

    def to_cardinal_float(self, value):
        out = super().to_cardinal_float(value)
        out = self.zh_to_cap(out, self.capital)
        return out.replace(" ", "")

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        # ignore lpair if lnum is 1 and rnum is less than 10
        if lnum == 1 and rnum < 10:
            return (rtext, rnum)
        # stuff_zero logic between discontinous numbers
        # http://www.hkame.org.hk/uploaded_files/magazine/15/271.pdf
        with_zero = ("%s%s%s" % (ltext, self.low_numwords[-1], rtext), lnum + rnum)
        no_zero = ("%s%s" % (ltext, rtext), lnum + rnum)
        if len(str(lnum)) - len(str(rnum)) > 1:
            if self.stuff_zero == 1: # 凡「零」必讀 All discontinous numbers
                return with_zero
            elif self.stuff_zero == 2: # Discontinous high numbers
                if len(str(lnum)) - len(str(rnum)) > 1 and len(str(rnum)) % 4 != 0:
                    return with_zero
                return no_zero
            elif self.stuff_zero == 3: # 凡「零」不讀 No zeros
                return no_zero
        elif rnum > lnum:
            return ("%s%s" % (ltext, rtext), lnum * rnum)
        return no_zero
    
    def num_to_base(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        out = ''
        for i in range(len(value)):
            x = int(value[i])
            out = out + self.cards[x]
        return out
    
    def verify_ordinal(self, value):
        if '.' in value:
            raise TypeError(self.errmsg_floatord % value)
        if '-' in value:
            raise TypeError(self.errmsg_negord % value)

    def to_ordinal(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        self.verify_ordinal(value)
        out = self.to_cardinal(value).replace('零', '〇')
        if len(out) >= 2 and out[0] == '一' and out[1] == '十':
            out = out[1:]
        out = '第' + out
        return out

    def to_ordinal_num(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        self.verify_ordinal(value)
        return '第' + value

    def to_year(self, value, **kwargs):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        self.verify_ordinal(value)
        return self.num_to_base(value).replace('零', '〇')+'年'

    def to_currency(self, val, currency='XXX', cents=False, separator="",
                    adjective=False, capital=False):
        """
        Args:
            val: Numeric value
            currency (str): Currency code
            # cents (bool): Verbose cents
            # separator (str): Cent separator
            # adjective (bool): Prefix currency name with adjective
            capital (bool): Select the capital form of a Chinese numeral
        Returns:
            str: Formatted string

        Handles whole numbers and decimal numbers differently
        """
        left, right, is_negative = parse_currency_parts(val, is_int_with_cents=False)

        try:
            cr = self.CURRENCY_FORMS[currency]
            # Not Applicable: ValueError('Decimals not supported for "%s"' % currency)
            # CURRENCY_FLOATS are the generic terms for demicals
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))
        
        # CURRENCY_ADJECTIVES are not implemented
        minus_str = self.negword if is_negative else ""
        money_str = self.to_cardinal(left, capital)
        # has_decimal is not implemented

        out = minus_str + money_str
        out += cr if currency == "XXX" else self.CURRENCY_FORMS["XXX"]

        cents_str = self.to_currency_float(right, capital)
        if len(cents_str) > 0:
            out += cents_str
        elif capital: # Only add "整" in capital format
            out += self.cheque_suffix

        out = self.zh_to_cap(out, capital)
        if currency != "XXX": # Currency forms are not affected by capitalization
            out = cr + out

        return  out
    
    def to_currency_float(self, value, capital):
        cents = "%02d" % value
        out = ""
        
        if int(cents) > 0:
            if not (int(cents[0]) == 0 and capital):
                out += self.cards[int(cents[0])]
            if int(cents[0]) > 0:
                out += self.CURRENCY_FLOATS[0]
            if int(cents[1]) > 0:
                out += self.cards[int(cents[1])] + self.CURRENCY_FLOATS[1]

        return out

    def zh_to_cap(self, value, capital):
        """
        Select the capital form of a Chinese numeral
        """
        out = value
        if capital:
            for cap_w in self.CAP_map:
                if cap_w[0] in out:
                    out = out.replace(cap_w[0],cap_w[1])
            return out
        elif out.startswith("一十"):
            out = out[1:]
        return out
    
    def setup(self):
        self.precision = 2
        self.negword = "負"
        self.pointword = "點"
        self.exclude_title = [self.negword, self.pointword]
        self.high_numwords = [
            "萬",       # 10 ** 4
            "億",       # 10 ** 8
            "兆",       # 10 ** 12
            "京",       # 10 ** 16
            "垓",       # 10 ** 20
            "秭",       # 10 ** 24
            "穣",       # 10 ** 28
            "溝",       # 10 ** 32
            "澗",       # 10 ** 36
            "正",       # 10 ** 40
            "載",       # 10 ** 44
            "極",       # 10 ** 48
            "恆河沙",   # 10 ** 52
            "阿僧祇",   # 10 ** 56
            "那由他",   # 10 ** 60
            "不可思議", # 10 ** 64
            "無量",     # 10 ** 68
            "不可說",   # 10 ** 72
        ]
        self.high_numwords.reverse()
        
        self.mid_numwords = [
            (1000,  '千'),
            (100,   '百'),
            (10,    '十')
            ]
        self.low_numwords = [
            "九",
            "八",
            "七",
            "六",
            "五",
            "四",
            "三",
            "二",
            "一",
            "零"
            ]
        
    CAP_map = [
        ("千", "仟"),
        ("百", "佰"),
        ("十", "拾"),
        ("九", "玖"),
        ("八", "捌"),
        ("七", "柒"),
        ("六", "陸"),
        ("五", "伍"),
        ("四", "肆"),
        ("三", "叁"),
        ("二", "貳"),
        ("一", "壹"),
        ("元", "圓"),
        ("正", "整"),
    ]
