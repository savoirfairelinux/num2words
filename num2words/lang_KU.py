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

class Num2Word_KU(object):

    ONES = [
        "", "Yek", "du", "sê", "çar", "pênc", "şeş", "heft", "heşt",
        "neh", "deh", "yanzdeh", "dwanzdeh", "sêzdeh", "çardeh", "panzdeh",
        "şanzdeh", "hivdeh", "hijdeh", "nozdeh",
    ]

    TENS = [
        "", "deh", "bîst", "sî", "çil", "pêncî", "şêst", "heftê", "heştê",
        "nod",
    ]

    HUNDREDS = [
        "", "sed", "du sed", "sê sed", "çar sed", "pênc sed", "şeş sed",
        "heft sed", "heşt sed", "neh sed",
    ]

    BIG = [
        '', ' hezar', ' milyon', " milyar", ' trilyion', " trlitar",
    ]

    FRAC = ["", "dehem", "sedhem"]
    FRAC_BIG = ["", "hezarem", "milyonem", "milyarem"]

    SEPARATOR = ' û '

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
            return Num2Word_KU.ONES[number]
        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return Num2Word_KU.TENS[x]
            return Num2Word_KU.TENS[x] + Num2Word_KU.SEPARATOR + Num2Word_KU.ONES[y]
        x, y = divmod(number, 100)
        if y == 0:
            return Num2Word_KU.HUNDREDS[x]
        return Num2Word_KU.HUNDREDS[x] + Num2Word_KU.SEPARATOR + Num2Word_KU.cardinal3(y)

    @staticmethod
    def cardinal_pos(number: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        x = number
        res = ''
        for b in Num2Word_KU.BIG:
            x, y = divmod(x, 1000)
            if y == 0:
                continue
            yx = Num2Word_KU.cardinal3(y) + b
            if b == ' hezar' and y == 1:
                yx = 'hezar'
            if res == '':
                res = yx
            else:
                res = yx + Num2Word_KU.SEPARATOR + res
        return res

    @staticmethod
    def fractional(number: int, level: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        x = Num2Word_KU.cardinal_pos(number)
        ld3, lm3 = divmod(level, 3)
        ltext = (Num2Word_KU.FRAC[lm3] + " " + Num2Word_KU.FRAC_BIG[ld3]).strip()
        return x + " " + ltext

    @staticmethod
    def to_currency(value: Union[int, float, Decimal]) -> str:
        if value is None:
            raise ValueError("Value cannot be None")
        return Num2Word_KU.to_cardinal(value) + " lira"

    @staticmethod
    def to_ordinal(number: int) -> str:
        if number < 0:
            raise ValueError("Number cannot be negative")
        r = Num2Word_KU.to_cardinal(number)
        if r[-1] == 'e' and r[-2] == 's':
            return r[:-1] + 'wm'
        return r + 'yem'

    @staticmethod
    def to_year(value: Union[int, float, Decimal]) -> str:
        if value is None:
            raise ValueError("Value cannot be None")
        return 'sala ' + Num2Word_KU.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value: int) -> str:
        if value is None:
            raise ValueError("Value cannot be None")
        return str(value)+"yem"
    def _int2word(number):
        if number is None:
            raise ValueError("Value cannot be None")
        if number < 0:
            return "negatîf " + Num2Word_KU.to_cardinal(-number)
        if number == 0:
            return "sifir"
        x, y, level = Num2Word_KU.float2tuple(number)
        if y == 0:
            return Num2Word_KU.cardinal_pos(x)
        if x == 0:
            return Num2Word_KU.fractional(y, level)
        return Num2Word_KU.cardinal_pos(x) + Num2Word_KU.SEPARATOR + Num2Word_KU.fractional(y, level)
    
    @staticmethod
    def to_cardinal(number):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            decimal_part = (("sifir" + ' ') * leading_zero_count +
                            Num2Word_KU._int2word(int(right)))
            return '%s%s %s' % (
                Num2Word_KU._int2word(int(left)),
                " point",
                decimal_part
            )
        else:
            return "%s" % ( Num2Word_KU._int2word(int(n)))
        
    

