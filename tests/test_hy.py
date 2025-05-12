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


class Num2WordsHYTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(0, lang='hy'), 'զրո')
        self.assertEqual(num2words(1, lang='hy'), 'մեկ')
        self.assertEqual(num2words(2, lang='hy'), 'երկու')
        self.assertEqual(num2words(3, lang='hy'), 'երեք')
        self.assertEqual(num2words(5, lang='hy'), 'հինգ')
        self.assertEqual(num2words(9, lang='hy'), 'ինը')
        self.assertEqual(num2words(10, lang='hy'), 'տասը')
        self.assertEqual(num2words(11, lang='hy'), 'տասնմեկ')
        self.assertEqual(num2words(12, lang='hy'), 'տասներկու')
        self.assertEqual(num2words(15, lang='hy'), 'տասնհինգ')
        self.assertEqual(num2words(19, lang='hy'), 'տասնինը')
        self.assertEqual(num2words(20, lang='hy'), 'քսան')
        self.assertEqual(num2words(21, lang='hy'), 'քսան մեկ')
        self.assertEqual(num2words(30, lang='hy'), 'երեսուն')
        self.assertEqual(num2words(50, lang='hy'), 'հիսուն')
        self.assertEqual(num2words(99, lang='hy'), 'իննսուն ինը')
        self.assertEqual(num2words(100, lang='hy'), 'հարյուր')
        self.assertEqual(num2words(101, lang='hy'), 'հարյուր մեկ')
        self.assertEqual(num2words(111, lang='hy'), 'հարյուր տասնմեկ')
        self.assertEqual(num2words(120, lang='hy'), 'հարյուր քսան')
        self.assertEqual(num2words(200, lang='hy'), 'երկու հարյուր')
        self.assertEqual(num2words(999, lang='hy'), 'ինը հարյուր իննսուն ինը')
        self.assertEqual(num2words(1000, lang='hy'), 'հազար')
        self.assertEqual(num2words(1001, lang='hy'), 'հազար մեկ')
        self.assertEqual(num2words(1111, lang='hy'), 'հազար հարյուր տասնմեկ')
        self.assertEqual(num2words(2000, lang='hy'), 'երկու հազար')
        self.assertEqual(num2words(10000, lang='hy'), 'տասը հազար')
        self.assertEqual(num2words(100000, lang='hy'), 'հարյուր հազար')
        self.assertEqual(num2words(1000000, lang='hy'), 'մեկ միլիոն')
        self.assertEqual(num2words(2000000, lang='hy'), 'երկու միլիոն')
        self.assertEqual(num2words(1000000000, lang='hy'), 'մեկ միլիարդ')

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='hy', to='ordinal'), 'առաջին')
        self.assertEqual(num2words(2, lang='hy', to='ordinal'), 'երկրորդ')
        self.assertEqual(num2words(3, lang='hy', to='ordinal'), 'երրորդ')
        self.assertEqual(num2words(5, lang='hy', to='ordinal'), 'հինգերորդ')
        self.assertEqual(num2words(9, lang='hy', to='ordinal'), 'իններորդ')
        self.assertEqual(num2words(10, lang='hy', to='ordinal'), 'տասներորդ')
        self.assertEqual(
            num2words(11, lang='hy', to='ordinal'),
            'տասնմեկերորդ'
        )
        self.assertEqual(
            num2words(12, lang='hy', to='ordinal'),
            'տասներկուերորդ'
        )
        self.assertEqual(num2words(20, lang='hy', to='ordinal'), 'քսաներորդ')
        self.assertEqual(num2words(21, lang='hy', to='ordinal'), 'քսան առաջին')
        self.assertEqual(
            num2words(101, lang='hy', to='ordinal'),
            'հարյուր մեկերորդ'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(1, lang='hy', to='ordinal_num'), '1-րդ')
        self.assertEqual(num2words(2, lang='hy', to='ordinal_num'), '2-րդ')
        self.assertEqual(num2words(10, lang='hy', to='ordinal_num'), '10-րդ')

    def test_currency(self):
        self.assertEqual(
            num2words(1.0, lang='hy', to='currency', currency='AMD'),
            'մեկ դրամ'
        )
        self.assertEqual(
            num2words(2.0, lang='hy', to='currency', currency='AMD'),
            'երկու դրամ'
        )
        self.assertEqual(
            num2words(1.5, lang='hy', to='currency', currency='USD'),
            'մեկ դոլար ամբողջ հինգ տասներորդ ցենտ'
        )
        self.assertEqual(
            num2words(100.0, lang='hy', to='currency', currency='EUR'),
            'հարյուր եվրո'
        )

    def test_year(self):
        self.assertEqual(
            num2words(2020, lang='hy', to='year'),
            'երկու հազար քսան թվական'
        )
        self.assertEqual(
            num2words(1990, lang='hy', to='year'),
            'հազար ինը հարյուր իննսուն թվական'
        )
        self.assertEqual(
            num2words(-44, lang='hy', to='year'),
            'քառասուն չորս թվականից առաջ'
        )
