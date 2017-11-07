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

ZERO = (u'нуль',)

ONES_FEMININE = {
    1: (u'одна',),
    2: (u'двi',),
    3: (u'три',),
    4: (u'чотири',),
    5: (u'п\'ять',),
    6: (u'шiсть',),
    7: (u'сiм',),
    8: (u'вiсiм',),
    9: (u'дев\'ять',),
}

ONES = {
    1: (u'один',),
    2: (u'два',),
    3: (u'три',),
    4: (u'чотири',),
    5: (u'п\'ять',),
    6: (u'шiсть',),
    7: (u'сiм',),
    8: (u'вiсiм',),
    9: (u'дев\'ять',),
}

TENS = {
    0: (u'десять',),
    1: (u'одинадцять',),
    2: (u'дванадцять',),
    3: (u'тринадцять',),
    4: (u'чотирнадцять',),
    5: (u'п\'ятнадцять',),
    6: (u'шiстнадцять',),
    7: (u'сiмнадцять',),
    8: (u'вiсiмнадцять',),
    9: (u'дев\'ятнадцять',),
}

TWENTIES = {
    2: (u'двадцять',),
    3: (u'тридцять',),
    4: (u'сорок',),
    5: (u'п\'ятдесят',),
    6: (u'шiстдесят',),
    7: (u'сiмдесят',),
    8: (u'вiсiмдесят',),
    9: (u'дев\'яносто',),
}

HUNDREDS = {
    1: (u'сто',),
    2: (u'двiстi',),
    3: (u'триста',),
    4: (u'чотириста',),
    5: (u'п\'ятсот',),
    6: (u'шiстсот',),
    7: (u'сiмсот',),
    8: (u'вiсiмсот',),
    9: (u'дев\'ятсот',),
}

THOUSANDS = {
    1: (u'тисяча', u'тисячi', u'тисяч'),  # 10^3
    2: (u'мiльйон', u'мiльйони', u'мiльйонiв'),  # 10^6
    3: (u'мiльярд', u'мiльярди', u'мiльярдiв'),  # 10^9
    4: (u'трильйон', u'трильйони', u'трильйонiв'),  # 10^12
    5: (u'квадрильйон', u'квадрильйони', u'квадрильйонiв'),  # 10^15
    6: (u'квiнтильйон', u'квiнтильйони', u'квiнтильйонiв'),  # 10^18
    7: (u'секстильйон', u'секстильйони', u'секстильйонiв'),  # 10^21
    8: (u'септильйон', u'септильйони', u'септильйонiв'),  # 10^24
    9: (u'октильйон', u'октильйони', u'октильйонiв'),  # 10^27
    10: (u'нонiльйон', u'нонiльйони', u'нонiльйонiв'),  # 10^30
}

CURRENCIES = {
    'UAH': (
        (u'гривня', u'гривнi', u'гривень'),
        (u'копiйка', u'копiйки', u'копiйок')
    ),
    'EUR': (
        (u'евро', u'евро', u'евро'), (u'цент', u'центи', u'центiв')
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
    # form = 0 if n==1 else 1 if (n % 10 > 1 and n % 10 < 5 and (n % 100 < 10
    # or n % 100 > 20)) else 2
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


def int2word(n, feminine=True):
    if n < 0:
        return ' '.join([u'мiнус', int2word(abs(n))])

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
        # elif n1 > 0 and not (i > 0 and x == 1):
        elif n1 > 0:
            ones = ONES_FEMININE if i == 1 or feminine and i == 0 else ONES
            words.append(ones[n1][0])

        if i > 0 and ((n1 + n2 + n3) > 0):
            words.append(pluralize(x, THOUSANDS[i]))

    return ' '.join(words)


def n2w(n):
    n = str(n).replace(',', '.')
    if '.' in n:
        left, right = n.split('.')
        return u'%s кома %s' % (int2word(int(left)), int2word(int(right)))
    else:
        return int2word(int(n))


def to_currency(n, currency='EUR', cents=True, seperator=','):
    left, right, is_negative = parse_currency_parts(n)
    cr1, cr2 = CURRENCIES[currency]

    minus_str = "мiнус " if is_negative else ""

    if cents:
        cents_feminine = currency == 'UAH'
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


class Num2Word_UK(object):
    def to_cardinal(self, number):
        return n2w(number)

    def to_ordinal(self, number):
        raise NotImplementedError()

    def to_currency(self, n, currency='EUR', cents=True, seperator=','):
        return to_currency(n, currency, cents, seperator)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
