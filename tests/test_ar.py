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
# from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsARTest(TestCase):

    def test_default_currency(self):
        self.assertEqual(num2words(1, to='currency', lang='ar'), 'واحد ريال')
        self.assertEqual(num2words(10, to='currency', lang='ar'),
                         'عشرة ريالات')
        self.assertEqual(num2words(100, to='currency', lang='ar'), 'مائة ريال')
        self.assertEqual(num2words(324, to='currency', lang='ar'),
                         'ثلاثمائة و أربعة و عشرون ريالاً')
        self.assertEqual(num2words(2000, to='currency', lang='ar'),
                         'ألفا ريال')
        self.assertEqual(num2words(541, to='currency', lang='ar'),
                         'خمسمائة و واحد و أربعون ريالاً')
        self.assertEqual(num2words(10000, to='currency', lang='ar'),
                         'عشرة آلاف ريال')
        self.assertEqual(num2words(20000.12, to='currency', lang='ar'),
                         'عشرون ألف ريال و اثنتا عشرة هللة')
        self.assertEqual(num2words(1000000, to='currency', lang='ar'),
                         'واحد مليون ريال')
        value = "تسعمائة و ثلاثة و عشرون ألفاً  و أربعمائة و أحد عشر ريالاً"
        self.assertEqual(num2words(923411, to='currency', lang='ar'), value)
        self.assertEqual(num2words(63411, to='currency', lang='ar'),
                         'ثلاثة و ستون ألفاً  و أربعمائة و أحد عشر ريالاً')
        self.assertEqual(num2words(1000000.99, to='currency', lang='ar'),
                         'واحد مليون ريال و تسع و تسعون هللة')

    def test_currency_parm(self):
        self.assertEqual(
            num2words(1, to='currency', lang='ar', currency="KWD"),
            'واحد دينار')
        self.assertEqual(
            num2words(10, to='currency', lang='ar', currency="EGP"),
            'عشرة جنيهات')
        self.assertEqual(
            num2words(20000.12, to='currency', lang='ar', currency="EGP"),
            'عشرون ألف جنيه و اثنتا عشرة قرش')
        self.assertEqual(
            num2words(923411, to='currency', lang='ar', currency="SR"),
            'تسعمائة و ثلاثة و عشرون ألفاً  و أربعمائة و أحد عشر ريالاً')
        self.assertEqual(
            num2words(1000000.99, to='currency', lang='ar', currency="KWD"),
            'واحد مليون دينار و تسع و تسعون فلس')

    def test_ordinal(self):
        self.assertEqual(num2words(1, to='ordinal', lang='ar'), 'الاول')
        self.assertEqual(num2words(2, to='ordinal', lang='ar'), 'الثاني')
        self.assertEqual(num2words(3, to='ordinal', lang='ar'), 'الثالث')
        self.assertEqual(num2words(4, to='ordinal', lang='ar'), 'الرابع')
        self.assertEqual(num2words(5, to='ordinal', lang='ar'), 'الخامس')
        self.assertEqual(num2words(6, to='ordinal', lang='ar'), 'السادس')
        self.assertEqual(num2words(9, to='ordinal', lang='ar'), 'التاسع')
        self.assertEqual(num2words(20, to='ordinal', lang='ar'), 'العشرون')
        self.assertEqual(num2words(20, to='ordinal', lang='ar'), 'العشرون')
        self.assertEqual(num2words(20, to='ordinal', lang='ar'), 'العشرون')
        self.assertEqual(num2words(94, to='ordinal', lang='ar'),
                         'الأربع و تسعون')
        self.assertEqual(num2words(102, to='ordinal', lang='ar'),
                         'المائة و اثنان')

    def test_year(self):
        self.assertEqual(num2words(1, to='ordinal', lang='ar'), 'الاول')
        self.assertEqual(num2words(2, to='ordinal', lang='ar'), 'الثاني')
        self.assertEqual(num2words(3, to='ordinal', lang='ar'), 'الثالث')
        self.assertEqual(num2words(4, to='ordinal', lang='ar'), 'الرابع')
        self.assertEqual(num2words(5, to='ordinal', lang='ar'), 'الخامس')
        self.assertEqual(num2words(6, to='ordinal', lang='ar'), 'السادس')
        self.assertEqual(num2words(9, to='ordinal', lang='ar'), 'التاسع')
        self.assertEqual(num2words(20, to='ordinal', lang='ar'), 'العشرون')
        self.assertEqual(num2words(20, to='ordinal', lang='ar'), 'العشرون')
        self.assertEqual(num2words(20, to='ordinal', lang='ar'), 'العشرون')
        self.assertEqual(num2words(94, to='ordinal', lang='ar'),
                         'الأربع و تسعون')
        self.assertEqual(num2words(102, to='ordinal', lang='ar'),
                         'المائة و اثنان')
