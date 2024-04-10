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
from unittest import TestCase, skip

from num2words import num2words
from num2words.lang_MGM_NC import Num2Word_MGM_NC


class Num2WordsMGMTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_MGM_NC()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='mgm'), 'id')
        self.assertEqual(num2words(2, lang='mgm'), 'ru')
        self.assertEqual(num2words(3, lang='mgm'), 'teil')
        self.assertEqual(num2words(4, lang='mgm'), 'pat')
        self.assertEqual(num2words(5, lang='mgm'), 'lim')
        self.assertEqual(num2words(6, lang='mgm'), 'hohonid')
        self.assertEqual(num2words(7, lang='mgm'), 'hohoru')
        self.assertEqual(num2words(8, lang='mgm'), 'hohoteil')
        self.assertEqual(num2words(9, lang='mgm'), 'hohopat')
        self.assertEqual(num2words(10, lang='mgm'), 'sagul')
        self.assertEqual(num2words(11, lang='mgm'), 'sagul resi id')
        self.assertEqual(num2words(12, lang='mgm'), 'sagul resi ru')
        self.assertEqual(num2words(13, lang='mgm'), 'sagul resi teil')
        self.assertEqual(num2words(14, lang='mgm'), 'sagul resi pat')
        self.assertEqual(num2words(15, lang='mgm'), 'sagul resi lim')
        self.assertEqual(num2words(16, lang='mgm'), 'sagul resi hohonid')
        self.assertEqual(num2words(17, lang='mgm'), 'sagul resi hohoru')
        self.assertEqual(num2words(18, lang='mgm'), 'sagul resi hohoteil')
        self.assertEqual(num2words(19, lang='mgm'), 'sagul resi hohopat')
        self.assertEqual(num2words(20, lang='mgm'), 'gulru')

        self.assertEqual(num2words(21, lang='mgm'), 'gulru resi id')
        self.assertEqual(num2words(22, lang='mgm'), 'gulru resi ru')
        self.assertEqual(num2words(35, lang='mgm'), 'gulteil resi lim')
        self.assertEqual(num2words(99, lang='mgm'), 'gulhohopat resi hohopat')

        self.assertEqual(num2words(100, lang='mgm'), 'atusid id')
        self.assertEqual(num2words(101, lang='mgm'), 'atusid id resi id')
        self.assertEqual(num2words(107, lang='mgm'), 'atusid id resi hohoru')
        self.assertEqual(num2words(110, lang='mgm'), 'atusid id sagul')
        self.assertEqual(num2words(114, lang='mgm'), 'atusid id sagul resi pat')
        self.assertEqual(num2words(128, lang='mgm'), 'atusid id gulru resi hohoteil')
        self.assertEqual(num2words(151, lang='mgm'), 'atusid id gullim resi id')
        self.assertEqual(num2words(713, lang='mgm'), 'atusid hohoru sagul resi teil')
        self.assertEqual(num2words(999, lang='mgm'), 'atusid hohopat gulhohopat resi hohopat')

        self.assertEqual(num2words(1000, lang='mgm'), 'rihunid id')
        self.assertEqual(num2words(1001, lang='mgm'), 'rihunid id resi id')
        self.assertEqual(num2words(1011, lang='mgm'), 'rihunid id sagul resi id')
        self.assertEqual(num2words(1111, lang='mgm'), 'rihunid id atusid id sagul resi id')
        self.assertEqual(num2words(2357, lang='mgm'), 'rihunid ru atusid teil gullim resi hohoru')
        self.assertEqual(
            num2words(2200, lang='mgm'),
            'rihunid ru atusid ru'
        )
        self.assertEqual(num2words(2230, lang='mgm'), 'rihunid ru atusid ru gulteil')
        self.assertEqual(num2words(73400, lang='mgm'), 'rihunid gulhohoru resi teil atusid pat')
        self.assertEqual(num2words(73421, lang='mgm'), 'rihunid gulhohoru resi teil atusid pat gulru resi id')
        self.assertEqual(num2words(100000, lang='mgm'), 'rihunid atusid id')
        self.assertEqual(num2words(250050, lang='mgm'), 'rihunid atusid ru gullim gullim')
        self.assertEqual(
            num2words(6000000, lang='mgm'), 'miliaunid hohonid'
        )
        self.assertEqual(
            num2words(100000000, lang='mgm'), 'miliaunid atusid id'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm'), 'miliaunid rihunid sagul resi hohopat'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm'),
            'miliaunid rihunid atusid id gulpat resi lim resi ru'
        )
        self.assertEqual(
            num2words(4635102, lang='mgm'),
            'miliaunid pat rihunid atusid hohonid gulteil resi lim atusid id resi ru'
        )
        self.assertEqual(
            num2words(145254635102, lang='mgm'),
            'miliaunid rihunid atusid id gulpat resi lim atusid ru gullim resi pat rihunid atusid hohonid gulteil resi lim atusid id resi ru'
        )
        self.assertEqual(
            num2words(1000000000000, lang='mgm'),
            'biliaunid id'
        )
        self.assertEqual(
            num2words(2000000000000, lang='mgm'),
            'biliaunid ru'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='mgm'),
            'biliaunid rihunid id'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='mgm'),
            'biliaunid rihunid ru'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='mgm'),
            'triliaunid id'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='mgm'),
            'triliaunid ru'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='mgm'), 'menus id')
        self.assertEqual(
            num2words(-256, lang='mgm'), 'menus atusid ru gullim resi hohonid'
        )
        self.assertEqual(num2words(-1000, lang='mgm'), 'menus rihunid id')
        self.assertEqual(num2words(-1000000, lang='mgm'), 'menus miliaunid id')
        self.assertEqual(
            num2words(-1234567, lang='mgm'),
            'menus miliaunid id rihunid atusid ru gulteil resi pat atusid lim gulhohonid resi hohoru'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='mgm'), 'id')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='mgm'), 'id vírgula mamu id')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='mgm'), 'id vírgula mamu teil lim'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='mgm'), 'id vírgula teil lim'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='mgm'),
            'teil vírgula id pat id lim hohopat'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='mgm'),
            'atusid id resi id vírgula ru ru'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='mgm'),
            'rihunid ru atusid teil gulpat resi lim vírgula hohoru lim'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='mgm'),
            'menus ru vírgula teil pat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='mgm'),
            'menus hohopat vírgula hohopat hohopat'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='mgm'),
            'menus hohoru vírgula mamu id'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='mgm'),
            'menus atusid ru gulru resi ru vírgula ru ru'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='mgm', ordinal=True), 'primeir')
        self.assertEqual(num2words(2, lang='mgm', ordinal=True), 'segund')
        self.assertEqual(num2words(3, lang='mgm', ordinal=True), 'terceir')
        self.assertEqual(num2words(4, lang='mgm', ordinal=True), 'quart')
        self.assertEqual(num2words(5, lang='mgm', ordinal=True), 'quint')
        self.assertEqual(num2words(6, lang='mgm', ordinal=True), 'sext')
        self.assertEqual(num2words(7, lang='mgm', ordinal=True), 'sétim')
        self.assertEqual(num2words(8, lang='mgm', ordinal=True), 'oitav')
        self.assertEqual(num2words(9, lang='mgm', ordinal=True), 'non')
        self.assertEqual(num2words(10, lang='mgm', ordinal=True), 'décim')
        self.assertEqual(
            num2words(11, lang='mgm', ordinal=True), 'décim primeir'
        )
        self.assertEqual(
            num2words(12, lang='mgm', ordinal=True), 'décim segund'
        )
        self.assertEqual(
            num2words(13, lang='mgm', ordinal=True), 'décim terceir'
        )
        self.assertEqual(
            num2words(14, lang='mgm', ordinal=True), 'décim quart'
        )
        self.assertEqual(
            num2words(15, lang='mgm', ordinal=True), 'décim quint'
        )
        self.assertEqual(
            num2words(16, lang='mgm', ordinal=True), 'décim sext'
        )
        self.assertEqual(
            num2words(17, lang='mgm', ordinal=True), 'décim sétim'
        )
        self.assertEqual(
            num2words(18, lang='mgm', ordinal=True), 'décim oitav'
        )
        self.assertEqual(
            num2words(19, lang='mgm', ordinal=True), 'décim non'
        )
        self.assertEqual(
            num2words(20, lang='mgm', ordinal=True), 'vigésim'
        )

        self.assertEqual(
            num2words(21, lang='mgm', ordinal=True), 'vigésim primeir'
        )
        self.assertEqual(
            num2words(22, lang='mgm', ordinal=True), 'vigésim segund'
        )
        self.assertEqual(
            num2words(35, lang='mgm', ordinal=True), 'trigésim quint'
        )
        self.assertEqual(
            num2words(99, lang='mgm', ordinal=True), 'nonagésim non'
        )

        self.assertEqual(
            num2words(100, lang='mgm', ordinal=True), 'centésim'
        )
        self.assertEqual(
            num2words(101, lang='mgm', ordinal=True), 'centésim primeir'
        )
        self.assertEqual(
            num2words(128, lang='mgm', ordinal=True),
            'centésim vigésim oitav'
        )
        self.assertEqual(
            num2words(713, lang='mgm', ordinal=True),
            'septigentésim décim terceir'
        )

        self.assertEqual(
            num2words(1000, lang='mgm', ordinal=True), 'milésim'
        )
        self.assertEqual(
            num2words(1001, lang='mgm', ordinal=True), 'milésim primeir'
        )
        self.assertEqual(
            num2words(1111, lang='mgm', ordinal=True),
            'milésim centésim décim primeir'
        )
        self.assertEqual(
            num2words(2114, lang='mgm', ordinal=True),
            'segund milésim centésim décim quart'
        )
        self.assertEqual(
            num2words(73421, lang='mgm', ordinal=True),
            'septuagésim terceir milésim quadrigentésim vigésim primeir'
        )

        self.assertEqual(
            num2words(100000, lang='mgm', ordinal=True),
            'centésim milésim'
        )
        self.assertEqual(
            num2words(250050, lang='mgm', ordinal=True),
            'ducentésim quinquagésim milésim quinquagésim'
        )
        self.assertEqual(
            num2words(6000000, lang='mgm', ordinal=True), 'sext milionésim'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm', ordinal=True),
            'décim non milésim milionésim'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm', ordinal=True),
            'centésim quadragésim quint milésim milionésim segund'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'id dólar')
        self.assertEqual(self.n2w.to_currency(2.00), 'ru dólares')
        self.assertEqual(self.n2w.to_currency(3.00), 'teil dólares')
        self.assertEqual(self.n2w.to_currency(4.00), 'pat dólares')
        self.assertEqual(self.n2w.to_currency(5.00), 'lim dólares')
        self.assertEqual(self.n2w.to_currency(6.00), 'hohonid dólares')
        self.assertEqual(self.n2w.to_currency(7.00), 'hohoru dólares')
        self.assertEqual(self.n2w.to_currency(8.00), 'hohoteil dólares')
        self.assertEqual(self.n2w.to_currency(9.00), 'hohopat dólares')
        self.assertEqual(self.n2w.to_currency(10.00), 'sagul dólares')
        self.assertEqual(self.n2w.to_currency(11.00), 'sagul resi id dólares')
        self.assertEqual(self.n2w.to_currency(12.00), 'sagul resi ru dólares')
        self.assertEqual(self.n2w.to_currency(13.00), 'sagul resi teil dólares')
        self.assertEqual(self.n2w.to_currency(14.00), 'sagul resi pat dólares')
        self.assertEqual(self.n2w.to_currency(15.00), 'sagul resi lim dólares')
        self.assertEqual(self.n2w.to_currency(16.00), 'sagul resi hohonid dólares')
        self.assertEqual(self.n2w.to_currency(17.00), 'sagul resi hohoru dólares')
        self.assertEqual(self.n2w.to_currency(18.00), 'sagul resi hohoteil dólares')
        self.assertEqual(self.n2w.to_currency(19.00), 'sagul resi hohopat dólares')
        self.assertEqual(self.n2w.to_currency(20.00), 'gulru dólares')

        self.assertEqual(self.n2w.to_currency(21.00), 'gulru resi id dólares')
        self.assertEqual(self.n2w.to_currency(22.00), 'gulru resi ru dólares')
        self.assertEqual(self.n2w.to_currency(35.00), 'gulteil resi lim dólares')
        self.assertEqual(self.n2w.to_currency(99.00), 'gulhohopat resi hohopat dólares')

        self.assertEqual(self.n2w.to_currency(100.00), 'atusid id dólares')
        self.assertEqual(self.n2w.to_currency(101.00), 'atusid id resi id dólares')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'atusid id gulru resi hohoteil dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'atusid hohoru sagul resi teil dólares')

        self.assertEqual(self.n2w.to_currency(1000.00), 'rihunid id dólares')
        self.assertEqual(self.n2w.to_currency(1001.00), 'rihunid id resi id dólares')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'rihunid id atusid id sagul resi id dólares')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'rihunid ru atusid id sagul resi pat dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'rihunid gulhohoru resi teil atusid pat gulru resi id dólares'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'rihunid atusid id dólares')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'rihunid atusid ru gullim gullim dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'miliaunid hohonid dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'miliaunid rihunid sagul resi hohopat dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'miliaunid rihunid atusid id gulpat resi lim resi ru dólares'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'id dólar')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'id dólar resi gullim cêntimus')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus id dólar')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus atusid ru gullim resi hohonid dólares'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus rihunid id dólares')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus miliaunid id dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus miliaunid id rihunid atusid ru gulteil resi pat atusid lim gulhohonid resi hohoru dólares'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'id dólar')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'id dólar resi id cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'id dólar resi teil cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'id dólar resi gulteil resi lim cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'teil dólares resi sagul resi pat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'atusid id resi id dólares resi gulru resi ru cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'rihunid ru atusid teil gulpat resi lim dólares resi gulhohoru resi lim cêntimus'

        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus ru dólares resi gulteil resi pat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus hohopat dólares resi gulhohopat resi hohopat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus hohoru dólares resi id cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus atusid ru gulru resi ru dólares resi gulru resi ru cêntimus'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihunid id resi id')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihunid id atusid hohoru gulhohoteil resi hohopat'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihunid id atusid hohopat gulpat resi ru'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihunid id atusid hohopat gulhohoteil resi pat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihunid ru')
        self.assertEqual(self.n2w.to_year(2001), 'rihunid ru resi id')
        self.assertEqual(self.n2w.to_year(2016), 'rihunid ru sagul resi hohonid')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'gulteil muna Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atusid hohoru gulpat resi pat muna Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'rihunid sagul muna Kristu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
