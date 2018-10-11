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

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = ('ноль',)
ZERO_ORDINAL = ('нулевой',)

ONES_FEMININE = {
    1: ('одна',),
    2: ('две',),
    3: ('три',),
    4: ('четыре',),
    5: ('пять',),
    6: ('шесть',),
    7: ('семь',),
    8: ('восемь',),
    9: ('девять',),
}

ONES = {
    1: ('один', 'одного',),
    2: ('два', 'двух',),
    3: ('три', 'трёх',),
    4: ('четыре', 'четырёх',),
    5: ('пять', 'пяти',),
    6: ('шесть', 'шести',),
    7: ('семь', 'семи',),
    8: ('восемь', 'восьми',),
    9: ('девять', 'девяти',),
}

ONES_ORDINAL = {
    1: ('первый',),
    2: ('второй',),
    3: ('третий',),
    4: ('четвертый',),
    5: ('пятый',),
    6: ('шестой',),
    7: ('седьмой',),
    8: ('восьмой',),
    9: ('девятый',),
}

TENS = {
    0: ('десять', 'десятый',),
    1: ('одиннадцать', 'одиннадцатый',),
    2: ('двенадцать', 'двенадцатый',),
    3: ('тринадцать', 'тринадцатый',),
    4: ('четырнадцать', 'четырнадцатый',),
    5: ('пятнадцать', 'пятнадцатый',),
    6: ('шестнадцать', 'шестнадцатый',),
    7: ('семнадцать', 'семнадцатый',),
    8: ('восемнадцать', 'восемнадцатый',),
    9: ('девятнадцать', 'девятнадцатый',),
}

TWENTIES = {
    2: ('двадцать', 'двадцати',),
    3: ('тридцать', 'тридцати',),
    4: ('сорок', 'сорока',),
    5: ('пятьдесят', 'пятидесяти',),
    6: ('шестьдесят', 'шестидесяти',),
    7: ('семьдесят', 'семидесяти',),
    8: ('восемьдесят', 'восьмидесяти',),
    9: ('девяносто', 'девяноста',),
}

TWENTIES_ORDINAL = {
    2: ('двадцатый',),
    3: ('тридцатый',),
    4: ('сороковой',),
    5: ('пятидесятый',),
    6: ('шестидесятый',),
    7: ('семидесятый',),
    8: ('восьмидесятый',),
    9: ('девяностый',),
}

HUNDREDS = {
    1: ('сто', 'ста',),
    2: ('двести', 'двухсот',),
    3: ('триста', 'трёхсот',),
    4: ('четыреста', 'четырёхсот',),
    5: ('пятьсот', 'пятисот',),
    6: ('шестьсот', 'шестисот',),
    7: ('семьсот', 'семисот',),
    8: ('восемьсот', 'восьмисот',),
    9: ('девятьсот', 'девятисот',),
}

HUNDREDS_ORDINAL = {
    1: ('сотый',),
    2: ('двухсотый',),
    3: ('трёхсотый',),
    4: ('четырёхсотый',),
    5: ('пятисотый',),
    6: ('шестисотый',),
    7: ('семисотый',),
    8: ('восьмисотый',),
    9: ('девятисотый',),
}

THOUSANDS = {
    1: ('тысяча', 'тысячи', 'тысяч'),  # 10^3
    2: ('миллион', 'миллиона', 'миллионов'),  # 10^6
    3: ('миллиард', 'миллиарда', 'миллиардов'),  # 10^9
    4: ('триллион', 'триллиона', 'триллионов'),  # 10^12
    5: ('квадриллион', 'квадриллиона', 'квадриллионов'),  # 10^15
    6: ('квинтиллион', 'квинтиллиона', 'квинтиллионов'),  # 10^18
    7: ('секстиллион', 'секстиллиона', 'секстиллионов'),  # 10^21
    8: ('септиллион', 'септиллиона', 'септиллионов'),  # 10^24
    9: ('октиллион', 'октиллиона', 'октиллионов'),  # 10^27
    10: ('нониллион', 'нониллиона', 'нониллионов'),  # 10^30
}

class Num2Word_RU(Num2Word_Base):
    CURRENCY_FORMS = {
        'RUB': (
            ('рубль', 'рубля', 'рублей'), ('копейка', 'копейки', 'копеек')
        ),
        'EUR': (
            ('евро', 'евро', 'евро'), ('цент', 'цента', 'центов')
        ),
    }

    def setup(self):
        self.negword = "минус"
        self.pointword = "запятая"

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
        cardinal_words = self.to_cardinal(number).split(' ')

        ordinal_word = self.get_ordinal_equivalent(cardinal_words)

        if self.ordinal_number_contains_thousands(ordinal_word):
            ordinal_word = self.build_ordinal_thousands(ordinal_word, number)

        return self.merge_ordinal_words_string(cardinal_words, ordinal_word)

    def get_ordinal_equivalent(self, cardinal_words):
        last_word = cardinal_words[-1:][0]

        if last_word == ZERO[0]:
            return ZERO_ORDINAL[0]

        for key, value in ONES.items():
            if last_word == value[0]:
                return ONES_ORDINAL[key][0]

        for key, value in TENS.items():
            if last_word == value[0]:
                return last_word[:-2] + 'тый'

        for key, value in TWENTIES.items():
            if last_word == value[0]:
                return TWENTIES_ORDINAL[key][0]

        for key, value in HUNDREDS.items():
            if last_word == value[0]:
                return HUNDREDS_ORDINAL[key][0]

        thousand_identifier = self.get_ordinal_thousand(last_word)

        if thousand_identifier == '':
            raise ValueError("Ordinal wording for number could not be built")
        else:
            return [thousand_identifier]

    def get_ordinal_thousand(self, word):
        for value_tuple in THOUSANDS.values():
            for thousands_declination in value_tuple:
                if word == thousands_declination:
                    return self.transform_to_ordinal_thousand(word)
        return ''

    def transform_to_ordinal_thousand(self, word):
        if word[-1:] in ['а', 'и']:
            return word[:-1] + 'ный'
        elif word[-2:] == 'ов':
            return word[:-2] + 'ный'
        else:
            return word + 'ный'

    def ordinal_number_contains_thousands(self, ordinal_word):
        return isinstance(ordinal_word, list)

    def build_ordinal_thousands(self, ordinal_words, number):
        number = self.devaluate_number(number, 3)
        if number % 100 == 0:
            hundred = self.devaluate_number(number, 2)
            hundred_genitiv = HUNDREDS[hundred][1]
            ordinal_words.insert(0, hundred_genitiv)
        else:
            rest = number % 100
            if rest < 10:
                rest_genitiv = ONES[rest][1] if rest != 1 else ''
                ordinal_words.insert(0, rest_genitiv)
            elif rest < 20:
                rest_genitiv = TENS[rest % 10][1][:-2] + 'и'
                ordinal_words.insert(0, rest_genitiv)
            else:
                ones_genitiv = ONES[rest % 10][1] if rest % 10 > 0 else ''
                twenties_genitiv = TWENTIES[(rest - rest % 10) / 10][1]

                ordinal_words.insert(0, ones_genitiv)
                ordinal_words.insert(0, twenties_genitiv)

            if (number - rest) > 0:
                hundreds = (number - rest) / 100
                ordinal_words.insert(0, HUNDREDS[hundreds][1])

        return ordinal_words

    def devaluate_number(self, number, power):
        while number % 10**power == 0:
            number /= 10**power

        return number % 10**power

    def merge_ordinal_words_string(self, prefix_words, ordinal_word):
        if self.ordinal_number_contains_thousands(ordinal_word):
            merged_words_count = len(ordinal_word)
            ordinal_word = "".join(ordinal_word)
        else:
            merged_words_count = 1

        ordinal_words_string = prefix_words[:-merged_words_count]
        ordinal_words_string.append(ordinal_word)
        return " ".join(ordinal_words_string)

    def _cents_verbose(self, number, currency):
        return self._int2word(number, currency == 'RUB')

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
                words.append(self.pluralize(x, THOUSANDS[i]))

        return " ".join(words)
