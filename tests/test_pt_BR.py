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

from decimal import Decimal
from unittest import TestCase

from num2words import num2words
from num2words.lang_PT_BR import Num2Word_PT_BR


class Num2WordsPTBRTest(TestCase):
    def setUp(self):
        super(Num2WordsPTBRTest, self).setUp()
        self.n2w = Num2Word_PT_BR()

    def test_cardinal_integer(self):
        self.assertEquals(num2words(1, lang='pt_BR'), 'um')
        self.assertEquals(num2words(2, lang='pt_BR'), 'dois')
        self.assertEquals(num2words(3, lang='pt_BR'), 'três')
        self.assertEquals(num2words(4, lang='pt_BR'), 'quatro')
        self.assertEquals(num2words(5, lang='pt_BR'), 'cinco')
        self.assertEquals(num2words(6, lang='pt_BR'), 'seis')
        self.assertEquals(num2words(7, lang='pt_BR'), 'sete')
        self.assertEquals(num2words(8, lang='pt_BR'), 'oito')
        self.assertEquals(num2words(9, lang='pt_BR'), 'nove')
        self.assertEquals(num2words(10, lang='pt_BR'), 'dez')
        self.assertEquals(num2words(11, lang='pt_BR'), 'onze')
        self.assertEquals(num2words(12, lang='pt_BR'), 'doze')
        self.assertEquals(num2words(13, lang='pt_BR'), 'treze')
        self.assertEquals(num2words(14, lang='pt_BR'), 'catorze')
        self.assertEquals(num2words(15, lang='pt_BR'), 'quinze')
        self.assertEquals(num2words(16, lang='pt_BR'), 'dezesseis')
        self.assertEquals(num2words(17, lang='pt_BR'), 'dezessete')
        self.assertEquals(num2words(18, lang='pt_BR'), 'dezoito')
        self.assertEquals(num2words(19, lang='pt_BR'), 'dezenove')
        self.assertEquals(num2words(20, lang='pt_BR'), 'vinte')

        self.assertEquals(num2words(21, lang='pt_BR'), 'vinte e um')
        self.assertEquals(num2words(22, lang='pt_BR'), 'vinte e dois')
        self.assertEquals(num2words(35, lang='pt_BR'), 'trinta e cinco')
        self.assertEquals(num2words(99, lang='pt_BR'), 'noventa e nove')

        self.assertEquals(num2words(100, lang='pt_BR'), 'cem')
        self.assertEquals(num2words(101, lang='pt_BR'), 'cento e um')
        self.assertEquals(num2words(128, lang='pt_BR'), 'cento e vinte e oito')
        self.assertEquals(num2words(713, lang='pt_BR'), 'setecentos e treze')

        self.assertEquals(num2words(1000, lang='pt_BR'), 'mil')
        self.assertEquals(num2words(1001, lang='pt_BR'), 'mil e um')
        self.assertEquals(num2words(1111, lang='pt_BR'), 'mil, cento e onze')
        self.assertEquals(num2words(2114, lang='pt_BR'), 'dois mil, cento e catorze')
        self.assertEquals(num2words(73421, lang='pt_BR'), 'setenta e três mil, quatrocentos e vinte e um')

        self.assertEquals(num2words(100000, lang='pt_BR'), 'cem mil')
        self.assertEquals(num2words(250050, lang='pt_BR'), 'duzentos e cinquenta mil e cinquenta')
        self.assertEquals(num2words(6000000, lang='pt_BR'), 'seis milhões')
        self.assertEquals(num2words(19000000000, lang='pt_BR'), 'dezenove bilhões')
        self.assertEquals(num2words(145000000002, lang='pt_BR'), 'cento e quarenta e cinco bilhões e dois')

    def test_cardinal_integer_negative(self):
        self.assertEquals(num2words(-1, lang='pt_BR'), 'menos um')
        self.assertEquals(num2words(-256, lang='pt_BR'), 'menos duzentos e cinquenta e seis')
        self.assertEquals(num2words(-1000, lang='pt_BR'), 'menos mil')
        self.assertEquals(num2words(-1000000, lang='pt_BR'), 'menos um milhão')
        self.assertEquals(num2words(-1234567, lang='pt_BR'), 'menos um milhão, duzentos e trinta e quatro mil, quinhentos e sessenta e sete')

    def test_cardinal_float(self):
        self.assertEquals(num2words(Decimal('1.00'), lang='pt_BR'), 'um')
        self.assertEquals(num2words(Decimal('1.01'), lang='pt_BR'), 'um ponto zero um')
        self.assertEquals(num2words(Decimal('1.035'), lang='pt_BR'), 'um ponto zero três')
        self.assertEquals(num2words(Decimal('1.35'), lang='pt_BR'), 'um ponto três cinco')
        self.assertEquals(num2words(Decimal('3.14159'), lang='pt_BR'), 'três ponto um quatro')
        self.assertEquals(num2words(Decimal('101.22'), lang='pt_BR'), 'cento e um ponto dois dois')
        self.assertEquals(num2words(Decimal('2345.75'), lang='pt_BR'), 'dois mil, trezentos e quarenta e cinco ponto sete cinco')

    def test_cardinal_float_negative(self):
        self.assertEquals(num2words(Decimal('-2.34'), lang='pt_BR'), 'menos dois ponto três quatro')
        self.assertEquals(num2words(Decimal('-9.99'), lang='pt_BR'), 'menos nove ponto nove nove')
        self.assertEquals(num2words(Decimal('-7.01'), lang='pt_BR'), 'menos sete ponto zero um')
        self.assertEquals(num2words(Decimal('-222.22'), lang='pt_BR'), 'menos duzentos e vinte e dois ponto dois dois')

    def test_ordinal(self):
        self.assertEquals(num2words(1, lang='pt_BR', ordinal=True), 'primeiro')
        self.assertEquals(num2words(2, lang='pt_BR', ordinal=True), 'segundo')
        self.assertEquals(num2words(3, lang='pt_BR', ordinal=True), 'terceiro')
        self.assertEquals(num2words(4, lang='pt_BR', ordinal=True), 'quarto')
        self.assertEquals(num2words(5, lang='pt_BR', ordinal=True), 'quinto')
        self.assertEquals(num2words(6, lang='pt_BR', ordinal=True), 'sexto')
        self.assertEquals(num2words(7, lang='pt_BR', ordinal=True), 'sétimo')
        self.assertEquals(num2words(8, lang='pt_BR', ordinal=True), 'oitavo')
        self.assertEquals(num2words(9, lang='pt_BR', ordinal=True), 'nono')
        self.assertEquals(num2words(10, lang='pt_BR', ordinal=True), 'décimo')
        self.assertEquals(num2words(11, lang='pt_BR', ordinal=True), 'décimo primeiro')
        self.assertEquals(num2words(12, lang='pt_BR', ordinal=True), 'décimo segundo')
        self.assertEquals(num2words(13, lang='pt_BR', ordinal=True), 'décimo terceiro')
        self.assertEquals(num2words(14, lang='pt_BR', ordinal=True), 'décimo quarto')
        self.assertEquals(num2words(15, lang='pt_BR', ordinal=True), 'décimo quinto')
        self.assertEquals(num2words(16, lang='pt_BR', ordinal=True), 'décimo sexto')
        self.assertEquals(num2words(17, lang='pt_BR', ordinal=True), 'décimo sétimo')
        self.assertEquals(num2words(18, lang='pt_BR', ordinal=True), 'décimo oitavo')
        self.assertEquals(num2words(19, lang='pt_BR', ordinal=True), 'décimo nono')
        self.assertEquals(num2words(20, lang='pt_BR', ordinal=True), 'vigésimo')

        self.assertEquals(num2words(21, lang='pt_BR', ordinal=True), 'vigésimo primeiro')
        self.assertEquals(num2words(22, lang='pt_BR', ordinal=True), 'vigésimo segundo')
        self.assertEquals(num2words(35, lang='pt_BR', ordinal=True), 'trigésimo quinto')
        self.assertEquals(num2words(99, lang='pt_BR', ordinal=True), 'nonagésimo nono')

        self.assertEquals(num2words(100, lang='pt_BR', ordinal=True), 'centésimo')
        self.assertEquals(num2words(101, lang='pt_BR', ordinal=True), 'centésimo primeiro')
        self.assertEquals(num2words(128, lang='pt_BR', ordinal=True), 'centésimo vigésimo oitavo')
        self.assertEquals(num2words(713, lang='pt_BR', ordinal=True), 'septigentésimo décimo terceiro')

        self.assertEquals(num2words(1000, lang='pt_BR', ordinal=True), 'milésimo')
        self.assertEquals(num2words(1001, lang='pt_BR', ordinal=True), 'milésimo primeiro')
        self.assertEquals(num2words(1111, lang='pt_BR', ordinal=True), 'milésimo centésimo décimo primeiro')
        self.assertEquals(num2words(2114, lang='pt_BR', ordinal=True), 'segundo milésimo centésimo décimo quarto')
        self.assertEquals(num2words(73421, lang='pt_BR', ordinal=True), 'septuagésimo terceiro milésimo quadrigentésimo vigésimo primeiro')

        self.assertEquals(num2words(100000, lang='pt_BR', ordinal=True), 'centésimo milésimo')
        self.assertEquals(num2words(250050, lang='pt_BR', ordinal=True), 'ducentésimo quinquagésimo milésimo quinquagésimo')
        self.assertEquals(num2words(6000000, lang='pt_BR', ordinal=True), 'sexto milionésimo')
        self.assertEquals(num2words(19000000000, lang='pt_BR', ordinal=True), 'décimo nono bilionésimo')
        self.assertEquals(num2words(145000000002, lang='pt_BR', ordinal=True), 'centésimo quadragésimo quinto bilionésimo segundo')

    def test_currency_integer(self):
        self.assertEquals(self.n2w.to_currency(1), 'um real')
        self.assertEquals(self.n2w.to_currency(2), 'dois reais')
        self.assertEquals(self.n2w.to_currency(3), 'três reais')
        self.assertEquals(self.n2w.to_currency(4), 'quatro reais')
        self.assertEquals(self.n2w.to_currency(5), 'cinco reais')
        self.assertEquals(self.n2w.to_currency(6), 'seis reais')
        self.assertEquals(self.n2w.to_currency(7), 'sete reais')
        self.assertEquals(self.n2w.to_currency(8), 'oito reais')
        self.assertEquals(self.n2w.to_currency(9), 'nove reais')
        self.assertEquals(self.n2w.to_currency(10), 'dez reais')
        self.assertEquals(self.n2w.to_currency(11), 'onze reais')
        self.assertEquals(self.n2w.to_currency(12), 'doze reais')
        self.assertEquals(self.n2w.to_currency(13), 'treze reais')
        self.assertEquals(self.n2w.to_currency(14), 'catorze reais')
        self.assertEquals(self.n2w.to_currency(15), 'quinze reais')
        self.assertEquals(self.n2w.to_currency(16), 'dezesseis reais')
        self.assertEquals(self.n2w.to_currency(17), 'dezessete reais')
        self.assertEquals(self.n2w.to_currency(18), 'dezoito reais')
        self.assertEquals(self.n2w.to_currency(19), 'dezenove reais')
        self.assertEquals(self.n2w.to_currency(20), 'vinte reais')

        self.assertEquals(self.n2w.to_currency(21), 'vinte e um reais')
        self.assertEquals(self.n2w.to_currency(22), 'vinte e dois reais')
        self.assertEquals(self.n2w.to_currency(35), 'trinta e cinco reais')
        self.assertEquals(self.n2w.to_currency(99), 'noventa e nove reais')

        self.assertEquals(self.n2w.to_currency(100), 'cem reais')
        self.assertEquals(self.n2w.to_currency(101), 'cento e um reais')
        self.assertEquals(self.n2w.to_currency(128), 'cento e vinte e oito reais')
        self.assertEquals(self.n2w.to_currency(713), 'setecentos e treze reais')

        self.assertEquals(self.n2w.to_currency(1000), 'mil reais')
        self.assertEquals(self.n2w.to_currency(1001), 'mil e um reais')
        self.assertEquals(self.n2w.to_currency(1111), 'mil, cento e onze reais')
        self.assertEquals(self.n2w.to_currency(2114), 'dois mil, cento e catorze reais')
        self.assertEquals(self.n2w.to_currency(73421), 'setenta e três mil, quatrocentos e vinte e um reais')

        self.assertEquals(self.n2w.to_currency(100000), 'cem mil reais')
        self.assertEquals(self.n2w.to_currency(250050), 'duzentos e cinquenta mil e cinquenta reais')
        self.assertEquals(self.n2w.to_currency(6000000), 'seis milhões de reais')
        self.assertEquals(self.n2w.to_currency(19000000000), 'dezenove bilhões de reais')
        self.assertEquals(self.n2w.to_currency(145000000002), 'cento e quarenta e cinco bilhões e dois reais')

    def test_currency_integer_negative(self):
        self.assertEquals(self.n2w.to_currency(-1), 'menos um real')
        self.assertEquals(self.n2w.to_currency(-256), 'menos duzentos e cinquenta e seis reais')
        self.assertEquals(self.n2w.to_currency(-1000), 'menos mil reais')
        self.assertEquals(self.n2w.to_currency(-1000000), 'menos um milhão de reais')
        self.assertEquals(self.n2w.to_currency(-1234567), 'menos um milhão, duzentos e trinta e quatro mil, quinhentos e sessenta e sete reais')

    def test_currency_float(self):
        self.assertEquals(self.n2w.to_currency(Decimal('1.00')), 'um real')
        self.assertEquals(self.n2w.to_currency(Decimal('1.01')), 'um real e um centavo')
        self.assertEquals(self.n2w.to_currency(Decimal('1.035')), 'um real e três centavos')
        self.assertEquals(self.n2w.to_currency(Decimal('1.35')), 'um real e trinta e cinco centavos')
        self.assertEquals(self.n2w.to_currency(Decimal('3.14159')), 'três reais e catorze centavos')
        self.assertEquals(self.n2w.to_currency(Decimal('101.22')), 'cento e um reais e vinte e dois centavos')
        self.assertEquals(self.n2w.to_currency(Decimal('2345.75')), 'dois mil, trezentos e quarenta e cinco reais e setenta e cinco centavos')

    def test_currency_float_negative(self):
        self.assertEquals(self.n2w.to_currency(Decimal('-2.34')), 'menos dois reais e trinta e quatro centavos')
        self.assertEquals(self.n2w.to_currency(Decimal('-9.99')), 'menos nove reais e noventa e nove centavos')
        self.assertEquals(self.n2w.to_currency(Decimal('-7.01')), 'menos sete reais e um centavo')
        self.assertEquals(self.n2w.to_currency(Decimal('-222.22')), 'menos duzentos e vinte e dois reais e vinte e dois centavos')

    def test_year(self):
        self.assertEquals(self.n2w.to_year(1001), 'mil e um')
        self.assertEquals(self.n2w.to_year(1789), 'mil, setecentos e oitenta e nove')
        self.assertEquals(self.n2w.to_year(1942), 'mil, novecentos e quarenta e dois')
        self.assertEquals(self.n2w.to_year(1984), 'mil, novecentos e oitenta e quatro')
        self.assertEquals(self.n2w.to_year(2000), 'dois mil')
        self.assertEquals(self.n2w.to_year(2001), 'dois mil e um')
        self.assertEquals(self.n2w.to_year(2016), 'dois mil e dezesseis')

    def test_year_negative(self):
        self.assertEquals(self.n2w.to_year(-30), 'trinta antes de Cristo')
        self.assertEquals(self.n2w.to_year(-744), 'setecentos e quarenta e quatro antes de Cristo')
        self.assertEquals(self.n2w.to_year(-10000), 'dez mil antes de Cristo')
