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

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

CURRENCY_ir = {
    'RIAL': ("ريال",),
    'TOMAN': ("تومان",),
}

ONES = {
    0: ('صفر',),
    1: ('یک',),
    2: ('دو',),
    3: ('سه',),
    4: ('چهار',),
    5: ('پنج',),
    6: ('شش',),
    7: ('هفت',),
    8: ('هشت',),
    9: ('نه',),
}

TENS = {
    0: ('ده',),
    1: ('یازده',),
    2: ('دوازده',),
    3: ('سیزده',),
    4: ('چهارده',),
    5: ('پانزده',),
    6: ('شانزده',),
    7: ('هفده',),
    8: ('هجده',),
    9: ('نوزده',),
}

TWENTIES = {
    2: ('بیست',),
    3: ('سی',),
    4: ('چهل',),
    5: ('پنجاه',),
    6: ('شصت',),
    7: ('هفتاد',),
    8: ('هشتاد',),
    9: ('نود',),
}

HUNDREDS = {
    1: ('یكصد',),
    2: ('دویست',),
    3: ('سیصد',),
    4: ('چهارصد',),
    5: ('پانصد',),
    6: ('ششصد',),
    7: ('هفتصد',),
    8: ('هشتصد',),
    9: ('نهصد',),
}

THOUSANDS = {
    1: ('هزار',),  # 10^3
    2: ('میلیون', ),  # 10^6
    3: ('میلیارد', ),  # 10^9
    4: ('بیلیون', ),  # 10^12
    5: ('بیلیارد', ),  # 10^15
    6: ('تریلیون', ),  # 10^18
    7: ('تریلیارد',),  # 10^21
    8: ('کوآدریلیون', ),  # 10^24
    9: ('کادریلیارد', ),  # 10^27
    10: ('کوینتیلیون', ),  # 10^30
}

MANTISSA = {
    1: ('دهم',),  # .0
    2: ('صدم', ),  # .00
    3: ('هزارم', ),  # .000
    4: ('ده هزارم', ),  # .0000
    5: ('صدهزارم', ),  # .00000
    6: ('یک میلیونیم', ),  # .000000
    7: ('ده میلیونیم',),  # .0000000
    8: (' صد میلیونیم', ),  # .00000000
    9: ('یک میلیاردم', ),  # .000000000
}


class Num2Word_FA(Num2Word_Base):

    def __init__(self):
        self.separator = ' و '
        self.errmsg_too_big = "Too large"
        self.errmsg_too_small = "Too Small"
        self.max_num = 10 ** 33

    def to_cardinal(self, number):
        number = self._validate_number(number)
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            decimal_part = self.ـint2word(int(right))
            if len(str(right).strip("0")) > 0:
                return(u'%s%s%s %s' % (
                    self.ـint2word(int(left)),
                    self.separator,
                    decimal_part,
                    MANTISSA[len(str(right).rstrip("0"))][0]
                ))
            else:
                return (self._nt2word(int(left)))
        else:
            return (self.ـint2word(int(n)))

    def ـint2word(self, n):
        if n == 0:
            return ONES[0][0]
        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)

        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            if n3 > 0:
                words.append(HUNDREDS[n3][0])

            if n2 > 1:
                words.append(TWENTIES[n2][0])

            if n2 == 1:
                words.append(TENS[n1][0])
            elif n1 > 0 and not (i > 0 and x == 0):
                words.append(ONES[n1][0])

            if i > 0:
                words[-1] += ' '+(THOUSANDS[i][0])

        return self.separator.join(words)

    def _validate_number(self, number):
        if type(number) is int:
            if number >= self.max_num:
                raise OverflowError(self.errmsg_too_big)
            return number
        else:
            n = str(number)
            _, right = n.split('.')
            if len(right) >= 9:
                raise OverflowError(self.errmsg_too_small)
            return number

    def to_currency(self, value, currency='RIAL'):
        if type(value) is str:
            value = int(value.replace(',', ''))

        value = self._validate_number(value)

        return u'%s %s' % (str(self.ـint2word(value)), CURRENCY_ir[currency][0])


    
