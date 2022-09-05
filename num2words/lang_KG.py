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
from .utils import get_digits, splitbyx

ZERO = 'нөл'

ONES = {
    1: 'бир',
    2: 'эки',
    3: 'үч',
    4: 'төрт',
    5: 'беш',
    6: 'алты',
    7: 'жети',
    8: 'сегиз',
    9: 'тогуз',
}

TEN = 'он'

TWENTIES = {
    2: 'жыйырма',
    3: 'отуз',
    4: 'кырк',
    5: 'элүү',
    6: 'алтымыш',
    7: 'жетимиш',
    8: 'сексен',
    9: 'токсон',
}

HUNDRED = 'жүз'

THOUSANDS = {
    1: 'миң',
    2: 'миллион',
    3: 'миллиард',
    4: 'триллион',
    5: 'квадриллион',
    6: 'квинтиллион',
    7: 'секстиллион',
    8: 'септиллион',
    9: 'октиллион',
    10: 'нониллион',
}


class Num2Word_KG(Num2Word_Base):
    CURRENCY_FORMS = {
        'USD': ('доллар', 'цент'),
        'KG': ('сом', 'тыйын'),
    }

    def setup(self):
        self.negword = "минус"
        self.pointword = "үтүр"

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            return u'%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                (ZERO + ' ') * leading_zero_count + self._int2word(int(right))
            )
        else:
            return self._int2word(int(n))

    def pluralize(self, n, form):
        return form

    def _cents_verbose(self, number, currency):
        return self._int2word(number, currency == 'KG')

    def _int2word(self, n, feminine=False):
        if n < 0:
            return ' '.join([self.negword, self._int2word(abs(n))])

        if n == 0:
            return ZERO

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            if n3 > 0:
                if n3 > 1:
                    words.append(ONES[n3])
                words.append(HUNDRED)

            if n2 == 1:
                words.append(TEN)
            elif n2 > 1:
                words.append(TWENTIES[n2])

            if n1 > 0:
                words.append(ONES[n1])

            if i > 0:
                words.append(THOUSANDS[i])

        return ' '.join(words)

    def to_ordinal(self, number):
        # TODO: Implement to_ordinal
        raise NotImplementedError()
