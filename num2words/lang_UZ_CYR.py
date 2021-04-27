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

from num2words.base import Num2Word_Base
from num2words.utils import get_digits, splitbyx

ZERO = ('нол',)

ONES_FEMININE = {
    1: ('бир',),
    2: ('икки',),
    3: ('уч',),
    4: ('тўрт',),
    5: ('беш',),
    6: ('олти',),
    7: ('етти',),
    8: ('саккиз',),
    9: ('тўққиз',),
}

ONES = {
    1: ('бир',),
    2: ('икки',),
    3: ('уч',),
    4: ('тўрт',),
    5: ('беш',),
    6: ('олти',),
    7: ('етти',),
    8: ('саккиз',),
    9: ('тўққиз',),
}

TENS = {
    0: ('ўн',),
    1: ('ўн бир',),
    2: ('ўн икки',),
    3: ('ўн уч',),
    4: ('ўн тўрт',),
    5: ('ўн беш',),
    6: ('ўн олти',),
    7: ('ўн етти',),
    8: ('ўн саккиз',),
    9: ('ўн тўққиз',),
}

TWENTIES = {
    2: ('йигирма',),
    3: ('ўттиз',),
    4: ('қирқ',),
    5: ('эллик',),
    6: ('олтмиш',),
    7: ('етмиш',),
    8: ('саксон',),
    9: ('тўқсон',),
}

HUNDREDS = {
    1: ('бир юз',),
    2: ('икки юз',),
    3: ('уч юз',),
    4: ('тўрт юз',),
    5: ('беш юз',),
    6: ('олти юз',),
    7: ('етти юз',),
    8: ('саккиз юз',),
    9: ('тўққиз юз',),
}

THOUSANDS = {
    1: ('минг', 'минг', 'минг'),  # 10^3
    2: ('миллион', 'миллион', 'миллион'),  # 10^6
    3: ('миллиард', 'миллиард', 'миллиард'),  # 10^9
    4: ('триллион', 'триллион', 'триллион'),  # 10^12
    5: ('квадриллион', 'квадриллион', 'квадриллион'),  # 10^15
    6: ('квинтиллион', 'квинтиллион', 'квинтиллион'),  # 10^18
    7: ('секстиллион', 'секстиллион', 'секстиллион'),  # 10^21
    8: ('септиллион', 'септиллион', 'септиллион'),  # 10^24
    9: ('октиллион', 'октиллион', 'октиллион'),  # 10^27
    10: ('нониллион', 'нониллион', 'нониллион'),  # 10^30
}


class Num2Word_UZ_CYRILLIC(Num2Word_Base):
    CURRENCY_FORMS = {
        'UZS': (
            ('сўм', 'сўм', 'сўм'), ('тийин', 'тийин', 'тийин')
        ),
        'EUR': (
            ('евро', 'евро', 'евро'), ('цент', 'цент', 'цент')
        ),
        'USD': (
            ('доллар', 'доллар', 'доллар'), ('цент', 'цент', 'цент')
        ),

    }

    def setup(self):
        self.negword = "минус"
        self.pointword = "вергул"
        self.ords = {"ноль": "нолинчи",
                     "бир": "биринчи",
                     "икки": "иккинчи",
                     "уч": "учинчи",
                     "тўрт": "тўртинчи",
                     "беш": "бешинчи",
                     "олти": "олтинчи",
                     "етти": "еттинчи",
                     "саккиз": "саккизинчи",
                     "тўққиз": "тўққизинчи",
                     "юз": "юзинчи"}
        self.ords_feminine = {"бир": "",
                              "бир": "",
                              "икки": "икки",
                              "уч": "уч",
                              "тўрт": "тўрт",
                              "беш": "беш",
                              "олти": "олти",
                              "етти": "етти",
                              "саккиз": "саккиз",
                              "тўққиз": "тўққиз"}

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            return u'%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                self._int2word(int(right))
            )
        else:
            return self._int2word(int(n))

    def pluralize(self, n, forms):
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

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        outwords = self.to_cardinal(number).split(" ")
        lastword = outwords[-1].lower()
        try:
            if len(outwords) > 1:
                if outwords[-2] in self.ords_feminine:
                    outwords[-2] = self.ords_feminine.get(
                        outwords[-2], outwords[-2])
                elif outwords[-2] == 'ўн':
                    outwords[-2] = outwords[-2][:-1] + 'н'
            if len(outwords) == 3:
                if outwords[-3] in ['бир', 'бир']:
                    outwords[-3] = ''
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[:-3] in self.ords_feminine:
                lastword = self.ords_feminine.get(
                    lastword[:-3], lastword) + "юзинчи"
            elif lastword[-1] == "а" or lastword[-2] == "м":
                lastword = lastword + "нчи"
            elif lastword[-1] == "к":
                lastword = lastword + "инчи"
            elif lastword[-1] == "қ":
                lastword = lastword + "инчи"
            elif lastword[-5:] == "ўн":
                lastword = lastword + 'инчи'
            elif lastword[-2] == "ш" or lastword[-1] == "ш":
                if lastword[-2] == "ш":
                    lastword = lastword[:-1] + "инчи"
                if lastword[-1] == "ш":
                    lastword = lastword + "инчи"
            elif lastword[-1] == "н" or lastword[-2] == "н":
                lastword = lastword + "инчи"
            elif lastword[-1] == "з" or lastword[-2] == "з":
                lastword = lastword + "инчи"
        outwords[-1] = self.title(lastword)
        return " ".join(outwords).strip()

    def _cents_verbose(self, number, currency):
        return self._int2word(number, currency == 'UZS')

    def _int2word(self, n, feminine=False):
        if n < 0:
            return ' '.join([self.negword, self._int2word(abs(n))])

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
                words.append(HUNDREDS[n3][0])

            if n2 > 1:
                words.append(TWENTIES[n2][0])

            if n2 == 1:
                words.append(TENS[n1][0])
            elif n1 > 0:
                ones = ONES_FEMININE if i == 1 or feminine and i == 0 else ONES
                words.append(ones[n1][0])

            if i > 0:
                words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)
