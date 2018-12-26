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

from decimal import Decimal
from unittest import TestCase

from num2words import num2words
from num2words.lang_PT import Num2Word_PT


class Num2WordsPTTest(TestCase):
    def setUp(self):
        super(Num2WordsPTTest, self).setUp()
        self.n2w = Num2Word_PT()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='pt'), 'um')
        self.assertEqual(num2words(2, lang='pt'), 'dois')
        self.assertEqual(num2words(3, lang='pt'), 'três')
        self.assertEqual(num2words(4, lang='pt'), 'quatro')
        self.assertEqual(num2words(5, lang='pt'), 'cinco')
        self.assertEqual(num2words(6, lang='pt'), 'seis')
        self.assertEqual(num2words(7, lang='pt'), 'sete')
        self.assertEqual(num2words(8, lang='pt'), 'oito')
        self.assertEqual(num2words(9, lang='pt'), 'nove')
        self.assertEqual(num2words(10, lang='pt'), 'dez')
        self.assertEqual(num2words(11, lang='pt'), 'onze')
        self.assertEqual(num2words(12, lang='pt'), 'doze')
        self.assertEqual(num2words(13, lang='pt'), 'treze')
        self.assertEqual(num2words(14, lang='pt'), 'catorze')
        self.assertEqual(num2words(15, lang='pt'), 'quinze')
        self.assertEqual(num2words(16, lang='pt'), 'dezasseis')
        self.assertEqual(num2words(17, lang='pt'), 'dezassete')
        self.assertEqual(num2words(18, lang='pt'), 'dezoito')
        self.assertEqual(num2words(19, lang='pt'), 'dezanove')
        self.assertEqual(num2words(20, lang='pt'), 'vinte')

        self.assertEqual(num2words(21, lang='pt'), 'vinte e um')
        self.assertEqual(num2words(22, lang='pt'), 'vinte e dois')
        self.assertEqual(num2words(35, lang='pt'), 'trinta e cinco')
        self.assertEqual(num2words(99, lang='pt'), 'noventa e nove')

        self.assertEqual(num2words(100, lang='pt'), 'cem')
        self.assertEqual(num2words(101, lang='pt'), 'cento e um')
        self.assertEqual(num2words(128, lang='pt'), 'cento e vinte e oito')
        self.assertEqual(num2words(713, lang='pt'), 'setecentos e treze')

        self.assertEqual(num2words(1000, lang='pt'), 'mil')
        self.assertEqual(num2words(1001, lang='pt'), 'mil e um')
        self.assertEqual(num2words(1111, lang='pt'), 'mil cento e onze')
        self.assertEqual(
            num2words(2114, lang='pt'), 'dois mil cento e catorze'
        )
        self.assertEqual(
            num2words(2200, lang='pt'),
            'dois mil e duzentos'
        )
        self.assertEqual(
            num2words(2230, lang='pt'),
            'dois mil duzentos e trinta'
        )
        self.assertEqual(
            num2words(73400, lang='pt'),
            'setenta e três mil e quatrocentos'
        )
        self.assertEqual(
            num2words(73421, lang='pt'),
            'setenta e três mil quatrocentos e vinte e um'
        )
        self.assertEqual(num2words(100000, lang='pt'), 'cem mil')
        self.assertEqual(
            num2words(250050, lang='pt'),
            'duzentos e cinquenta mil e cinquenta'
        )
        self.assertEqual(
            num2words(6000000, lang='pt'), 'seis milhões'
        )
        self.assertEqual(
            num2words(100000000, lang='pt'), 'cem milhões'
        )
        self.assertEqual(
            num2words(19000000000, lang='pt'), 'dezanove mil milhões'
        )
        self.assertEqual(
            num2words(145000000002, lang='pt'),
            'cento e quarenta e cinco mil milhões e dois'
        )
        self.assertEqual(
            num2words(4635102, lang='pt'),
            'quatro milhões seiscentos e trinta e cinco mil cento e dois'
        )
        self.assertEqual(
            num2words(145254635102, lang='pt'),
            'cento e quarenta e cinco mil duzentos e cinquenta e quatro '
            'milhões seiscentos e trinta e cinco mil cento e dois'
        )
        self.assertEqual(
            num2words(1000000000000, lang='pt'),
            'um bilião'
        )
        self.assertEqual(
            num2words(2000000000000, lang='pt'),
            'dois biliões'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='pt'),
            'mil biliões'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='pt'),
            'dois mil biliões'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='pt'),
            'um trilião'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='pt'),
            'dois triliões'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='pt'), 'menos um')
        self.assertEqual(
            num2words(-256, lang='pt'), 'menos duzentos e cinquenta e seis'
        )
        self.assertEqual(num2words(-1000, lang='pt'), 'menos mil')
        self.assertEqual(num2words(-1000000, lang='pt'), 'menos um milhão')
        self.assertEqual(
            num2words(-1234567, lang='pt'),
            'menos um milhão duzentos e trinta e quatro mil quinhentos e '
            'sessenta e sete'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='pt'), 'um')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='pt'), 'um vírgula zero um')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='pt'), 'um vírgula zero três cinco'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='pt'), 'um vírgula três cinco'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='pt'),
            'três vírgula um quatro um cinco nove'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='pt'),
            'cento e um vírgula dois dois'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='pt'),
            'dois mil trezentos e quarenta e cinco vírgula sete cinco')

    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='pt'),
            'menos dois vírgula três quatro'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='pt'),
            'menos nove vírgula nove nove'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='pt'),
            'menos sete vírgula zero um'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='pt'),
            'menos duzentos e vinte e dois vírgula dois dois'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='pt', ordinal=True), 'primeiro')
        self.assertEqual(num2words(2, lang='pt', ordinal=True), 'segundo')
        self.assertEqual(num2words(3, lang='pt', ordinal=True), 'terceiro')
        self.assertEqual(num2words(4, lang='pt', ordinal=True), 'quarto')
        self.assertEqual(num2words(5, lang='pt', ordinal=True), 'quinto')
        self.assertEqual(num2words(6, lang='pt', ordinal=True), 'sexto')
        self.assertEqual(num2words(7, lang='pt', ordinal=True), 'sétimo')
        self.assertEqual(num2words(8, lang='pt', ordinal=True), 'oitavo')
        self.assertEqual(num2words(9, lang='pt', ordinal=True), 'nono')
        self.assertEqual(num2words(10, lang='pt', ordinal=True), 'décimo')
        self.assertEqual(
            num2words(11, lang='pt', ordinal=True), 'décimo primeiro'
        )
        self.assertEqual(
            num2words(12, lang='pt', ordinal=True), 'décimo segundo'
        )
        self.assertEqual(
            num2words(13, lang='pt', ordinal=True), 'décimo terceiro'
        )
        self.assertEqual(
            num2words(14, lang='pt', ordinal=True), 'décimo quarto'
        )
        self.assertEqual(
            num2words(15, lang='pt', ordinal=True), 'décimo quinto'
        )
        self.assertEqual(
            num2words(16, lang='pt', ordinal=True), 'décimo sexto'
        )
        self.assertEqual(
            num2words(17, lang='pt', ordinal=True), 'décimo sétimo'
        )
        self.assertEqual(
            num2words(18, lang='pt', ordinal=True), 'décimo oitavo'
        )
        self.assertEqual(
            num2words(19, lang='pt', ordinal=True), 'décimo nono'
        )
        self.assertEqual(
            num2words(20, lang='pt', ordinal=True), 'vigésimo'
        )

        self.assertEqual(
            num2words(21, lang='pt', ordinal=True), 'vigésimo primeiro'
        )
        self.assertEqual(
            num2words(22, lang='pt', ordinal=True), 'vigésimo segundo'
        )
        self.assertEqual(
            num2words(35, lang='pt', ordinal=True), 'trigésimo quinto'
        )
        self.assertEqual(
            num2words(99, lang='pt', ordinal=True), 'nonagésimo nono'
        )

        self.assertEqual(
            num2words(100, lang='pt', ordinal=True), 'centésimo'
        )
        self.assertEqual(
            num2words(101, lang='pt', ordinal=True), 'centésimo primeiro'
        )
        self.assertEqual(
            num2words(128, lang='pt', ordinal=True),
            'centésimo vigésimo oitavo'
        )
        self.assertEqual(
            num2words(713, lang='pt', ordinal=True),
            'septigentésimo décimo terceiro'
        )

        self.assertEqual(
            num2words(1000, lang='pt', ordinal=True), 'milésimo'
        )
        self.assertEqual(
            num2words(1001, lang='pt', ordinal=True), 'milésimo primeiro'
        )
        self.assertEqual(
            num2words(1111, lang='pt', ordinal=True),
            'milésimo centésimo décimo primeiro'
        )
        self.assertEqual(
            num2words(2114, lang='pt', ordinal=True),
            'segundo milésimo centésimo décimo quarto'
        )
        self.assertEqual(
            num2words(73421, lang='pt', ordinal=True),
            'septuagésimo terceiro milésimo quadrigentésimo vigésimo primeiro'
        )

        self.assertEqual(
            num2words(100000, lang='pt', ordinal=True),
            'centésimo milésimo'
        )
        self.assertEqual(
            num2words(250050, lang='pt', ordinal=True),
            'ducentésimo quinquagésimo milésimo quinquagésimo'
        )
        self.assertEqual(
            num2words(6000000, lang='pt', ordinal=True), 'sexto milionésimo'
        )
        self.assertEqual(
            num2words(19000000000, lang='pt', ordinal=True),
            'décimo nono milésimo milionésimo'
        )
        self.assertEqual(
            num2words(145000000002, lang='pt', ordinal=True),
            'centésimo quadragésimo quinto milésimo milionésimo segundo'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'um euro')
        self.assertEqual(self.n2w.to_currency(2.00), 'dois euros')
        self.assertEqual(self.n2w.to_currency(3.00), 'três euros')
        self.assertEqual(self.n2w.to_currency(4.00), 'quatro euros')
        self.assertEqual(self.n2w.to_currency(5.00), 'cinco euros')
        self.assertEqual(self.n2w.to_currency(6.00), 'seis euros')
        self.assertEqual(self.n2w.to_currency(7.00), 'sete euros')
        self.assertEqual(self.n2w.to_currency(8.00), 'oito euros')
        self.assertEqual(self.n2w.to_currency(9.00), 'nove euros')
        self.assertEqual(self.n2w.to_currency(10.00), 'dez euros')
        self.assertEqual(self.n2w.to_currency(11.00), 'onze euros')
        self.assertEqual(self.n2w.to_currency(12.00), 'doze euros')
        self.assertEqual(self.n2w.to_currency(13.00), 'treze euros')
        self.assertEqual(self.n2w.to_currency(14.00), 'catorze euros')
        self.assertEqual(self.n2w.to_currency(15.00), 'quinze euros')
        self.assertEqual(self.n2w.to_currency(16.00), 'dezasseis euros')
        self.assertEqual(self.n2w.to_currency(17.00), 'dezassete euros')
        self.assertEqual(self.n2w.to_currency(18.00), 'dezoito euros')
        self.assertEqual(self.n2w.to_currency(19.00), 'dezanove euros')
        self.assertEqual(self.n2w.to_currency(20.00), 'vinte euros')

        self.assertEqual(self.n2w.to_currency(21.00), 'vinte e um euros')
        self.assertEqual(self.n2w.to_currency(22.00), 'vinte e dois euros')
        self.assertEqual(self.n2w.to_currency(35.00), 'trinta e cinco euros')
        self.assertEqual(self.n2w.to_currency(99.00), 'noventa e nove euros')

        self.assertEqual(self.n2w.to_currency(100.00), 'cem euros')
        self.assertEqual(self.n2w.to_currency(101.00), 'cento e um euros')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'cento e vinte e oito euros'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'setecentos e treze euros')

        self.assertEqual(self.n2w.to_currency(1000.00), 'mil euros')
        self.assertEqual(self.n2w.to_currency(1001.00), 'mil e um euros')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'mil cento e onze euros')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dois mil cento e catorze euros'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'setenta e três mil quatrocentos e vinte e um euros'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'cem mil euros')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'duzentos e cinquenta mil e cinquenta euros'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00), 'seis milhões de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dezanove mil milhões de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'cento e quarenta e cinco mil milhões e dois euros'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'um dólar')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'um dólar e cinquenta cêntimos')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menos um euro')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menos duzentos e cinquenta e seis euros'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menos mil euros')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menos um milhão de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menos um milhão duzentos e trinta e quatro mil quinhentos e '
            'sessenta e sete euros'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'um euro')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'um euro e um cêntimo'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'um euro e três cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'um euro e trinta e cinco cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'três euros e catorze cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'cento e um euros e vinte e dois cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dois mil trezentos e quarenta e cinco euros e setenta e cinco '
            'cêntimos'
        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menos dois euros e trinta e quatro cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menos nove euros e noventa e nove cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menos sete euros e um cêntimo'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menos duzentos e vinte e dois euros e vinte e dois cêntimos'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'mil e um')
        self.assertEqual(
            self.n2w.to_year(1789), 'mil setecentos e oitenta e nove'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'mil novecentos e quarenta e dois'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'mil novecentos e oitenta e quatro'
        )
        self.assertEqual(self.n2w.to_year(2000), 'dois mil')
        self.assertEqual(self.n2w.to_year(2001), 'dois mil e um')
        self.assertEqual(self.n2w.to_year(2016), 'dois mil e dezasseis')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'trinta antes de Cristo')
        self.assertEqual(
            self.n2w.to_year(-744),
            'setecentos e quarenta e quatro antes de Cristo'
        )
        self.assertEqual(self.n2w.to_year(-10000), 'dez mil antes de Cristo')

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
