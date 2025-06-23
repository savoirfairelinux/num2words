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

from __future__ import unicode_literals

from .base import Num2Word_Base
from .currency import parse_currency_parts, prefix_currency
from .utils import get_digits, splitbyx

ZERO = ('нула',)

ONES = {
    1: ('један', 'једна'),
    2: ('два', 'две'),
    3: ('три', 'три'),
    4: ('четири', 'четири'),
    5: ('пет', 'пет'),
    6: ('шест', 'шест'),
    7: ('седам', 'седам'),
    8: ('осам', 'осам'),
    9: ('девет', 'девет'),
}

TENS = {
    0: ('десет',),
    1: ('једанаест',),
    2: ('дванаест',),
    3: ('тринаест',),
    4: ('четрнаест',),
    5: ('петнаест',),
    6: ('шеснаест',),
    7: ('седамнаест',),
    8: ('осамнаест',),
    9: ('деветнаест',),
}

TWENTIES = {
    2: ('двадесет',),
    3: ('тридесет',),
    4: ('четрдесет',),
    5: ('педесет',),
    6: ('шездесет',),
    7: ('седамдесет',),
    8: ('осамдесет',),
    9: ('деведесет',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двеста',),
    3: ('триста',),
    4: ('четристо',),
    5: ('петсо',),
    6: ('шесто',),
    7: ('седамсто',),
    8: ('осамсто',),
    9: ('деветсто',),
}

SCALE = {
    0: ('', '', '', False),
    1: ('хиљада', 'хиљаде', 'хиљада', True),  # 10^3
    2: ('милион', 'милиона', 'милиона', False),  # 10^6
    3: ('билион', 'билиона', 'билиона', False),  # 10^9
    4: ('трилион', 'трилиона', 'трилиона', False),  # 10^12
    5: ('квадрилион', 'квадрилиона', 'квадрилиона', False),  # 10^15
    6: ('квинтилион', 'квинтилиона', 'квинтилиона', False),  # 10^18
    7: ('секстилион', 'секстилиона', 'секстилиона', False),  # 10^21
    8: ('септилион', 'септилиона', 'септилиона', False),  # 10^24
    9: ('октилион', 'октилиона', 'октилиона', False),  # 10^27
    10: ('нонилион', 'нонилиона', 'нонилиона', False),  # 10^30
}


class Num2Word_SR(Num2Word_Base):
    CURRENCY_FORMS = {
        'RUB': (
            ('рубља', 'рубље', 'рубљи', True),
            ('корејка', 'корејке', 'корејки', True)
        ),
        'EUR': (
            ('евро', 'евра', 'евра', False),
            ('цент', 'цента', 'центи', False)
        ),
        'RSD': (
            ('динар', 'динара', 'динара', False),
            ('пара', 'паре', 'пара', True)
        ),
    }

    def setup(self):
        self.negword = "минус"
        self.pointword = "запета"

    def to_cardinal(self, number, feminine=False):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            decimal_part = ((ZERO[0] + ' ') * leading_zero_count +
                            self._int2word(int(right), feminine))
            return u'%s %s %s' % (
                self._int2word(int(left), feminine),
                self.pointword,
                decimal_part
            )
        else:
            return self._int2word(int(n), feminine)

    def pluralize(self, number, forms):
        if number % 100 < 10 or number % 100 > 20:
            if number % 10 == 1:
                form = 0
            elif 1 < number % 10 < 5:
                form = 1
            else:
                form = 2
        else:
            form = 2
        return forms[form]

    def to_ordinal(self, number):
        raise NotImplementedError()

    def _cents_verbose(self, number, currency):
        return self._int2word(
            number,
            self.CURRENCY_FORMS[currency][1][-1]
        )

    def _int2word(self, number, feminine=False):
        if number < 0:
            return ' '.join([self.negword, self._int2word(abs(number))])

        if number == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(number), 3))
        chunk_len = len(chunks)
        for chunk in chunks:
            chunk_len -= 1
            digit_right, digit_mid, digit_left = get_digits(chunk)

            if digit_left > 0:
                words.append(HUNDREDS[digit_left][0])

            if digit_mid > 1:
                words.append(TWENTIES[digit_mid][0])

            if digit_mid == 1:
                words.append(TENS[digit_right][0])
            elif digit_right > 0:
                is_feminine = feminine or SCALE[chunk_len][-1]
                gender_idx = int(is_feminine)
                words.append(
                    ONES[digit_right][gender_idx]
                )

            if chunk_len > 0 and chunk != 0:
                words.append(self.pluralize(chunk, SCALE[chunk_len]))

        return ' '.join(words)

    def to_currency(self, val, currency='EUR', cents=True, separator=',',
                    adjective=False):
        """
        Args:
            val: Numeric value
            currency (str): Currency code
            cents (bool): Verbose cents
            separator (str): Cent separator
            adjective (bool): Prefix currency name with adjective
        Returns:
            str: Formatted string

        """
        left, right, is_negative = parse_currency_parts(val)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]

        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            cr1 = prefix_currency(
                self.CURRENCY_ADJECTIVES[currency],
                cr1
            )

        minus_str = "%s " % self.negword if is_negative else ""
        cents_str = self._cents_verbose(right, currency) \
            if cents else self._cents_terse(right, currency)

        return u'%s%s %s%s %s %s' % (
            minus_str,
            self.to_cardinal(left, feminine=cr1[-1]),
            self.pluralize(left, cr1),
            separator,
            cents_str,
            self.pluralize(right, cr2)
        )
