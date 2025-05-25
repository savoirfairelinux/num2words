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

ZERO = 'nol'

ONES = {
    1: 'bir',
    2: 'ikki',
    3: 'uch',
    4: 'toʻrt',
    5: 'besh',
    6: 'olti',
    7: 'yetti',
    8: 'sakkiz',
    9: 'toʻqqiz',
}

TEN = 'oʻn'

TWENTIES = {
    2: 'yigirma',
    3: 'oʻttiz',
    4: 'qirq',
    5: 'ellik',
    6: 'oltmish',
    7: 'yetmish',
    8: 'sakson',
    9: 'toʻqson',
}
HUNDRED = 'bir yuz'

THOUSANDS = {
    1: 'ming',
    2: 'million',
    3: 'milliard',
    4: 'trillion',
    5: 'kvadrillion',
    6: 'kvintillion',
    7: 'sextillion',
    8: 'septillion',
    9: 'oktilion',
    10: 'nonillion',
}


class Num2Word_UZ(Num2Word_Base):
    CURRENCY_FORMS = {
        'USD': ('dollar', 'sent'),                  # AQSh (Amerika Qo‘shma Shtatlari)
        'UZS': ('soʻm', 'tiyin'),                   # Oʻzbekiston
        'RUB': ('rubl', 'kopek'),                   # Rossiya
        'EUR': ('yevro', 'sent'),                   # Yevro hududi (Yevropa Ittifoqi davlatlari)
        'GBP': ('funt', 'pens'),                    # Buyuk Britaniya
        'KZT': ('tenge', 'tiyin'),                  # Qozogʻiston
        'TJS': ('somoniy', 'diram'),                # Tojikiston
        'CNY': ('yuan', 'feni'),                    # Xitoy
        'JPY': ('yen', 'sen'),                      # Yaponiya
        'KRW': ('von', 'chon'),                     # Janubiy Koreya
        'TRY': ('lira', 'kuruş'),                   # Turkiya
        'INR': ('rupiy', 'paysa'),                  # Hindiston
        'SAR': ('riyal', 'halala'),                 # Saudiya Arabistoni
        'CHF': ('frank', 'rappen'),                 # Shveytsariya
        'AFN': ('afgʻoniy', 'pul'),                 # Afgʻoniston
        'BRL': ('real', 'sentavo'),                 # Braziliya
        'IRR': ('rial', 'dinor'),                   # Eron
        'IDR': ('rupiya', 'sen'),                   # Indoneziya
        'TMT': ('manat', 'tenge'),                  # Turkmaniston
        'KGS': ('som', 'tiyin'),                    # Qirgʻiziston
        'EGP': ('misr funti', 'piastr'),            # Misr
        'AED': ('dirham', 'fils'),                  # Birlashgan Arab Amirliklari (BAA)
        'KWD': ('quvayt dinori', 'fils'),           # Quvayt
    }

    def setup(self):
        self.negword = "minus"
        self.pointword = "butun"

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
        return self._int2word(number, currency == 'UZS')

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
                if n3 == 1:
                    words.append(HUNDRED)
                if n3 > 1:
                    words.append(ONES[n3] + ' yuz')

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
        """
        Convert number to ordinal word in Uzbek.
        For example:
          1 -> birinchi
          2 -> ikkinchi
          3 -> uchinchi
          4 -> toʻrtinchi
          10 -> oʻninchi
          21 -> yigirmanchi birinchi (note: complex ordinals may need improvements)
        """
        if not isinstance(number, int):
            raise ValueError("Ordinal conversion supports integers only")

        if number == 0:
            return ZERO  # nol is zero, ordinal form is not common

        # Get the cardinal form as list of words
        cardinal_words = self._int2word(number).split()

        # Uzbek ordinal suffixes vary depending on last digit.
        # We'll handle common base words with special forms:
        special_ordinals = {
            'bir': 'birinchi',
            'ikki': 'ikkinchi',
            'uch': 'uchinchi',
            'toʻrt': 'toʻrtinchi',
            'besh': 'beshinchi',
            'olti': 'oltinchi',
            'yetti': 'yettinchi',
            'sakkiz': 'sakkizinchi',
            'toʻqqiz': 'toʻqqizinchi',
            'oʻn': 'oʻninchi',
            'yigirma': 'yigirmanchi',
            'oʻttiz': 'oʻttizinchi',
            'qirq': 'qirqinchi',
            'ellik': 'ellikinchi',
            'oltmish': 'oltmishinchi',
            'yetmish': 'yetmishinchi',
            'sakson': 'saksoninchi',
            'toʻqson': 'toʻqsoninchi',
            'bir yuz': 'bir yuzinchi',
        }

        last_word = cardinal_words[-1]

        if last_word in special_ordinals:
            cardinal_words[-1] = special_ordinals[last_word]
        else:
            # For compound words or words not in dictionary, just add 'inchi'
            cardinal_words[-1] = last_word + 'inchi'

        return ' '.join(cardinal_words)