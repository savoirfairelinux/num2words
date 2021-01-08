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
from num2words.base import Num2Word_Base
from num2words.currency import parse_currency_parts, prefix_currency
from num2words.utils import splitbyx, get_digits

MINUS_PREFIX_WORD = "минус "
FLOAT_INFIX_WORD = ' цяло '
CONJUNCTION = 'и'

ZERO = 'нула'

ONES = {
    1: ('едно', 'един', 'една', True),
    2: ('две', 'два', 'две', True),
    3: ('три', 'три', 'три', False),
    4: ('четири', 'четири', 'четири', False),
    5: ('пет', 'пет', 'пет', False),
    6: ('шест', 'шест', 'шест', False),
    7: ('седем', 'седем', 'седем', False),
    8: ('осем', 'осем', 'осем', False),
    9: ('девет', 'девет', 'девет', False),
}

TENS = {
    0: ('десет',),
    1: ('единадесет',),
    2: ('дванадесет',),
    3: ('тринадесет',),
    4: ('четиринадесет',),
    5: ('петнадесет',),
    6: ('шестнадесет',),
    7: ('седемнадесет',),
    8: ('осемнадесет',),
    9: ('деветнадесет',),
}

TWENTIES = {
    2: ('двадесет',),
    3: ('тридесет',),
    4: ('четиридесет',),
    5: ('петдесет',),
    6: ('шейсет',),
    7: ('седемдесет',),
    8: ('осемдесет',),
    9: ('деветдесет',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двеста',),
    3: ('триста',),
    4: ('четиристотин',),
    5: ('петстотин',),
    6: ('шестстотин',),
    7: ('седемстотин',),
    8: ('осемстотин',),
    9: ('деветстотин',),
}

SCALE = {
    0: ('', '', '', False),
    1: ('хиляда', 'хиляди', 'хиляди', True),  # 10^3
    2: ('милион', 'милиона', 'милиони', False),  # 10^6
    3: ('милиард', 'милиарда', 'милиарди', False),  # 10^9
    4: ('трилион', 'трилиона', 'трилиони', False),  # 10^12
    5: ('квадрилион', 'квадрилиона', 'квадрилиони', False),  # 10^15
    6: ('квинтилион', 'квинтилиона', 'квинтилиони', False),  # 10^18
    7: ('секстилион', 'секстилиона', 'секстилиони', False),  # 10^21
    8: ('септилион', 'септилиона', 'септилиони', False),  # 10^24
    9: ('октилион', 'октилиона', 'октилиони', False),  # 10^27
    11: ('нонилион', 'нонилиона', 'нонилиони', False),  # 10^30
    12: ('децилион', 'децилиона', 'децилиони', False),  # 10^33
    13: ('ундецилион', 'ундецилиона', 'ундецилиони', False),  # 10^36
    14: ('дуодецилион', 'дуодецилиона', 'дуодецилиони', False),  # 10^39
    15: ('тридецилион', 'тридецилиона', 'тридецилиони', False),  # 10^42
    16: ('кваддецилион', 'кваддецилиона', 'кваддецилиони', False),  # 10^45
    17: ('квиндецилион', 'квиндецилиона', 'квиндецилиони', False),  # 10^48
    18: ('сексдецилион', 'сексдецилиона', 'сексдецилиони', False),  # 10^51
    19: ('септендецилион', 'септендецилиона', 'септендецилиони', False),  # 10^54
    20: ('октодецилион', 'октодецилиона', 'октодецилиони', False),  # 10^57
    21: ('новемдецилион', 'новемдецилиона', 'новемдецилиони', False),  # 10^60
    22: ('вигинтилион', 'вигинтилиона', 'вигинтилиони', False),  # 10^63
}

CURRENCY_FORMS = {
    'BGN': (
        ('лев', 'лева', 'лева', False),
        ('стотинка', 'стотинки', 'стотинки', False)
    ),
    'EUR': (
        ('евро', 'евро', 'евро', False),
        ('цент', 'цента', 'цента', False)
    ),
    'USD': (
        ('долар', 'долара', 'долара', False),
        ('цент', 'цента', 'цента', False)
    )
}

ORDINAL_YEARS = {
    'едно': 'първа',
    'един': 'първа',
    'една': 'първа',
    'две': 'втора',
    'три': 'трета',
    'четири': 'четвърта',
    'пет': 'пета',
    'шест': 'шеста',
    'седем': 'седма',
    'осем': 'осма',
    'девет': 'девета',
}

ORDINAL_ENDING = {
    0: ('ти', 'та'),
    1: ('ви', 'ва'),
    2: ('ри', 'ра'),
    3: ('ти', 'та'),
    4: ('ти', 'та'),
    5: ('ти', 'та'),
    6: ('ти', 'та'),
    7: ('ми', 'ма'),
    8: ('ми', 'ма'),
    9: ('ти', 'та'),
}

ORDINAL = {
    'едно': 'първи',
    'един': 'първи',
    'една': 'първи',
    'две': 'втори',
    'три': 'трети',
    'четири': 'четвърти',
    'пет': 'пети',
    'шест': 'шести',
    'седем': 'седми',
    'осем': 'осми',
    'девет': 'девети',
    'десет': 'десети',
}


class Num2Word_BG(Num2Word_Base):

    negword = 'минус'

    def __init__(self):
        self.is_currency = False

    def set_high_numwords(self, *args):
        pass

    def merge(self, curr, next):
        pass

    def pluralize(self, number, forms):
        is_feminine = forms[-1]

        if number == 1:
            return forms[0]

        if is_feminine:
            form = 2
        else:
            if number % 10 == 1 and not self.is_currency:
                form = 0
            else:
                form = 1

        return forms[form]

    def setup(self):
        pass

    def _int2word(self, number, feminine=False):
        if number < 0:
            return ' '.join([MINUS_PREFIX_WORD, self._int2word(abs(number))])

        if number == 0:
            return ZERO

        words = []
        self.chunks = list(splitbyx(str(number), 3))
        chunk_len = len(self.chunks)

        for chunk in self.chunks:
            chunk_len -= 1
            digit_right, digit_mid, digit_left = get_digits(chunk)

            if digit_left > 0:
                # the True is missing condition
                if len(words) and True and digit_right == 0 and digit_mid == 0:
                    words.append(CONJUNCTION)

                words.append(HUNDREDS[digit_left][0])

            if digit_mid > 1:
                if len(words) and digit_right == 0:
                    words.append(CONJUNCTION)

                words.append(TWENTIES[digit_mid][0])

            if digit_mid == 1:
                if len(words) and digit_right == 0:
                    pass
                    words.append(CONJUNCTION)

                words.append(TENS[digit_right][0])
            elif digit_right > 0:
                if len(words):
                    words.append(CONJUNCTION)

                # digit gender depends from scale
                gender_type = 0

                is_feminine = feminine or SCALE[chunk_len][-1]

                if is_feminine:
                    gender_type = 2
                elif (len(self.chunks) > 2 and chunk_len > 1) or self.is_currency:
                    gender_type = 1

                if chunk_len == 1 and len(self.chunks) == 2:
                    if digit_mid == 0 and digit_left == 0 and digit_right == 1:
                        pass
                    else:
                        words.append(
                            ONES[digit_right][gender_type]
                        )
                else:
                    words.append(
                        ONES[digit_right][gender_type]
                    )

            if chunk_len > 0 and chunk != 0:
                words.append(self.pluralize(chunk, SCALE[chunk_len]))

        return ' '.join(words)

    def to_cardinal(self, number, feminine=False):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            return u'%s %s %s' % (
                self._int2word(int(left), feminine),
                self.pointword,
                self._int2word(int(right), feminine)
            )
        else:
            return self._int2word(int(n), feminine)

    def to_currency(self, val, currency='BGN', cents=True, separator=' и',
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
            cr1, cr2 = CURRENCY_FORMS[currency]

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
        cents_str = self.to_cardinal(right, True) \
            if cents else self._cents_terse(right, currency)

        self.is_currency = True

        return u'%s%s %s%s %s %s' % (
            minus_str,
            self.to_cardinal(left, feminine=False),
            self.pluralize(left, cr1),
            separator,
            cents_str if cents else right,
            self.pluralize(right, cr2)
        )

    def to_year(self, number, **kwargs):
        self.verify_ordinal(number)
        outwords = self._int2word(number, False).split(" ")
        lastword = outwords[-1].lower()

        try:
            lastword = ORDINAL_YEARS[lastword]
        except KeyError:
            lastword = lastword + "а"

        outwords[-1] = lastword

        return " ".join(outwords)

    def to_ordinal(self, number, feminine=False):
        self.verify_ordinal(number)
        outwords = self.to_cardinal(number).split(" ")
        lastword = outwords[-1].lower()

        try:
            lastword = ORDINAL[lastword]
        except KeyError:
            if "десет" in lastword:
                lastword = lastword + "и"

        outwords[-1] = lastword

        return " ".join(outwords)

    def to_ordinal_num(self, number, feminine=False):
        gender_idx = int(feminine)
        last_digit = number % 10
        return str(number) + '-' + ORDINAL_ENDING[last_digit][gender_idx]
