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

ZERO = ("нуль",)

ONES_FEMININE = {
    1: ("одна",),
    2: ("дві",),
    3: ("три",),
    4: ("чотири",),
    5: ("п’ять",),
    6: ("шість",),
    7: ("сім",),
    8: ("вісім",),
    9: ("дев’ять",),
}

ONES = {
    1: ("один",),
    2: ("два",),
    3: ("три",),
    4: ("чотири",),
    5: ("п’ять",),
    6: ("шість",),
    7: ("сім",),
    8: ("вісім",),
    9: ("дев’ять",),
}

TENS = {
    0: ("десять",),
    1: ("одинадцять",),
    2: ("дванадцять",),
    3: ("тринадцять",),
    4: ("чотирнадцять",),
    5: ("п’ятнадцять",),
    6: ("шістнадцять",),
    7: ("сімнадцять",),
    8: ("вісімнадцять",),
    9: ("дев’ятнадцять",),
}

TWENTIES = {
    2: ("двадцять",),
    3: ("тридцять",),
    4: ("сорок",),
    5: ("п’ятдесят",),
    6: ("шістдесят",),
    7: ("сімдесят",),
    8: ("вісімдесят",),
    9: ("дев’яносто",),
}

HUNDREDS = {
    1: ("сто",),
    2: ("двісті",),
    3: ("триста",),
    4: ("чотириста",),
    5: ("п’ятсот",),
    6: ("шістсот",),
    7: ("сімсот",),
    8: ("вісімсот",),
    9: ("дев’ятсот",),
}

THOUSANDS = {
    1: ("тисяча", "тисячі", "тисяч"),  # 10^3
    2: ("мільйон", "мільйони", "мільйонів"),  # 10^6
    3: ("мільярд", "мільярди", "мільярдів"),  # 10^9
    4: ("трильйон", "трильйона", "трильйонів"),  # 10^12
    5: ("квадрильйон", "квадрильйона", "квадрильйонів"),  # 10^15
    6: ("квінтильйон", "квінтильйони", "квінтильйонів"),  # 10^18
    7: ("секстильйонів", "секстильйонів", "секстильйонів"),  # 10^21
    8: ("септілліон", "септілліона", "септілліонов"),  # 10^24
    9: ("октілліон", "октілліона", "октілліонов"),  # 10^27
    10: ("нонілліон", "нонілліона", "нонілліонов"),  # 10^30
}


class Num2Word_UA(Num2Word_Base):
    CURRENCY_FORMS = {
        'RUB': (
            ("рубль", "рубля", "рублів"), ("копійка", "копійки", "копійок")
        ),
        'EUR': (
            ("євро", "євро", "євро"), ("цент", "цента", "центів")
        ),
        'USD': (
            ("долар", "долара", "доларів"), ("цент", "цента", "центів")
        ),
        'UAH': (
            ("гривня", "гривні", "гривень"), ("копійка", "копійки", "копійок")
        ),
    }

    def setup(self):
        self.negword = "мінус"
        self.pointword = "кома"
        self.ords = {"нуль": "нульовий",
                     "один": "перший",
                     "два": "другий",
                     "три": "третій",
                     "чотири": "четвертий",
                     "п’ять": "п’ятий",
                     "шість": "шостий",
                     "сім": "сьомий",
                     "вісім": "восьмий",
                     "дев’ять": "дев’ятий",
                     "сто": "сотий"}
        self.ords_feminine = {"один": "",
                              "одна": "",
                              "дві": "двох",
                              "три": "трьох",
                              "чотири": "чотирьох",
                              "п’ять": "п’яти",
                              "шість": "шести",
                              "сім": "семи",
                              "вісім": "восьми",
                              "дев’ять": "дев’яти"}

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
                elif outwords[-2] == "десять":
                    outwords[-2] = outwords[-2][:-1] + 'и'
            if len(outwords) == 3:
                if outwords[-3] in ["один", "одна"]:
                    outwords[-3] = ''
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[:-3] in self.ords_feminine:
                lastword = self.ords_feminine.get(
                    lastword[:-3], lastword) + "сотий"
            elif lastword[-1] == "ь" or lastword[-2] == "т":
                lastword = lastword[:-1] + "ий"
            elif lastword[-1] == "к":
                lastword = lastword + "овий"
            elif lastword[-5:] == "десят":
                lastword = lastword.replace('ь', 'и') + 'ий'
            elif lastword[-2] == "ч" or lastword[-1] == "ч":
                if lastword[-2] == "ч":
                    lastword = lastword[:-1] + "ний"
                if lastword[-1] == "ч":
                    lastword = lastword + "ний"
            elif lastword[-1] == "н" or lastword[-2] == "н":
                lastword = lastword[:lastword.rfind('н') + 1] + "ний"
            elif lastword[-1] == "д" or lastword[-2] == "д":
                lastword = lastword[:lastword.rfind('д') + 1] + "ний"
        outwords[-1] = self.title(lastword)
        return " ".join(outwords).strip()

    def _money_verbose(self, number, currency):
        return self._int2word(number, currency == 'UAH')

    def _cents_verbose(self, number, currency):
        return self._int2word(number, currency in ('UAH', 'RUB'))

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
