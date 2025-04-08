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

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'un euro e zero centesimi'),
    (2.01, 'due euro e un centesimo'),
    (8.10, 'otto euro e dieci centesimi'),
    (12.26, 'dodici euro e ventisei centesimi'),
    (21.29, 'ventun euro e ventinove centesimi'),
    (81.25, 'ottantun euro e venticinque centesimi'),
    (100.00, 'cento euro e zero centesimi'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'un dollaro e zero centesimi'),
    (2.01, 'due dollari e un centesimo'),
    (8.10, 'otto dollari e dieci centesimi'),
    (12.26, 'dodici dollari e ventisei centesimi'),
    (21.29, 'ventun dollari e ventinove centesimi'),
    (81.25, 'ottantun dollari e venticinque centesimi'),
    (100.00, 'cento dollari e zero centesimi'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'una sterlina e zero penny'),
    (2.01, 'due sterline e un penny'),
    (8.10, 'otto sterline e dieci penny'),
    (12.26, 'dodici sterline e ventisei penny'),
    (21.29, 'ventun sterline e ventinove penny'),
    (81.25, 'ottantun sterline e venticinque penny'),
    (100.00, 'cento sterline e zero penny'),
)


class Num2WordsITTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="it")
        neg_crd = num2words(-number, lang="it")
        pos_ord = num2words(+number, lang="it", ordinal=True)
        neg_ord = num2words(-number, lang="it", ordinal=True)
        self.assertEqual("meno " + pos_crd, neg_crd)
        self.assertEqual("meno " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words("3.1415", lang="it"),
            "tre virgola uno quattro uno cinque"
        )
        self.assertEqual(
            num2words(3.1415, lang="it"), "tre virgola uno quattro uno cinque"
        )
        self.assertEqual(
            num2words(-5.15, lang="it"), "meno cinque virgola uno cinque"
        )
        self.assertEqual(
            num2words(-0.15, lang="it"), "meno zero virgola uno cinque"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="it", ordinal=True),
            "terzo virgola uno quattro uno cinque"
        )
        self.assertEqual(
            num2words(-5.15, lang="it", ordinal=True),
            "meno quinto virgola uno cinque"
        )
        self.assertEqual(
            num2words(-0.15, lang="it", ordinal=True),
            "meno zero virgola uno cinque"
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="it"), "zero")
        self.assertEqual(num2words(0, lang="it", ordinal=True), "zero")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="it"), "uno")
        self.assertEqual(num2words(2, lang="it"), "due")
        self.assertEqual(num2words(7, lang="it"), "sette")
        self.assertEqual(num2words(10, lang="it"), "dieci")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="it"), "undici")
        self.assertEqual(num2words(13, lang="it"), "tredici")
        self.assertEqual(num2words(15, lang="it"), "quindici")
        self.assertEqual(num2words(16, lang="it"), "sedici")
        self.assertEqual(num2words(19, lang="it"), "diciannove")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="it"), "venti")
        self.assertEqual(num2words(21, lang="it"), "ventuno")
        self.assertEqual(num2words(23, lang="it"), "ventitré")
        self.assertEqual(num2words(28, lang="it"), "ventotto")
        self.assertEqual(num2words(31, lang="it"), "trentuno")
        self.assertEqual(num2words(40, lang="it"), "quaranta")
        self.assertEqual(num2words(66, lang="it"), "sessantasei")
        self.assertEqual(num2words(92, lang="it"), "novantadue")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="it"), "cento")
        self.assertEqual(num2words(111, lang="it"), "centoundici")
        self.assertEqual(num2words(150, lang="it"), "centocinquanta")
        self.assertEqual(num2words(196, lang="it"), "centonovantasei")
        self.assertEqual(num2words(200, lang="it"), "duecento")
        self.assertEqual(num2words(210, lang="it"), "duecentodieci")
        self.assertEqual(num2words(701, lang="it"), "settecentouno")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="it"), "mille")
        self.assertEqual(num2words(1001, lang="it"), "milleuno")
        self.assertEqual(num2words(1500, lang="it"), "millecinquecento")
        self.assertEqual(
            num2words(7378, lang="it"), "settemilatrecentosettantotto"
        )
        self.assertEqual(num2words(2000, lang="it"), "duemila")
        self.assertEqual(num2words(2100, lang="it"), "duemilacento")
        self.assertEqual(
            num2words(6870, lang="it"), "seimilaottocentosettanta"
        )
        self.assertEqual(num2words(10000, lang="it"), "diecimila")
        self.assertEqual(
            num2words(98765, lang="it"),
            "novantottomilasettecentosessantacinque"
        )
        self.assertEqual(num2words(100000, lang="it"), "centomila")
        self.assertEqual(
            num2words(523456, lang="it"),
            "cinquecentoventitremilaquattrocentocinquantasei"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="it"), "un milione")
        self.assertEqual(num2words(1000007, lang="it"), "un milione e sette")
        self.assertEqual(
            num2words(1200000, lang="it"), "un milione e duecentomila"
        )
        self.assertEqual(num2words(3000000, lang="it"), "tre milioni")
        self.assertEqual(num2words(3000005, lang="it"), "tre milioni e cinque")
        self.assertEqual(
            num2words(3800000, lang="it"), "tre milioni e ottocentomila"
        )
        self.assertEqual(num2words(1000000000, lang="it"), "un miliardo")
        self.assertEqual(
            num2words(1000000017, lang="it"), "un miliardo e diciassette"
        )
        self.assertEqual(num2words(2000000000, lang="it"), "due miliardi")
        self.assertEqual(
            num2words(2000001000, lang="it"), "due miliardi e mille"
        )
        self.assertEqual(
            num2words(1234567890, lang="it"),
            "un miliardo, duecentotrentaquattro milioni e "
            "cinquecentosessantasettemilaottocentonovanta"
        )
        self.assertEqual(num2words(1000000000000, lang="it"), "un bilione")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="it"),
            "centoventitré quadriliardi, quattrocentocinquantasei "
            "quadrilioni, settecentottantanove triliardi, dodici trilioni, "
            "trecentoquarantacinque biliardi, seicentosettantotto bilioni, "
            "novecentouno miliardi, duecentotrentaquattro milioni e "
            "cinquecentosessantasettemilaottocentonovanta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="it", ordinal=True), "primo")
        self.assertEqual(num2words(8, lang="it", ordinal=True), "ottavo")
        self.assertEqual(
            num2words(21, lang="it", ordinal=True), "ventunesimo"
        )
        self.assertEqual(
            num2words(23, lang="it", ordinal=True), "ventitreesimo"
        )
        self.assertEqual(
            num2words(47, lang="it", ordinal=True), "quarantasettesimo"
        )
        self.assertEqual(
            num2words(99, lang="it", ordinal=True), "novantanovesimo"
        )

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="it", ordinal=True), "centesimo")
        self.assertEqual(
            num2words(112, lang="it", ordinal=True), "centododicesimo"
        )
        self.assertEqual(
            num2words(120, lang="it", ordinal=True), "centoventesimo"
        )
        self.assertEqual(
            num2words(121, lang="it", ordinal=True), "centoventunesimo"
        )
        self.assertEqual(
            num2words(316, lang="it", ordinal=True), "trecentosedicesimo"
        )
        self.assertEqual(
            num2words(700, lang="it", ordinal=True), "settecentesimo"
        )
        self.assertEqual(
            num2words(803, lang="it", ordinal=True), "ottocentotreesimo"
        )
        self.assertEqual(
            num2words(923, lang="it", ordinal=True), "novecentoventitreesimo"
        )

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="it", ordinal=True), "millesimo")
        self.assertEqual(
            num2words(1001, lang="it", ordinal=True), "milleunesimo"
        )
        self.assertEqual(
            num2words(1003, lang="it", ordinal=True), "milletreesimo"
        )
        self.assertEqual(
            num2words(1200, lang="it", ordinal=True), "milleduecentesimo"
        )
        self.assertEqual(
            num2words(8640, lang="it", ordinal=True),
            "ottomilaseicentoquarantesimo"
        )
        self.assertEqual(
            num2words(14000, lang="it", ordinal=True), "quattordicimillesimo"
        )
        self.assertEqual(
            num2words(123456, lang="it", ordinal=True),
            "centoventitremilaquattrocentocinquantaseiesimo"
        )
        self.assertEqual(
            num2words(987654, lang="it", ordinal=True),
            "novecentottantasettemilaseicentocinquantaquattresimo"
        )

    def test_nth_big(self):
        self.assertEqual(
            num2words(1000000001, lang="it", ordinal=True),
            "un miliardo e unesimo"
        )
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="it", ordinal=True),
            "centoventitré quadriliardi, quattrocentocinquantasei "
            "quadrilioni, settecentottantanove triliardi, dodici trilioni, "
            "trecentoquarantacinque biliardi, seicentosettantotto bilioni, "
            "novecentouno miliardi, duecentotrentaquattro milioni e "
            "cinquecentosessantasettemilaottocentonovantesimo"
        )

    def test_with_floats(self):
        self.assertEqual(
            num2words(1.0, lang="it"), "uno"
        )
        self.assertEqual(
            num2words(1.1, lang="it"), "uno virgola uno"
        )

    def test_with_strings(self):
        for i in range(2002):
            # Just make sure it doesn't raise an exception
            num2words(str(i), lang='it', to='cardinal')
            num2words(str(i), lang='it', to='ordinal')
        self.assertEqual(num2words('1', lang="it", to='ordinal'), "primo")
        self.assertEqual(
            num2words('100', lang="it", to='ordinal'),
            "centesimo"
        )
        self.assertEqual(
            num2words('1000', lang="it", to='ordinal'),
            "millesimo"
        )
        self.assertEqual(
            num2words('1234567890123456789012345678', lang="it", to='ordinal'),
            "un quadriliardo, duecentotrentaquattro quadrilioni, "
            "cinquecentosessantasette triliardi, ottocentonovanta trilioni, "
            "centoventitré biliardi, quattrocentocinquantasei bilioni, "
            "settecentottantanove miliardi, dodici milioni e "
            "trecentoquarantacinquemilaseicentosettantottesimo"
        )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='it', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='it', to='currency', currency='USD'),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang='it', to='currency', currency='GBP'),
                test[1]
            )
