# -*- coding: utf-8 -*-
# Copyright (c) 2024, Karwan Khalid.  All Rights Reserved.

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

from decimal import Decimal
from math import floor
from typing import Union

class Num2Word_CKB(object):

    SORANI_ONES = [
        "", "یه‌ک", "دوو", "سێ", "چوار", "پێنج", "شەش", "حەوت", "هەشت",
        "نۆ",
        "ده",
        "یانزدە", "دوازدە", "سیانزدە", "چواردە", "پانزدە",
        "شانزدە", "حەڤدە", "هەژدە", "نۆزدە",
    ]

    SORANI_TENS = [
        "",
        "ده",
        "بیست",
        "سی",
        "چل",
        "پەنجا",
        "شەست",
        "حەفتا",
        "هەشتا",
        "نەوەد",
    ]

    SORANI_HUNDREDS = [
        "",
        "سەد",
        "دوو سەد",
        "سێ سەد",
        "چوار سەد",
        "پێنج سەد",
        "شەش سەد",
        "حەفت سەد",
        "هەشت سەد",
        "نۆ سەد",
    ]

    SORANI_BIG = [
        '',
        ' هەزار',
        ' میلیۆن',
        " میلیار",
        ' تریلیۆن',
        " تریلیارد",
    ]

    SORANI_FRAC = ["", "دەیەم", "سەدەم"]
    SORANI_FRAC_BIG = ["", "هەزارم", "میلیۆنیم", "میلیاردیم"]

    SORANI_SEPERATOR = ' و '

    MAXNUM = 10 ** 36

    @staticmethod
    def float2tuple(value: Union[int, float, Decimal]) -> tuple[int, int, int]:
        if value is None:
            raise ValueError("Value cannot be None")
        pre = int(value)

        # Simple way of finding decimal places to update the precision
        precision = abs(Decimal(str(value)).as_tuple().exponent)

        post = abs(value - pre) * 10**precision
        if abs(round(post) - post) < 0.01:
            post = int(round(post))
        else:
            post = int(floor(post))
        return pre, post, precision

    @staticmethod
    def cardinal3(number: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        if number <= 19:
            return Num2Word_CKB.SORANI_ONES[number]
        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return Num2Word_CKB.SORANI_TENS[x]
            return Num2Word_CKB.SORANI_TENS[x] + Num2Word_CKB.SORANI_SEPERATOR + Num2Word_CKB.SORANI_ONES[y]
        x, y = divmod(number, 100)
        if y == 0:
            return Num2Word_CKB.SORANI_HUNDREDS[x]
        return Num2Word_CKB.SORANI_HUNDREDS[x] + Num2Word_CKB.SORANI_SEPERATOR + Num2Word_CKB.cardinal3(y)

    @staticmethod
    def cardinalPos(number: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        x = number
        res = ''
        for b in Num2Word_CKB.SORANI_BIG:
            x, y = divmod(x, 1000)
            if y == 0:
                continue
            yx = Num2Word_CKB.cardinal3(y) + b
            if b == ' هەزار' and y == 1:
                yx = 'هەزار'
            if res == '':
                res = yx
            else:
                res = yx + Num2Word_CKB.SORANI_SEPERATOR + res
        return res

    @staticmethod
    def fractional(number: int, level: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        if number == 5:
            return "نیوە"
        x = Num2Word_CKB.cardinalPos(number)
        ld3, lm3 = divmod(level, 3)
        ltext = (Num2Word_CKB.SORANI_FRAC[lm3] + " " + Num2Word_CKB.SORANI_FRAC_BIG[ld3]).strip()
        return x + " " + ltext

    @staticmethod
    def to_currency(value: Union[int, float, Decimal]) -> str:
        if value is None:
            raise ValueError("Value cannot be None")
        return Num2Word_CKB.to_cardinal(value) + " دینار"

    @staticmethod
    def to_ordinal(number: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        r = Num2Word_CKB.to_cardinal(number)
        if r[-1] == 'ه' and r[-2] == 'س':
            return r[:-1] + 'وم'
        return r + 'یەم'

    @staticmethod
    def to_year(value: Union[int, float, Decimal]) -> str:
        if value is None:
            raise ValueError("Value cannot be None")
        return 'ساڵی ' + Num2Word_CKB.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value: int) -> str:
        if value is None:
            raise ValueError("Value cannot be None")
        return str(value)+"یەم"

    @staticmethod
    def to_cardinal(number: Union[int, float, Decimal]) -> str:
        if number is None:
            raise ValueError("Value cannot be None")
        if number < 0:
            return "سالب " + Num2Word_CKB.to_cardinal(-number)
        if number == 0:
            return "سفر"
        x, y, level = Num2Word_CKB.float2tuple(number)
        if y == 0:
            return Num2Word_CKB.cardinalPos(x)
        if x == 0:
            return Num2Word_CKB.fractional(y, level)
        return Num2Word_CKB.cardinalPos(x) + Num2Word_CKB.SORANI_SEPERATOR + Num2Word_CKB.fractional(y, level)

