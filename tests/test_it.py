# -*- encoding: utf-8 -*-
# Copyright (c) 2015, Savoir-faire Linux inc.  All Rights Reserved.

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

class Num2WordsITTest(TestCase):

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="it")
        neg_crd = num2words(-number, lang="it")
        pos_ord = num2words(+number, lang="it", ordinal=True)
        neg_ord = num2words(-number, lang="it", ordinal=True)
        self.assertEqual("meno " + pos_crd, neg_crd)
        self.assertEqual("meno " + pos_ord, neg_ord)


    # We cannot test for equality because of floating point imprecisions.
    def test_float_to_cardinal(self):
        number = 3.1415
        s = "tre virgola uno quattro uno "
        crd_s = num2words(number, lang="it")
        almost_eq_crd = s + "quattro" in crd_s or s + "cinque" in crd_s
        self.assertTrue(almost_eq_crd)

    # See above.
    def test_float_to_ordinal(self):
        number = 3.1415
        s = "terzo virgola uno quattro uno "
        ord_s = num2words(number, lang="it", ordinal=True)
        almost_eq_ord = s + "quattro" in ord_s or s + "cinque" in ord_s
        self.assertTrue(almost_eq_ord)

    def test_0(self):
        self.assertEqual(num2words(0, lang="it"), "zero")

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
        self.assertEqual(num2words(7378, lang="it"), "settemilatrecentosettantotto")
        self.assertEqual(num2words(2000, lang="it"), "duemila")
        self.assertEqual(num2words(2100, lang="it"), "duemilacento")
        self.assertEqual(num2words(6870, lang="it"), "seimilaottocentosettanta")
        self.assertEqual(num2words(98765, lang="it"), "novantottomilasettecentosessantacinque")
        self.assertEqual(num2words(123456, lang="it"), "centoventitremilaquattrocentocinquantasei")

    def test_big_numbers(self):
        self.assertEqual(num2words(1000000, lang="it"), "un milione")
        self.assertEqual(num2words(1000007, lang="it"), "un milione e sette")
        self.assertEqual(num2words(1200000, lang="it"), "un milione e duecentomila")
        self.assertEqual(num2words(3000000, lang="it"), "tre milioni")
        self.assertEqual(num2words(3000005, lang="it"), "tre milioni e cinque")
        self.assertEqual(num2words(3800000, lang="it"), "tre milioni e ottocentomila")
        self.assertEqual(num2words(1000000000, lang="it"), "un miliardo")
        self.assertEqual(num2words(1000000017, lang="it"), "un miliardo e diciassette")
        self.assertEqual(num2words(2000000000, lang="it"), "due miliardi")
        self.assertEqual(num2words(2000001000, lang="it"), "due miliardi e mille")
        self.assertEqual(num2words(1234567890, lang="it"), "un miliardo e duecentotrentaquattro milioni e cinquecentosessantasettemilaottocentonovanta")
        self.assertEqual(num2words(1000000000000, lang="it"), "un bilione")

    def test_nth_0_to_99(self):
        self.assertEqual(num2words(0, lang="it", ordinal=True), "zero")
        self.assertEqual(num2words(1, lang="it", ordinal=True), "primo")
        self.assertEqual(num2words(8, lang="it", ordinal=True), "ottavo")
        self.assertEqual(num2words(23, lang="it", ordinal=True), "ventitreesimo")
        self.assertEqual(num2words(47, lang="it", ordinal=True), "quarantasettesimo")
        self.assertEqual(num2words(99, lang="it", ordinal=True), "novantanovesimo")

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="it", ordinal=True), "centesimo")
        self.assertEqual(num2words(112, lang="it", ordinal=True), "centododicesimo")
        self.assertEqual(num2words(120, lang="it", ordinal=True), "centoventesimo")
        self.assertEqual(num2words(316, lang="it", ordinal=True), "trecentosedicesimo")
        self.assertEqual(num2words(700, lang="it", ordinal=True), "settecentesimo")
        self.assertEqual(num2words(803, lang="it", ordinal=True), "ottocentotreesimo")
        self.assertEqual(num2words(923, lang="it", ordinal=True), "novecentoventitreesimo")

    def test_nth_1000_to_1000000(self):
        self.assertEqual(num2words(1000, lang="it", ordinal=True), "millesimo")
        self.assertEqual(num2words(1200, lang="it", ordinal=True), "milleduecentesimo")
        self.assertEqual(num2words(123456, lang="it", ordinal=True), "centoventitremilaquattrocentocinquantaseiesimo")
        self.assertEqual(num2words(987654, lang="it", ordinal=True), "novecentoottantasettemilaseicentocinquantaquattresimo")
