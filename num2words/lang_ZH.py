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

    def str_to_number(self, value):
        # delete [,'] char, 
        # return:string
        if ',' in value:
            value = value.replace(',', '' )
        elif '\'' in value:
            value = value.replace('\'','')
        # verify the value if it is a number!
        try:
           value = Decimal(value)
        except Exception as e:
            raise TypeError(self.errmsg_nonnum % value)
        # Processing the beginning and end [0 .]
        return str(value)
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
    def to_cardinal(self, value, capital = False):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        try:
            assert '.' not in value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value, capital)
       
        out = ""
        if value[0] == '-':
            value = value[1:]
            out = self.negword
        val = self.splitnum(value)
        out = out + val
        if capital:
            out = self.zh_to_cap(out)
        return out

    def to_cardinal_float(self, value, capital = False):

        pre, post = self.float2tuple(value)

        out = self.to_cardinal(pre) + (self.pointword) + self.num_to_base(post)
        if capital:
            out = self.zh_to_cap(out)
        return out
    def splitnum(self, value):
        #string
        #int(value) >= 0
        out = ''
        value = value[::-1]
        val_bit = 1
        for num in value:
            i = int(num)
            x, y = divmod(val_bit, 4) 
            if y != 0:
                n = y
            elif x % 2 != 0:
                n = 4
            else:
                n = 8
            out = out + self.cards[i] + self.cards[10**n]
            val_bit = val_bit + 1
        out = out[-2::-1]
        out = self.clean(out)
        return out
    
    def num_to_base(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        out = ''
        for i in range(len(value)):
            x = int(value[i])
            out = out + self.cards[x]
        return out
    
    def float2tuple(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        if '.' in value:
            pre, post = str(value).split('.')
            return pre , post
        else:
            raise  TypeError('The value (%s) no them a float number' % value) 

    def clean(self, value):
        #clear chars in REP_map 
        out = value
        for rep_w in self.REP_map:
            while rep_w[0] in out:
                out = out.replace(rep_w[0],rep_w[1])
        if len(out) > 1 and out[-1] == '零':
            out = out [:-1]
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
        money_str = self._money_verbose(left, currency)
        # has_decimal is not implemented

        out = minus_str + money_str
        out += cr if currency == "XXX" else self.CURRENCY_FORMS["XXX"]

        cents_str = self.to_currency_float(right, capital)
        if len(cents_str) > 0:
            out += cents_str
        elif capital: # Only add "整" in capital format
            out += self.cheque_suffix

        if capital:
            out = self.zh_to_cap(out)
        else:
            out = out.replace("一十", "十")

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

    def zh_to_cap(self,value):
        #Select the capital form of a Chinese numeral
        out = value
        for cap_w in self.CAP_map:
            if cap_w[0] in out:
                out = out.replace(cap_w[0],cap_w[1])
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
    REP_map = [
        ('零千','零'),
        ('零百','零'),
        ('零十','零'),
        ('零零','零'),
        ('零萬','萬'),
        ('零億','億'),
        ('億萬','億')
    ]

