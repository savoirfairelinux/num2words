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

from unittest import TestCase

from num2words import num2words


class Num2WordsENTest(TestCase):
    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='dv', to='ordinal'),
            'ސުން ވަނަ'
        )
        self.assertEqual(
            num2words(1, lang='dv', to='ordinal'),
            'އެއް ވަނަ'
        )
        self.assertEqual(
            num2words(13, lang='dv', to='ordinal'),
            'ތޭރަ ވަނަ'
        )
        self.assertEqual(
            num2words(22, lang='dv', to='ordinal'),
            'ބާވީސް ވަނަ'
        )
        self.assertEqual(
            num2words(12, lang='dv', to='ordinal'),
            'ބާރަ ވަނަ'
        )
        self.assertEqual(
            num2words(130, lang='dv', to='ordinal'),
            'ސަތޭކަތިރީސް ވަނަ'
        )
        self.assertEqual(
            num2words(1003, lang='dv', to='ordinal'),
            'އެއްހާސް ތިން ވަނަ'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='dv', to='ordinal_num'), '10 ވަނަ')

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            num2words(12.5, lang='dv'),
            "ބާރަ ޕޮއިންޓް ފަހެއް"
        )
        self.assertEqual(
            num2words(12.51, lang='dv'),
            "ބާރަ ޕޮއިންޓް ފަހެއް އެކެއް"
        )
        self.assertEqual(
            num2words(12.53, lang='dv'),
            "ބާރަ ޕޮއިންޓް ފަހެއް ތިނެއް"
        )
        self.assertEqual(
            num2words(12.583824, lang='dv'),
            "ބާރަ ޕޮއިންޓް ފަހެއް އަށެއް ތިނެއް އަށެއް ދޭއް ހަތަރެއް"
        )

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000", lang='dv')

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='dv', to='currency'),
            "ތިރީސްއައް ރުފިޔާ ސާޅީސް ލާރި"
        )
        self.assertEqual(
            num2words('0', lang='dv', to='currency'),
            "ސުން ރުފިޔާ"
        )

        self.assertEqual(
            num2words('.01', lang='dv', to='currency'),
            "އެއް ލާރި"
        )

        self.assertEqual(
            num2words('43.23212', lang='dv', to='currency'),
            "ސާޅީސްތިން ރުފިޔާ ތޭވީސް ލާރި"
        )

        self.assertEqual(
            num2words('100000000', lang='dv', to='currency'),
            "ސަތޭކަމިލިޔަން ރުފިޔާ"
        )

    def test_to_year(self):
        # issue 141
        # "e2 e2"
        self.assertEqual(num2words(1990, lang='dv', to='year'),
                         'ނަވާރަ ސަތޭކަ ނުވަދިހަ')
        self.assertEqual(num2words(5555, lang='dv', to='year'),
                         'ފަސްހާސް ފަސްސަތޭކަ ފަންސާސްފަހެއް')
        self.assertEqual(num2words(2017, lang='dv', to='year'),
                         'ދެހާސް ސަތާރަ')
        self.assertEqual(num2words(1066, lang='dv', to='year'),
                         'އެއްހާސް ފަސްދޮޅަސްހައެއް')
        self.assertEqual(num2words(1166, lang='dv', to='year'),
                         'އެގާރަ ސަތޭކަ ފަސްދޮޅަސްހައެއް')
        self.assertEqual(num2words(1865, lang='dv', to='year'),
                         'އަށާރަ ސަތޭކަ ފަސްދޮޅަސްފަހެއް')
        self.assertEqual(num2words(1, lang='dv', to='year', suffix='އޭ.ޑީ'),
                         "އެކެއް އޭ.ޑީ")
        self.assertEqual(num2words(-44, lang='dv', to='year'),
                         'ސާޅީސްހަތަރެއް ބީ.ސީ')
        self.assertEqual(num2words(-66000000, lang='dv', to='year'),
                         'ފަސްދޮޅަސްހަމިލިޔަން ބީ.ސީ')
