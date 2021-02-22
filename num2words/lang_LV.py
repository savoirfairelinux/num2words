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

ZERO = ('nulle', 'nulltais')

ONES = {
    1: ('viens', 'pirmais'),
    2: ('divi', 'otrais'),
    3: ('trīs', 'trešais'),
    4: ('četri', 'ceturtais'),
    5: ('pieci', 'piektais'),
    6: ('seši', 'sestais'),
    7: ('septiņi', 'septītais'),
    8: ('astoņi', 'astotais'),
    9: ('deviņi', 'devītais'),
}

TENS = {
    0: ('desmit', 'desmitais'),
    1: ('vienpadsmit', 'vienpadsmitais'),
    2: ('divpadsmit', 'divpadsmitais'),
    3: ('trīspadsmit', 'trīspadsmitais'),
    4: ('četrpadsmit', 'četrpadsmitais'),
    5: ('piecpadsmit', 'piecpadsmitais'),
    6: ('sešpadsmit', 'sešpadsmitais'),
    7: ('septiņpadsmit', 'septiņpadsmitais'),
    8: ('astoņpadsmit', 'astoņpadsmitais'),
    9: ('deviņpadsmit', 'deviņpadsmitais'),
}

TWENTIES = {
    2: ('divdesmit', 'divdesmitais'),
    3: ('trīsdesmit', 'trīsdesmitais'),
    4: ('četrdesmit', 'četrdesmitais'),
    5: ('piecdesmit', 'piecdesmitais'),
    6: ('sešdesmit', 'sešdesmitais'),
    7: ('septiņdesmit', 'septiņdesmitais'),
    8: ('astoņdesmit', 'astoņdesmitais'),
    9: ('deviņdesmit', 'deviņdesmitais'),
}

HUNDRED = ('simts', 'simti', 'simtu', 'simtais')

HUNDREDS_ORDINAL = {
    2: ('divsimtais',),
    3: ('trīssimtais',),
    4: ('četrsimtais',),
    5: ('piecsimtais',),
    6: ('sešsimtais',),
    7: ('septiņsimtais',),
    8: ('astoņsimtais',),
    9: ('deviņsimtais',),
}

THOUSANDS = {
    1: ('tūkstotis', 'tūkstoši', 'tūkstošu', 'tūkstošais'),
    2: ('miljons', 'miljoni', 'miljonu', 'miljonais'),
    3: ('miljards', 'miljardi', 'miljardu'),
    4: ('triljons', 'triljoni', 'triljonu'),
    5: ('kvadriljons', 'kvadriljoni', 'kvadriljonu'),
    6: ('kvintiljons', 'kvintiljoni', 'kvintiljonu'),
    7: ('sikstiljons', 'sikstiljoni', 'sikstiljonu'),
    8: ('septiljons', 'septiljoni', 'septiljonu'),
    9: ('oktiljons', 'oktiljoni', 'oktiljonu'),
    10: ('nontiljons', 'nontiljoni', 'nontiljonu'),
}

'''
THOUSANDS_ORDINAL = {
    2: ('tūkstošais',),
    3: ('miljonais',),
    4: ('miljardus',),
    5: ('triljonus',),
    6: ('kvadriljonus',),
    7: ('septiņsimtais',),
    8: ('astoņsimtais',),
    9: ('deviņsimtais',),
}
'''

GENERIC_DOLLARS = ('dolārs', 'dolāri', 'dolāru')
GENERIC_CENTS = ('cents', 'centi', 'centu')

GENERIC_KRONA = ('krona', 'kronas', 'kronu')
GENERIC_ERA = ('ēre', 'ēras', 'ēru')


class Num2Word_LV(Num2Word_Base):
    """
    Sadly we have a legal form (used in legal and finance documents):
    http://www.eiro.lv/files/upload/files/Eiro_rakstiba-1.pdf
    https://likumi.lv/doc.php?id=254741
    http://eur-lex.europa.eu/legal-content/LV/TXT/HTML/?uri=CELEX:31998R0974&from=LV

    Source: http://publications.europa.eu/code/lv/lv-5000500.htm
    """
    CURRENCY_FORMS = {
        'AUD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'CAD': (GENERIC_DOLLARS, GENERIC_CENTS),
        # repalced by EUR
        'EEK': (GENERIC_KRONA, GENERIC_CENTS),
        'EUR': (('eiro', 'eiro', 'eiro'), GENERIC_CENTS),
        'EUR_LEGAL': (('euro', 'euro', 'euro'), GENERIC_CENTS),
        'GBP': (
            ('sterliņu mārciņa', 'sterliņu mārciņas', 'sterliņu mārciņu'),
            ('penss', 'pensi', 'pensu')),
        # replaced by EUR
        'LTL': (('lits', 'liti', 'litu'), GENERIC_CENTS),
        # replaced by EUR
        'LVL': (('lats', 'lati', 'latu'),
                ('santīms', 'santīmi', 'santīmu')),
        'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'RUB': (('rublis', 'rubļi', 'rubļu'),
                ('kapeika', 'kapeikas', 'kapeiku')),
        'SEK': (GENERIC_KRONA, GENERIC_ERA),
        'NOK': (GENERIC_KRONA, GENERIC_ERA),
        'PLN': (('zlots', 'zloti', 'zlotu'),
                ('grasis', 'graši', 'grašu')),
    }

    CURRENCY_ADJECTIVES = {
        'AUD': 'Austrālijas',
        'CAD': 'Kanādas',
        'EEK': 'Igaunijas',
        'USD': 'ASV',
        'RUB': 'Kreivijas',
        'SEK': 'Zviedrijas',
        'NOK': 'Norvēģijas',
    }

    def setup(self):
        self.negword = "mīnus"
        self.pointword = "komats"

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        base_str, n = self.parse_minus(n)
        if '.' in n:
            left, right = n.split('.')
            return '%s%s %s %s' % (
                base_str,
                self._int2word(int(left)),
                self.pointword,
                self._int2word(int(right))
            )
        else:
            return "%s%s" % (base_str, self._int2word(int(n)))

    def pluralize(self, n, forms):
        form = 0 if (n % 10 == 1 and n % 100 != 11) else 1 if n != 0 else 2
        return forms[form]

    def to_ordinal(self, number):
        n = str(number).replace(',', '.')
        base_str, n = self.parse_minus(n)
        if '.' in n:
            left, right = n.split('.')
            return '%s%s %s %s' % (
                base_str,
                self._int2word(int(left)),
                self.pointword,
                self._int2word(int(right))
            )
        else:
            return "%s%s" % (base_str, self._int2ordinal_word(int(n)))

    def _int2word(self, n):
        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

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
                words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)

    def _int2ordinal_word(self, n):
        if n == 0:
            return ZERO[1]
        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1
            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)
            if n3 > 0:
                if n3 == 1 and n2 == 0 and n1 > 0:
                    words.append(HUNDRED[0])
                elif n3 > 1:

                    if i == 0 and n1 == 0 and n2 == 0:
                        words.append(HUNDREDS_ORDINAL[n3][0])
                    else:
                        words.append(ONES[n3][0])
                        words.append(HUNDRED[1])
                else:
                    if i == 0 and n1 == 0 and n2 == 0:
                        words.append(HUNDRED[3])
                    else:
                        words.append(HUNDRED[0])
            if n2 > 1 and n1 == 0:
                if i > 0:
                    words.append(TWENTIES[n2][0])
                else:
                    words.append(TWENTIES[n2][1])
            if n2 > 1 and n1 != 0:
                words.append(TWENTIES[n2][0])
            if n2 == 1:
                if i >= 1:
                    words.append(TENS[n1][0])
                else:
                    words.append(TENS[n1][1])
            elif n1 > 0 and not (i > 0 and x == 1):
                if i >= 1 and x > 1:
                    words.append(ONES[n1][0])
                else:
                    words.append(ONES[n1][1])

            if i > 0 and sum(chunks[1:]) == 0:
                words.append(THOUSANDS[i][3])
            elif i > 0:
                words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)