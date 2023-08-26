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

from unittest import TestCase

from num2words import num2words


class Num2WordsKKTest(TestCase):
    def test_to_cardinal(self):
        self.maxDiff = None
        self.assertEqual(num2words(7, lang="kk"), "жеті")
        self.assertEqual(num2words(23, lang="kk"), "жиырма үш")
        self.assertEqual(num2words(145, lang="kk"), "жүз қырық бес")
        self.assertEqual(num2words(2869, lang="kk"),
                         "екі мың сегіз жүз алпыс тоғыз")
        self.assertEqual(
            num2words(-789000125, lang="kk"),
            "минус жеті жүз сексен тоғыз миллион жүз жиырма бес",
        )
        self.assertEqual(
            num2words(84932, lang="kk"), "сексен төрт мың тоғыз жүз отыз екі"
        )

    def test_to_cardinal_floats(self):
        self.assertEqual(num2words(100.67, lang="kk"), "жүз бүтін алпыс жеті")
        self.assertEqual(num2words(0.7, lang="kk"), "нөл бүтін жеті")
        self.assertEqual(num2words(1.73, lang="kk"), "бір бүтін жетпіс үш")
        self.assertEqual(num2words(10.02, lang="kk"), "он бүтін нөл екі")
        self.assertEqual(num2words(15.007, lang="kk"),
                         "он бес бүтін нөл нөл жеті")

    def test_to_ordinal(self):
        with self.assertRaises(NotImplementedError):
            num2words(1, lang="kk", to="ordinal")

    def test_to_currency(self):
        self.assertEqual(
            num2words(25.24, lang="kk", to="currency", currency="KZT"),
            "жиырма бес теңге, жиырма төрт тиын",
        )
        self.assertEqual(
            num2words(1996.4, lang="kk", to="currency", currency="KZT"),
            "бір мың тоғыз жүз тоқсан алты теңге, қырық тиын",
        )
        self.assertEqual(
            num2words(632924.51, lang="kk", to="currency", currency="KZT"),
            "алты жүз отыз екі мың тоғыз жүз жиырма төрт теңге, елу бір тиын",
        )
        self.assertEqual(
            num2words(632924.513, lang="kk", to="currency", currency="KZT"),
            "алты жүз отыз екі мың тоғыз жүз жиырма төрт теңге, елу бір тиын",
        )
        self.assertEqual(
            num2words(987654321.123, lang="kk", to="currency", currency="KZT"),
            "тоғыз жүз сексен жеті миллион алты жүз елу төрт мың "
            "үш жүз жиырма бір теңге, он екі тиын",
        )
