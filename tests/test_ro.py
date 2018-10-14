# -*- encoding: utf-8 -*-
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

from unittest import TestCase

from num2words import num2words


class Num2WordsROTest(TestCase):

    def test_ordinal(self):
        self.assertEqual(
            num2words(1, lang='ro', to='ordinal'),
            'primul'  # poate si intaiul
        )
        self.assertEqual(
            num2words(22, lang='ro', to='ordinal'),
            u'al douăzeci și doilea'
        )
        self.assertEqual(
            num2words(21, lang='ro', to='ordinal'),
            u'al douăzeci și unulea'
        )
        self.assertEqual(
            num2words(12, lang='ro', to='ordinal'),
            u'al doisprezecelea'
        )
        self.assertEqual(
            num2words(130, lang='ro', to='ordinal'),
            u'al o sută treizecilea'
        )
        self.assertEqual(
            num2words(1003, lang='ro', to='ordinal'),
            u'al o mie treilea'
        )

    def test_ordinal_num(self):
        self.assertEqual(
            num2words(1, lang='ro', to='ordinal_num'),
            '1-ul'
        )
        self.assertEqual(
            num2words(10, lang='ro', to='ordinal_num'),
            'al 10-lea'
        )
        self.assertEqual(num2words(
            21, lang='ro', to='ordinal_num'),
            'al 21-lea'
        )
        self.assertEqual(
            num2words(102, lang='ro', to='ordinal_num'),
            'al 102-lea'
        )
        self.assertEqual(
            num2words(73, lang='ro', to='ordinal_num'),
            'al 73-lea'
        )

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            num2words(12.5, lang='ro'),
            u'doisprezece virgulă cinci'
        )
        self.assertEqual(
            num2words(12.51, lang='ro'),
            u'doisprezece virgulă cinci unu'
        )
        self.assertEqual(
            num2words(12.53, lang='ro'),
            u'doisprezece virgulă cinci trei'
        )
        self.assertEqual(
            num2words(12.59, lang='ro'),
            u'doisprezece virgulă cinci nouă'
        )

    # def test_big_numbers(self):
    #     import pdb; pdb.set_trace()
    #     self.assertEqual(
    #         num2words(1000000),
    #         "un milion"
    #     )
    #     self.assertEqual(
    #         num2words(1000000000),
    #         "un miliard"
    #     )
    #     self.assertEqual(
    #         num2words(33000000),
    #         "treizeci și trei de milioane"
    #     )
    #     self.assertEqual(
    #         num2words(247000000000),
    #         "două sute patruzeci și șapte de miliarde"
    #     )

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("100000000000000000000000000000000000000000000000000000"
                      "000000000000000000000000000000000000000000000000000000"
                      "000000000000000000000000000000000000000000000000000000"
                      "000000000000000000000000000000000000000000000000000000"
                      "000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000")

    def test_to_currency(self):
        self.assertEqual(
            num2words(38.4, lang='ro', to='currency'),
            u"treizeci și opt de lei și patruzeci de bani"
        )

        # self.assertEqual(
        #     num2words(1.01, lang='ro', to='currency'),
        #     "un leu și un ban"
        # )

        # self.assertEqual(
        #     num2words(4778.00, lang='ro', to='currency'),
        #     'patru mii șapte sute șaptezeci și opt de lei')

        # self.assertEqual(
        #     num2words(4778.32, lang='ro', to='currency'),
        #     'patru mii șapte sute șaptezeci și opt de lei'
        #     ' și treizeci și doi de bani')

    # def test_to_year(self):
    #     self.assertEqual(num2words(1989, lang='ro', to='year'),
    #                      'o mie nouă sute optzeci și nouă')
    #     self.assertEqual(num2words(1984, lang='ro', to='year'),
    #                      'o mie nouă sute optzeci și patru')
    #     self.assertEqual(num2words(2018, lang='ro', to='year'),
    #                      'două mii optsprezece')
    #     self.assertEqual(num2words(1066, lang='ro', to='year'),
    #                      'o mie șaizeci și șase')
    #     self.assertEqual(num2words(5000, lang='ro', to='year'),
    #                      'cinci mii')
    #     self.assertEqual(num2words(2001, lang='ro', to='year'),
    #                      'două mii unu')
    #     self.assertEqual(num2words(905, lang='ro', to='year'),
    #                      'nouă sute cinci')
    #     self.assertEqual(num2words(6600, lang='ro', to='year'),
    #                      'șase mii șase sute')
    #     self.assertEqual(num2words(1600, lang='ro', to='year'),
    #                      'o mie sase sute')
    #     self.assertEqual(num2words(700, lang='ro', to='year'),
    #                      'șapte sute')
    #     self.assertEqual(num2words(50, lang='ro', to='year'),
    #                      'cincizeci')
    #     self.assertEqual(num2words(0, lang='ro', to='year'),
    #                      'zero')
    #     # suffixes
    #     self.assertEqual(num2words(-44, lang='ro', to='year'),
    #                      'patruzeci și patru î.Hr.')
    #     self.assertEqual(num2words(-44, lang='ro', to='year',),
    #                      suffix='î.e.n.', 'patruzeci și patru î.e.n.')
    #     self.assertEqual(num2words(1, lang='ro', to='year', suffix='d.Hr.'),
    #                      'unu d.Hr.')
    #     self.assertEqual(num2words(-66000000, lang='ro', to='year'),
    #                      'șaizeci și șase milioane î.Hr.')
