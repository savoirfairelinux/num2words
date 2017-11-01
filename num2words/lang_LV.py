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
nulle viens divi trīs četri pieci seši septiņi astoņi deviņi

>>> print(fill(' '.join([n2w(i+10) for i in range(10)])))
desmit vienpadsmit divpadsmit trīspadsmit četrpadsmit piecpadsmit
sešpadsmit septiņpadsmit astoņpadsmit deviņpadsmit

>>> print(fill(' '.join([n2w(i*10) for i in range(10)])))
nulle desmit divdesmit trīsdesmit četrdesmit piecdesmit sešdesmit
septiņdesmit astoņdesmit deviņdesmit

>>> print(n2w(100))
simts
>>> print(n2w(101))
simtu viens
>>> print(n2w(110))
simts desmit
>>> print(n2w(115))
simts piecpadsmit
>>> print(n2w(123))
simts divdesmit trīs
>>> print(n2w(1000))
tūkstotis
>>> print(n2w(1001))
tūkstotis viens
>>> print(n2w(2012))
divi tūkstoši divpadsmit

>>> print(fill(n2w(1234567890)))
miljards divi simti trīsdesmit četri miljoni pieci simti sešdesmit
septiņi tūkstoši astoņi simti deviņdesmit

>>> print(fill(n2w(215461407892039002157189883901676)))
divi simti piecpadsmit nontiljoni četri simti sešdesmit viens
oktiljons četri simti septiņi septiljoni astoņi simti deviņdesmit divi
sikstiljoni trīsdesmit deviņi kvintiljoni divi kvadriljoni simts
piecdesmit septiņi triljoni simts astoņdesmit deviņi miljardi astoņi
simti astoņdesmit trīs miljoni deviņi simti viens tūkstotis seši simti
septiņdesmit seši

>>> print(fill(n2w(719094234693663034822824384220291)))
septiņi simti deviņpadsmit nontiljoni deviņdesmit četri oktiljoni divi
simti trīsdesmit četri septiljoni seši simti deviņdesmit trīs
sikstiljoni seši simti sešdesmit trīs kvintiljoni trīsdesmit četri
kvadriljoni astoņi simti divdesmit divi triljoni astoņi simti
divdesmit četri miljardi trīs simti astoņdesmit četri miljoni divi
simti divdesmit tūkstoši divi simti deviņdesmit viens

# TODO: fix this:
# >>> print(fill(n2w(1000000000000000000000000000000)))
# nontiljons

>>> print(to_currency(1.0, 'EUR'))
viens eiro, nulle centu

>>> print(to_currency(1.0, 'LVL'))
viens lats, nulle santīmu

>>> print(to_currency(1234.56, 'EUR'))
tūkstotis divi simti trīsdesmit četri eiro, piecdesmit seši centi

>>> print(to_currency(1234.56, 'LVL'))
tūkstotis divi simti trīsdesmit četri lati, piecdesmit seši santīmi

>>> print(to_currency(10111, 'EUR', seperator=' un'))
simtu viens eiro un vienpadsmit centi

>>> print(to_currency(10121, 'LVL', seperator=' un'))
simtu viens lats un divdesmit viens santīms

>>> print(to_currency(-1251985, cents = False))
mīnus divpadsmit tūkstoši pieci simti deviņpadsmit eiro, 85 centi
"""
from __future__ import unicode_literals

from .currency import parse_currency_parts

ZERO = ('nulle',)

ONES = {
    1: ('viens',),
    2: ('divi',),
    3: ('trīs',),
    4: ('četri',),
    5: ('pieci',),
    6: ('seši',),
    7: ('septiņi',),
    8: ('astoņi',),
    9: ('deviņi',),
}

TENS = {
    0: ('desmit',),
    1: ('vienpadsmit',),
    2: ('divpadsmit',),
    3: ('trīspadsmit',),
    4: ('četrpadsmit',),
    5: ('piecpadsmit',),
    6: ('sešpadsmit',),
    7: ('septiņpadsmit',),
    8: ('astoņpadsmit',),
    9: ('deviņpadsmit',),
}

TWENTIES = {
    2: ('divdesmit',),
    3: ('trīsdesmit',),
    4: ('četrdesmit',),
    5: ('piecdesmit',),
    6: ('sešdesmit',),
    7: ('septiņdesmit',),
    8: ('astoņdesmit',),
    9: ('deviņdesmit',),
}

HUNDRED = ('simts', 'simti', 'simtu')

THOUSANDS = {
    1: ('tūkstotis', 'tūkstoši', 'tūkstošu'),
    2: ('miljons', 'miljoni', 'miljonu'),
    3: ('miljards', 'miljardi', 'miljardu'),
    4: ('triljons', 'triljoni', 'triljonu'),
    5: ('kvadriljons', 'kvadriljoni', 'kvadriljonu'),
    6: ('kvintiljons', 'kvintiljoni', 'kvintiljonu'),
    7: ('sikstiljons', 'sikstiljoni', 'sikstiljonu'),
    8: ('septiljons', 'septiljoni', 'septiljonu'),
    9: ('oktiljons', 'oktiljoni', 'oktiljonu'),
    10: ('nontiljons', 'nontiljoni', 'nontiljonu'),
}

"""
Sadly we have a legal form (used in legal and finance documents):
http://www.eiro.lv/files/upload/files/Eiro_rakstiba-1.pdf
https://likumi.lv/doc.php?id=254741
http://eur-lex.europa.eu/legal-content/LV/TXT/HTML/?uri=CELEX:31998R0974&from=LV
"""
CURRENCIES = {
    'LVL': (('lats', 'lati', 'latu'), ('santīms', 'santīmi', 'santīmu')),
    'EUR': (('eiro', 'eiro', 'eiro'), ('cents', 'centi', 'centu')),
    'EUR_LEGAL': (('euro', 'euro', 'euro'), ('cents', 'centi', 'centu')),
}


def splitby3(n):
    length = len(n)
    if length > 3:
        start = length % 3
        if start > 0:
            yield int(n[:start])
        for i in range(start, length, 3):
            yield int(n[i:i+3])
    else:
        yield int(n)


def get_digits(n):
    return [int(x) for x in reversed(list(('%03d' % n)[-3:]))]


def pluralize(n, forms):
    form = 0 if (n % 10 == 1 and n % 100 != 11) else 1 if n != 0 else 2
    return forms[form]


def int2word(n):
    if n == 0:
        return ZERO[0]

    words = []
    chunks = list(splitby3(str(n)))
    i = len(chunks)
    for x in chunks:
        i -= 1
        n1, n2, n3 = get_digits(x)

        if n3 > 0:
            if n3 == 1 and n2 == 0 and n1 > 0:
                words.append(HUNDRED[2])
            elif n3 > 1:
                words.append(ONES[n3][0])
                words.append(HUNDRED[1])
            else:
                words.append(HUNDRED[0])

        if n2 > 1:
            words.append(TWENTIES[n2][0])

        if n2 == 1:
            words.append(TENS[n1][0])
        elif n1 > 0 and not (i > 0 and x == 1):
            words.append(ONES[n1][0])

        if i > 0:
            words.append(pluralize(x, THOUSANDS[i]))

    return ' '.join(words)


def n2w(n):
    n = str(n).replace(',', '.')
    if '.' in n:
        left, right = n.split('.')
        return u'%s komats %s' % (int2word(int(left)), int2word(int(right)))
    else:
        return int2word(int(n))


def to_currency(n, currency='EUR', cents=True, seperator=','):
    left, right, is_negative = parse_currency_parts(n)
    cr1, cr2 = CURRENCIES[currency]

    minus_str = "mīnus " if is_negative else ""
    cents_str = int2word(right) if cents else "%02d" % right

    return u'%s%s %s%s %s %s' % (
        minus_str,
        int2word(left),
        pluralize(left, cr1),
        seperator,
        cents_str,
        pluralize(right, cr2)
    )


class Num2Word_LV(object):
    def to_cardinal(self, number):
        return n2w(number)

    def to_ordinal(self, number):
        raise NotImplementedError()

    def to_currency(self, n, currency='EUR', cents=True, seperator=','):
        return to_currency(n, currency, cents, seperator)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
