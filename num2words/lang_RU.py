# -*- encoding: utf-8 -*-
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

from .currency import parse_currency_parts

ZERO = (u'ноль',)

ONES_FEMININE = {
    1: (u'одна',),
    2: (u'две',),
    3: (u'три',),
    4: (u'четыре',),
    5: (u'пять',),
    6: (u'шесть',),
    7: (u'семь',),
    8: (u'восемь',),
    9: (u'девять',),
}

ONES = {
    1: (u'один',),
    2: (u'два',),
    3: (u'три',),
    4: (u'четыре',),
    5: (u'пять',),
    6: (u'шесть',),
    7: (u'семь',),
    8: (u'восемь',),
    9: (u'девять',),
}

TENS = {
    0: (u'десять',),
    1: (u'одиннадцать',),
    2: (u'двенадцать',),
    3: (u'тринадцать',),
    4: (u'четырнадцать',),
    5: (u'пятнадцать',),
    6: (u'шестнадцать',),
    7: (u'семнадцать',),
    8: (u'восемнадцать',),
    9: (u'девятнадцать',),
}

TWENTIES = {
    2: (u'двадцать',),
    3: (u'тридцать',),
    4: (u'сорок',),
    5: (u'пятьдесят',),
    6: (u'шестьдесят',),
    7: (u'семьдесят',),
    8: (u'восемьдесят',),
    9: (u'девяносто',),
}

HUNDREDS = {
    1: (u'сто',),
    2: (u'двести',),
    3: (u'триста',),
    4: (u'четыреста',),
    5: (u'пятьсот',),
    6: (u'шестьсот',),
    7: (u'семьсот',),
    8: (u'восемьсот',),
    9: (u'девятьсот',),
}

THOUSANDS = {
    1: (u'тысяча', u'тысячи', u'тысяч'),  # 10^3
    2: (u'миллион', u'миллиона', u'миллионов'),  # 10^6
    3: (u'миллиард', u'миллиарда', u'миллиардов'),  # 10^9
    4: (u'триллион', u'триллиона', u'триллионов'),  # 10^12
    5: (u'квадриллион', u'квадриллиона', u'квадриллионов'),  # 10^15
    6: (u'квинтиллион', u'квинтиллиона', u'квинтиллионов'),  # 10^18
    7: (u'секстиллион', u'секстиллиона', u'секстиллионов'),  # 10^21
    8: (u'септиллион', u'септиллиона', u'септиллионов'),  # 10^24
    9: (u'октиллион', u'октиллиона', u'октиллионов'),  # 10^27
    10: (u'нониллион', u'нониллиона', u'нониллионов'),  # 10^30
}

CURRENCIES = {
    'RUB': (
        (u'рубль', u'рубля', u'рублей'), (u'копейка', u'копейки', u'копеек')
    ),
    'EUR': (
        (u'евро', u'евро', u'евро'), (u'цент', u'цента', u'центов')
    ),
}


def splitby3(n):
    length = len(n)
    if length > 3:
        start = length % 3
        if start > 0:
            yield int(n[:start])
        for i in range(start, length, 3):
            yield int(n[i:i + 3])
    else:
        yield int(n)


def get_digits(n):
    return [int(x) for x in reversed(list(('%03d' % n)[-3:]))]


def pluralize(n, forms):
    if n % 100 < 10 or n % 100 > 20:
        if n % 10 == 1:
            form = 0
        elif 5 > n % 10 > 1:
            form = 1
        else:
            form = 2
    else:
        form = 2
    return forms[form]


def int2word(n, feminine=False):
    if n < 0:
        return ' '.join([u'минус', int2word(abs(n))])

    if n == 0:
        return ZERO[0]

    words = []
    chunks = list(splitby3(str(n)))
    i = len(chunks)
    for x in chunks:
        i -= 1
        n1, n2, n3 = get_digits(x)

        if n3 > 0:
            words.append(HUNDREDS[n3][0])

        if n2 > 1:
            words.append(TWENTIES[n2][0])

        if n2 == 1:
            words.append(TENS[n1][0])
        elif n1 > 0:
            ones = ONES_FEMININE if i == 1 or feminine and i == 0 else ONES
            words.append(ones[n1][0])

        if i > 0 and x != 0:
            words.append(pluralize(x, THOUSANDS[i]))

    return ' '.join(words)


def n2w(n):
    n = str(n).replace(',', '.')
    if '.' in n:
        left, right = n.split('.')
        return u'%s запятая %s' % (int2word(int(left)), int2word(int(right)))
    else:
        return int2word(int(n))


def to_currency(n, currency='EUR', cents=True, seperator=','):
    left, right, is_negative = parse_currency_parts(n)
    cr1, cr2 = CURRENCIES[currency]

    minus_str = "минус " if is_negative else ""

    if cents:
        cents_feminine = currency == 'RUB'
        cents_str = int2word(right, cents_feminine)
    else:
        cents_str = "%02d" % right

    return u'%s%s %s%s %s %s' % (
        minus_str,
        int2word(left),
        pluralize(left, cr1),
        seperator,
        cents_str,
        pluralize(right, cr2)
    )


class Num2Word_RU(object):
    def to_cardinal(self, number):
        return n2w(number)

    def to_ordinal(self, number):
        raise NotImplementedError()

    def to_currency(self, n, currency='EUR', cents=True, seperator=','):
        return to_currency(n, currency, cents, seperator)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
