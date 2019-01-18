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
from num2words.lang_TH import Num2Word_TH


class TestNumWord(TestCase):

    def test_0(self):
        self.assertEqual(num2words(0, lang='th'), "ศูนย์")

    def test_end_with_1(self):
        self.assertEqual(num2words(21, lang='th'), "ยี่สิบเอ็ด")
        self.assertEqual(num2words(11, lang='th'), "สิบเอ็ด")
        self.assertEqual(num2words(101, lang='th'), "หนึ่งร้อยเอ็ด")
        self.assertEqual(num2words(1201, lang='th'), "หนึ่งพันสองร้อยเอ็ด")

    def test_start_20(self):
        self.assertEqual(num2words(22, lang='th'), "ยี่สิบสอง")
        self.assertEqual(num2words(27, lang='th'), "ยี่สิบเจ็ด")

    def test_start_10(self):
        self.assertEqual(num2words(10, lang='th'), "สิบ")
        self.assertEqual(num2words(18, lang='th'), "สิบแปด")

    def test_1_to_9(self):
        self.assertEqual(num2words(1, lang='th'), "หนึ่ง")
        self.assertEqual(num2words(5, lang='th'), "ห้า")
        self.assertEqual(num2words(9, lang='th'), "เก้า")

    def test_31_to_99(self):
        self.assertEqual(num2words(31, lang='th'), "สามสิบเอ็ด")
        self.assertEqual(num2words(48, lang='th'), "สี่สิบแปด")
        self.assertEqual(num2words(76, lang='th'), "เจ็ดสิบหก")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang='th'), "หนึ่งร้อย")
        self.assertEqual(num2words(123, lang='th'), "หนึ่งร้อยยี่สิบสาม")
        self.assertEqual(num2words(456, lang='th'), "สี่ร้อยห้าสิบหก")
        self.assertEqual(num2words(721, lang='th'), "เจ็ดร้อยยี่สิบเอ็ด")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang='th'), "หนึ่งพัน")
        self.assertEqual(
            num2words(2175, lang='th'), "สองพันหนึ่งร้อยเจ็ดสิบห้า"
        )
        self.assertEqual(num2words(4582, lang='th'), "สี่พันห้าร้อยแปดสิบสอง")
        self.assertEqual(num2words(9346, lang='th'), "เก้าพันสามร้อยสี่สิบหก")

    def test_10000_to_99999(self):
        self.assertEqual(
            num2words(11111, lang='th'), "หนึ่งหมื่นหนึ่งพันหนึ่งร้อยสิบเอ็ด"
        )
        self.assertEqual(
            num2words(22222, lang='th'), "สองหมื่นสองพันสองร้อยยี่สิบสอง"
        )
        self.assertEqual(
            num2words(84573, lang='th'), "แปดหมื่นสี่พันห้าร้อยเจ็ดสิบสาม"
        )

    def test_100000_to_999999(self):
        self.assertEqual(
            num2words(153247, lang='th'),
            "หนึ่งแสนห้าหมื่นสามพันสองร้อยสี่สิบเจ็ด"
        )
        self.assertEqual(
            num2words(562442, lang='th'),
            "ห้าแสนหกหมื่นสองพันสี่ร้อยสี่สิบสอง"
        )
        self.assertEqual(
            num2words(999999, lang='th'),
            "เก้าแสนเก้าหมื่นเก้าพันเก้าร้อยเก้าสิบเก้า"
        )

    def test_more_than_million(self):
        self.assertEqual(
            num2words(1000000, lang='th'),
            "หนึ่งล้าน"
        )
        self.assertEqual(
            num2words(1000001, lang='th'),
            "หนึ่งล้านเอ็ด"
        )
        self.assertEqual(
            num2words(42478941, lang='th'),
            "สี่สิบสองล้านสี่แสนเจ็ดหมื่นแปดพันเก้าร้อยสี่สิบเอ็ด"
        )
        self.assertEqual(
            num2words(712696969, lang='th'),
            "เจ็ดร้อยสิบสองล้านหกแสนเก้าหมื่นหกพันเก้าร้อยหกสิบเก้า"
        )
        self.assertEqual(
            num2words(1000000000000000001, lang='th'),
            "หนึ่งล้านล้านล้านเอ็ด"
        )

    def test_decimal(self):
        self.assertEqual(
            num2words(0.0, lang='th'), "ศูนย์"
        )
        self.assertEqual(
            num2words(0.0038, lang='th'), "ศูนย์จุดศูนย์ศูนย์สามแปด"
        )
        self.assertEqual(
            num2words(0.01, lang='th'), "ศูนย์จุดศูนย์หนึ่ง"
        )
        self.assertEqual(
            num2words(1.123, lang='th'), "หนึ่งจุดหนึ่งสองสาม"
        )
        self.assertEqual(
            num2words(35.37, lang='th'), "สามสิบห้าจุดสามเจ็ด"
        )
        self.assertEqual(
            num2words(1000000.01, lang='th'), "หนึ่งล้านจุดศูนย์หนึ่ง"
        )

    def test_currency(self):
        self.assertEqual(
            num2words(100, lang='th', to='currency', currency='THB'),
            "หนึ่งร้อยบาทถ้วน"
        )
        self.assertEqual(
            num2words(100, lang='th', to='currency', currency='USD'),
            "หนึ่งร้อยดอลลาร์"
        )
        self.assertEqual(
            num2words(100, lang='th', to='currency', currency='EUR'),
            "หนึ่งร้อยยูโร"
        )

    def test_currency_decimal(self):
        self.assertEqual(
            num2words(0.00, lang='th', to='currency'), "ศูนย์บาทถ้วน"
        )
        self.assertEqual(
            num2words(0.05, lang='th', to='currency'), "ห้าสตางค์"
        )
        self.assertEqual(
            num2words(0.50, lang='th', to='currency'), "ห้าสิบสตางค์"
        )
        self.assertEqual(
            num2words(0.99, lang='th', to='currency'), "เก้าสิบเก้าสตางค์"
        )
        self.assertEqual(
            num2words(100.00, lang='th', to='currency'), "หนึ่งร้อยบาทถ้วน"
        )
        self.assertEqual(
            num2words(100.23, lang='th', to='currency', currency='USD'),
            "หนึ่งร้อยดอลลาร์ยี่สิบสามเซนต์"
        )
        self.assertEqual(
            num2words(100.24, lang='th', to='currency', currency='EUR'),
            "หนึ่งร้อยยูโรยี่สิบสี่เซนต์"
        )

    def test_negative(self):
        self.assertEqual(num2words(-10, lang='th'), "ติดลบสิบ")
        self.assertEqual(num2words(-10.50, lang='th'), "ติดลบสิบจุดห้า")
        self.assertEqual(
            num2words(-100.00, lang='th', to='currency'),
            "ติดลบหนึ่งร้อยบาทถ้วน"
        )

    def test_round_2_decimal(self):
        n2wTH = Num2Word_TH()
        self.assertEqual(n2wTH.round_2_decimal(0.004), ('0.00', False))
        self.assertEqual(n2wTH.round_2_decimal(0.005), ('0.01', False))
        self.assertEqual(n2wTH.round_2_decimal(0.006), ('0.01', False))
        self.assertEqual(n2wTH.round_2_decimal(0.0005),
                         ('0.00', False))
        self.assertEqual(n2wTH.round_2_decimal(0.984), ('0.98', False))
        self.assertEqual(n2wTH.round_2_decimal(0.989), ('0.99', False))
        self.assertEqual(n2wTH.round_2_decimal(0.994), ('0.99', False))
        self.assertEqual(n2wTH.round_2_decimal(0.999), ('1.00', False))
        self.assertEqual(n2wTH.round_2_decimal(-0.994), ('0.99', True))
        self.assertEqual(n2wTH.round_2_decimal(-0.999), ('1.00', True))
        # self.assertEqual(n2wTH.round_2_decimal(0.985), ('0.99', False))
        # Expect 0.99 get 0.98
        # self.assertEqual(n2wTH.round_2_decimal(0.995), ('1.00', False))
        # Expect 1.00 get 0.99

    def test_split_six(self):
        n2wTH = Num2Word_TH()
        self.assertEqual(n2wTH.split_six(str(123456789)),
                         ['987654', '321'])
        self.assertEqual(n2wTH.split_six(str(12345)),
                         ['54321'])
        self.assertEqual(n2wTH.split_six(str(1234567)),
                         ['765432', '1'])
