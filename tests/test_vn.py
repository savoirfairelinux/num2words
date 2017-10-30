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


class Num2WordsVNTest(TestCase):

    def test_0(self):
        self.assertEqual(num2words(0, lang="vi_VN"), "không")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="vi_VN"), "một")
        self.assertEqual(num2words(2, lang="vi_VN"), "hai")
        self.assertEqual(num2words(7, lang="vi_VN"), "bảy")
        self.assertEqual(num2words(10, lang="vi_VN"), "mười")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="vi_VN"), "mười một")
        self.assertEqual(num2words(13, lang="vi_VN"), "mười ba")
        self.assertEqual(num2words(14, lang="vi_VN"), "mười bốn")
        self.assertEqual(num2words(15, lang="vi_VN"), "mười lăm")
        self.assertEqual(num2words(16, lang="vi_VN"), "mười sáu")
        self.assertEqual(num2words(19, lang="vi_VN"), "mười chín")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="vi_VN"), "hai mươi")
        self.assertEqual(num2words(23, lang="vi_VN"), "hai mươi ba")
        self.assertEqual(num2words(28, lang="vi_VN"), "hai mươi tám")
        self.assertEqual(num2words(31, lang="vi_VN"), "ba mươi mốt")
        self.assertEqual(num2words(40, lang="vi_VN"), "bốn mươi")
        self.assertEqual(num2words(66, lang="vi_VN"), "sáu mươi sáu")
        self.assertEqual(num2words(92, lang="vi_VN"), "chín mươi hai")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="vi_VN"), "một trăm")
        self.assertEqual(num2words(150, lang="vi_VN"), "một trăm năm mươi")
        self.assertEqual(
            num2words(196, lang="vi_VN"), "một trăm chín mươi sáu"
        )
        self.assertEqual(num2words(200, lang="vi_VN"), "hai trăm")
        self.assertEqual(num2words(210, lang="vi_VN"), "hai trăm mười")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="vi_VN"), "một nghìn")
        self.assertEqual(num2words(1500, lang="vi_VN"), "một nghìn năm trăm")
        self.assertEqual(
            num2words(7378, lang="vi_VN"), "bảy nghìn ba trăm bảy mươi tám"
        )
        self.assertEqual(num2words(2000, lang="vi_VN"), "hai nghìn")
        self.assertEqual(num2words(2100, lang="vi_VN"), "hai nghìn một trăm")
        self.assertEqual(
            num2words(6870, lang="vi_VN"), "sáu nghìn tám trăm bảy mươi"
        )
        self.assertEqual(num2words(10000, lang="vi_VN"), "mười nghìn")
        self.assertEqual(num2words(100000, lang="vi_VN"), "một trăm nghìn")
        self.assertEqual(
            num2words(523456, lang="vi_VN"),
            "năm trăm hai mươi ba nghìn bốn trăm năm mươi sáu"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="vi_VN"), "một triệu")
        self.assertEqual(
            num2words(1200000, lang="vi_VN"), "một triệu hai trăm nghìn"
        )
        self.assertEqual(num2words(3000000, lang="vi_VN"), "ba triệu")
        self.assertEqual(
            num2words(3800000, lang="vi_VN"), "ba triệu tám trăm nghìn"
        )
        self.assertEqual(num2words(1000000000, lang="vi_VN"), "một tỷ")
        self.assertEqual(num2words(2000000000, lang="vi_VN"), "hai tỷ")
        self.assertEqual(
            num2words(2000001000, lang="vi_VN"), "hai tỷ một nghìn"
        )
        self.assertEqual(
            num2words(1234567890, lang="vi_VN"),
            "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn "
            "tám trăm chín mươi"
        )

    def test_decimal_number(self):
        self.assertEqual(
            num2words(1000.11, lang="vi_VN"), "một nghìn phẩy mười một"
        )
        self.assertEqual(
            num2words(1000.21, lang="vi_VN"), "một nghìn phẩy hai mươi mốt"
        )

    def test_special_number(self):
        """
        Some number will have some specail rule
        """
        self.assertEqual(num2words(21, lang="vi_VN"), "hai mươi mốt")
        self.assertEqual(num2words(25, lang="vi_VN"), "hai mươi lăm")
        # >100
        self.assertEqual(num2words(101, lang="vi_VN"), "một trăm lẻ một")
        self.assertEqual(num2words(105, lang="vi_VN"), "một trăm lẻ năm")
        self.assertEqual(num2words(701, lang="vi_VN"), "bảy trăm lẻ một")
        self.assertEqual(num2words(705, lang="vi_VN"), "bảy trăm lẻ năm")

        # >1000
        self.assertEqual(num2words(1001, lang="vi_VN"), "một nghìn lẻ một")
        self.assertEqual(num2words(1005, lang="vi_VN"), "một nghìn lẻ năm")
        self.assertEqual(
            num2words(98765, lang="vi_VN"),
            "chín mươi tám nghìn bảy trăm sáu mươi lăm"
        )

        # > 1000000
        self.assertEqual(num2words(3000005, lang="vi_VN"), "ba triệu lẻ năm")
        self.assertEqual(num2words(1000007, lang="vi_VN"), "một triệu lẻ bảy")

        # > 1000000000
        self.assertEqual(
            num2words(1000000017, lang="vi_VN"), "một tỷ lẻ mười bảy"
        )
        self.assertEqual(
            num2words(1000101017, lang="vi_VN"),
            "một tỷ một trăm lẻ một nghìn lẻ mười bảy"
        )
