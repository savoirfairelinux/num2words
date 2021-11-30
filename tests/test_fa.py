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


class Num2WordsFATest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='fa'), "یكصد")
        self.assertEqual(num2words(101, lang='fa'), "یكصد و یک")
        self.assertEqual(num2words(110, lang='fa'), "یكصد و ده")
        self.assertEqual(num2words(115, lang='fa'), "یكصد و پانزده")
        self.assertEqual(num2words(123, lang='fa'), "یكصد و بیست و سه")
        self.assertEqual(num2words(1000, lang='fa'), "یک هزار")
        self.assertEqual(num2words(1001, lang='fa'), "یک هزار و یک")
        self.assertEqual(num2words(2012, lang='fa'), "دو هزار و دوازده")
        self.assertEqual(
            num2words(10.02, lang='fa'),
            "ده و دو صدم"
        )
        self.assertEqual(
            num2words(15.007, lang='fa'),
            "پانزده و هفت هزارم"
        )
        self.assertEqual(
            num2words(12519.85, lang='fa'),
            "دوازده هزار و پانصد و نوزده و هشتاد و پنج صدم"
        )
        self.assertEqual(
            num2words(123.50, lang='fa'),
            "یكصد و بیست و سه و پنج دهم"
        )
        self.assertEqual(
            num2words(1234567890, lang='fa'),
            "یک میلیارد و دویست و سی و چهار میلیون و پانصد و شصت و هفت هزار و هشتصد و نود"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='fa'),
            "دویست و پانزده کوینتیلیون و چهارصد و شصت و یک کادریلیارد و چهارصد و هفت کوآدریلیون و هشتصد و نود و دو تریلیارد و سی و نه تریلیون و دو بیلیارد و یكصد و پنجاه و هفت بیلیون و یكصد و هشتاد و نه میلیارد و هشتصد و هشتاد و سه میلیون و نهصد و یک هزار و ششصد و هفتاد و شش"
        )

    def test_currency(self):
        self.assertEqual(
            num2words(70500, lang='fa', to='currency', currency='TOMAN'),
            "هفتاد هزار و پانصد تومان")
        self.assertEqual(
            num2words(102543, lang='fa', to='currency'),
            "یكصد و دو هزار و پانصد و چهل و سه ريال")
        self.assertEqual(
            num2words(102543, lang='fa', to='currency', currency='TOMAN'),
            "یكصد و دو هزار و پانصد و چهل و سه تومان")
       
