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
u"""
>>> from textwrap import fill

>>> ' '.join([str(i) for i in splitby3('1')])
u'1'
>>> ' '.join([str(i) for i in splitby3('1123')])
u'1 123'
>>> ' '.join([str(i) for i in splitby3('1234567890')])
u'1 234 567 890'

>>> print(' '.join([n2w(i) for i in range(10)]))
нуль один два три чотири п'ять шiсть сiмь вiсiм дев'ять

>>> print(fill(' '.join([n2w(i+10) for i in range(10)])))
десять одинадцять дванадцять тринадцять чотирнадцять п'ятнадцять
шiстнадцять сiмнадцять вiсiмнадцять дев'ятнадцять

>>> print(fill(' '.join([n2w(i*10) for i in range(10)])))
нуль десять двадцять тридцять сорок п'ятдесят шiстдесят сiмдесят
вiсiмдесят дев'яносто

>>> print(n2w(100))
сто
>>> print(n2w(101))
сто один
>>> print(n2w(110))
сто десять
>>> print(n2w(115))
сто п'ятнадцять
>>> print(n2w(123))
сто двадцять три
>>> print(n2w(1000))
тисяча
>>> print(n2w(1001))
тисяча один
>>> print(n2w(2012))
двi тисячi дванадцять

>>> print(n2w(12519.85))
дванадцять тисяч п'ятсот дев'ятнадцять кома вiсiмдесят п'ять

>>> print(fill(n2w(1234567890)))
мiльярд двiстi тридцать чотири мiльйона п'ятсот шiстдесят сiмь тисяч
вiсiмсот дев'яносто

>>> print(fill(n2w(215461407892039002157189883901676)))
двiстi п'ятнадцять нонiльйонiв чотириста шiстдесят один октильйон
чотириста сiм септильйонiв вiсiмсот дев'яносто два секстильйони
тридцять дев'ять квiнтильйонiв два квадрильйони сто п'ятдесят сiм
трильйонiв сто вiсiмдесят дев'ять мiльярдiв вiсiмсот вiсiмдесят три
мiльйона дев'ятсот одна тисяча шiстсот сiмдесят шiсть

>>> print(fill(n2w(719094234693663034822824384220291)))
сiмсот дев'ятнадцять нонiльйонiв дев'яносто чотири октильйони двiстi
тридцять чотири септильйони шiстсот дев'яносто три секстильйони
шiстсот шiстдесят три квiнтильйони тридцять чотири квадрильйони
вiсiмсот двадцять два трильйони вiсiмсот двадцять чотири мiльярди
триста вiсiмдесят чотири мiльйона двiстi двадцять тисяч двiстi
дев'яносто один

>>> print(to_currency(1.0, 'EUR'))
один євро, нуль центiв

>>> print(to_currency(1.0, 'UAH'))
одна гривня, нуль копiйок

>>> print(to_currency(1234.56, 'EUR'))
тисяча двiстi тридцять чотири євро, п'ятдесят шiсть центiв

>>> print(to_currency(1234.56, 'UAH'))
тисяча двiстi тридцять чотири гривнi, п'ятдесят шiсть копiйок

>>> print(to_currency(10111, 'EUR', seperator=u' та'))
сто один євро та одинадцять центiв

>>> print(to_currency(10121, 'UAH', seperator=u' та'))
сто одна гривня та двадцять одна копiйка

>>> print(to_currency(10122, 'UAH', seperator=u' та'))
сто одна гривня та двадцять одна копiйка

>>> print(to_currency(10121, 'EUR', seperator=u' та'))
сто один євро та двадцять один цент

>>> print(to_currency(-1251985, cents = False))
мiнус дванадцять тисяч п'ятьсот дев'ятнадцять євро, 85 центiв
"""
from __future__ import unicode_literals

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
        (u'гривня', u'гривнi', u'гривень'), (u'копiйка', u'копiйки', u'копiйок')
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
    # form = 0 if n==1 else 1 if (n % 10 > 1 and n % 10 < 5 and (n % 100 < 10 or
    # n % 100 > 20)) else 2
    if (n % 100 < 10 or n % 100 > 20):
        if n % 10 == 1:
            form = 0
        elif (n % 10 > 1 and n % 10 < 5):
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
    if type(n) == int:
        if n < 0:
            minus = True
        else:
            minus = False

        n = abs(n)
        left = n / 100
        right = n % 100
    else:
        n = str(n).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
        else:
            left, right = n, 0
        left, right = int(left), int(right)
        minus = False
    cr1, cr2 = CURRENCIES[currency]

    if minus:
        minus_str = "мiнус "
    else:
        minus_str = ""

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


if __name__ == '__main__':
    import doctest

    doctest.testmod()
