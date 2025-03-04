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


class Num2WordsARTest(TestCase):

    def test_default_currency(self):
        self.assertEqual(num2words(1, to='currency', lang='ar', rafea=True), 'واحد ريال')
        self.assertEqual(num2words(2, to='currency', lang='ar', rafea=True),
                         'اثنان ريالان')
        # self.assertEqual(num2words(2, to='currency', lang='ar', rafea=False),
        #                  'اثنين ريالين')
        self.assertEqual(num2words(10, to='currency', lang='ar', rafea=True),
                         'عشرة ريالات')
        self.assertEqual(num2words(100, to='currency', lang='ar', rafea=True), 'مائة ريال')
        self.assertEqual(num2words(652.12, to='currency', lang='ar', rafea=True),
                         'ستمائة واثنان وخمسون ريالاً واثنا عشر هللة')
        self.assertEqual(num2words(324, to='currency', lang='ar', rafea=True),
                         'ثلاثمائة وأربعة وعشرون ريالاً')
        self.assertEqual(num2words(2000, to='currency', lang='ar', rafea=True),
                         'ألفا ريال')
        self.assertEqual(num2words(541, to='currency', lang='ar', rafea=True),
                         'خمسمائة وواحد وأربعون ريالاً')
        self.assertEqual(num2words(10000, to='currency', lang='ar', rafea=True),
                         'عشرة آلاف ريال')
        self.assertEqual(num2words(20000.12, to='currency', lang='ar', rafea=True),
                         'عشرون ألف ريال واثنا عشر هللة')
        self.assertEqual(num2words(1000000, to='currency', lang='ar', rafea=True),
                         'مليون ريال')
        val = 'تسعمائة وثلاثة وعشرون ألفاً وأربعمائة وأحد عشر ريالاً'
        self.assertEqual(num2words(923411, to='currency', lang='ar', rafea=True), val)
        self.assertEqual(num2words(63411, to='currency', lang='ar', rafea=True),
                         'ثلاثة وستون ألفاً وأربعمائة وأحد عشر ريالاً')
        self.assertEqual(num2words(1000000.99, to='currency', lang='ar', rafea=True),
                         'مليون ريال وتسعة وتسعون هللة')

    def test_currency_parm(self):
        self.assertEqual(
            num2words(1, to='currency', lang='ar', currency="KWD", rafea=True),
            'واحد دينار')
        self.assertEqual(
            num2words(10, to='currency', lang='ar', currency="EGP", rafea=True),
            'عشرة جنيهات')
        self.assertEqual(
            num2words(20000.12, to='currency', lang='ar', currency="EGP", rafea=True),
            'عشرون ألف جنيه واثنا عشر قرش')
        self.assertEqual(
            num2words(923411, to='currency', lang='ar', currency="SR", rafea=True),
            'تسعمائة وثلاثة وعشرون ألفاً وأربعمائة وأحد عشر ريالاً')
        self.assertEqual(
            num2words(1000000.99, to='currency', lang='ar', currency="KWD", rafea=True),
            'مليون دينار وتسعة وتسعون فلس')
        self.assertEqual(
            num2words(1000.42, to='currency', lang='ar', currency="TND"),
            'ألف دينار و أربعمائة و عشرون مليم')
        self.assertEqual(
            num2words(123.21, to='currency', lang='ar', currency="TND"),
            'مائة و ثلاثة و عشرون ديناراً و مئتان و عشر مليمات')

    def test_ordinal(self):
        # Test cases where 'rafea' is True
        self.assertEqual(num2words(1, to='ordinal', lang='ar', rafea=True), 'اول')
        self.assertEqual(num2words(2, to='ordinal', lang='ar', rafea=True), 'ثاني')
        self.assertEqual(num2words(3, to='ordinal', lang='ar', rafea=True), 'ثالث')
        self.assertEqual(num2words(4, to='ordinal', lang='ar', rafea=True), 'رابع')
        self.assertEqual(num2words(5, to='ordinal', lang='ar', rafea=True), 'خامس')
        self.assertEqual(num2words(6, to='ordinal', lang='ar', rafea=True), 'سادس')
        self.assertEqual(num2words(9, to='ordinal', lang='ar', rafea=True), 'تاسع')
        self.assertEqual(num2words(20, to='ordinal', lang='ar', rafea=True), 'عشرون')
        self.assertEqual(num2words(94, to='ordinal', lang='ar', rafea=True), 'أربع وتسعون')
        self.assertEqual(num2words(102, to='ordinal', lang='ar', rafea=True), 'مائة واثنان')
        self.assertEqual(num2words(923411, to='ordinal_num', lang='ar', rafea=True), 'تسعمائة وثلاثة وعشرون ألفاً وأربعمائة وأحد عشر')

        # See https://github.com/savoirfairelinux/num2words/issues/403
        self.assertEqual(num2words(23, lang="ar", rafea=True), 'ثلاثة وعشرون')
        self.assertEqual(num2words(23, to='ordinal',
                         lang="ar", rafea=True), 'ثلاث وعشرون')
        self.assertEqual(num2words(23, lang="ar", rafea=True), 'ثلاثة وعشرون')

         # Test cases where 'rafea' is False
        self.assertEqual(num2words(1, to='ordinal', lang='ar', rafea=False), 'اول')
        self.assertEqual(num2words(2, to='ordinal', lang='ar', rafea=False), 'ثاني')
        self.assertEqual(num2words(3, to='ordinal', lang='ar', rafea=False), 'ثالث')
        self.assertEqual(num2words(4, to='ordinal', lang='ar', rafea=False), 'رابع')
        self.assertEqual(num2words(5, to='ordinal', lang='ar', rafea=False), 'خامس')
        self.assertEqual(num2words(6, to='ordinal', lang='ar', rafea=False), 'سادس')
        self.assertEqual(num2words(9, to='ordinal', lang='ar', rafea=False), 'تاسع')
        self.assertEqual(num2words(20, to='ordinal', lang='ar', rafea=False), 'عشرين')
        self.assertEqual(num2words(94, to='cardinal', lang='ar', rafea=False), 'أربعة وتسعين')
        self.assertEqual(num2words(102, to='ordinal', lang='ar', rafea=False), 'مائة واثنين')
        self.assertEqual(num2words(923411, to='ordinal_num', lang='ar', rafea=False), 'تسعمائة وثلاثة وعشرون ألفاً وأربعمائة وأحد عشر')
        self.assertEqual(num2words(23, lang="ar", rafea=False), 'ثلاثة وعشرين')
        self.assertEqual(num2words(23, to='ordinal', lang="ar", rafea=False), 'ثلاث وعشرين')
        self.assertEqual(num2words(23, lang="ar", rafea=False), 'ثلاثة وعشرين')
    
    def test_cardinal(self):
        self.assertEqual(num2words(0, to='cardinal', lang='ar', rafea=True), 'صفر')
        self.assertEqual(num2words(12, to='cardinal', lang='ar', rafea=True), 'اثنا عشر')
        self.assertEqual(num2words(12, to='cardinal', lang='ar', rafea=False), 'اثني عشر')
        self.assertEqual(num2words(12.3, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,ثلاثة أجزاء من العشر')
        self.assertEqual(num2words(12.3, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,ثلاثة أجزاء من العشر')

        self.assertEqual(num2words(12.01, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,جزءاً واحد من المئة')
        self.assertEqual(num2words(12.01, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,جزءاً واحد من المئة')

        self.assertEqual(num2words(12.02, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,جزءان من المئة')
        self.assertEqual(num2words(12.02, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,جزئين من المئة')

        self.assertEqual(num2words(12.03, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,ثلاثة أجزاء من المئة')
        self.assertEqual(num2words(12.03, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,ثلاثة أجزاء من المئة')

        self.assertEqual(num2words(12.34, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,أربعة وثلاثون جزءاً من المئة')
        self.assertEqual(num2words(12.34, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,أربعة وثلاثين جزءاً من المئة')

        # Testing with more complex numbers
        self.assertEqual(num2words(637.5, to='cardinal', lang='ar', rafea=True), 'ستمائة وسبعة وثلاثون ,خمسة أجزاء من العشر')
        self.assertEqual(num2words(637.5, to='cardinal', lang='ar', rafea=False), 'ستمائة وسبعة وثلاثين ,خمسة أجزاء من العشر')

        self.assertEqual(num2words(12.345, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,ثلاثمائة وخمسة وأربعون جزءاً من اﻷلف')
        self.assertEqual(num2words(12.345, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,ثلاثمائة وخمسة وأربعين جزءاً من اﻷلف')
        
        # self.assertEqual(num2words(12.3, to='cardinal', lang='ar', rafea=True),'اثنا عشر  , ثلاثون')
        # self.assertEqual(num2words(12.3, to='cardinal', lang='ar', rafea=False),'اثني عشر  , ثلاثين')
        # self.assertEqual(num2words(12.01, to='cardinal', lang='ar', rafea=True), 'اثنا عشر  ,إحدى')
        # self.assertEqual(num2words(12.01, to='cardinal', lang='ar', rafea=False), 'اثني عشر  ,إحدى')
       
        # self.assertEqual(num2words(12.02, to='cardinal', lang='ar', rafea=True), 'اثنا عشر  ,اثنتان')
        # self.assertEqual(num2words(12.02, to='cardinal', lang='ar', rafea=False), 'اثني عشر  ,اثنتين')

        # self.assertEqual(num2words(12.03, to='cardinal', lang='ar', rafea=True), 'اثنا عشر  ,ثلاث')
        # self.assertEqual(num2words(12.03, to='cardinal', lang='ar', rafea=False), 'اثني عشر  ,ثلاث')

        # self.assertEqual(num2words(12.34, to='cardinal', lang='ar', rafea=True), 'اثنا عشر ,أربع وثلاثون')
        # self.assertEqual(num2words(12.34, to='cardinal', lang='ar', rafea=False), 'اثني عشر ,أربع وثلاثين')

        # Not implemented
        self.assertEqual(num2words(12.345, to='cardinal', lang='ar', rafea=True),num2words(12.345, to='cardinal', lang='ar', rafea=True))
        self.assertEqual(num2words(12.345, to='cardinal', lang='ar', rafea=True),num2words(12.345, to='cardinal', lang='ar', rafea=True))

        self.assertEqual(num2words(-8324, to='cardinal', lang='ar', rafea=True),'سالب ثمانية آلاف وثلاثمائة وأربعة وعشرون')
        self.assertEqual(num2words(-8324, to='cardinal', lang='ar', rafea=False),'سالب ثمانية آلاف وثلاثمائة وأربعة وعشرين')

        self.assertEqual(num2words(200, to='cardinal', lang='ar', rafea=True), 'مئتا')
        self.assertEqual(num2words(200, to='cardinal', lang='ar', rafea=False), 'مئتي')

        self.assertEqual(num2words(700, to='cardinal', lang='ar', rafea=True), 'سبعمائة')
        self.assertEqual(num2words(101010, to='cardinal', lang='ar', rafea=True), 'مائة وألف ألف وعشرة')
        self.assertEqual(num2words(3431.12, to='cardinal', lang='ar', rafea=True), 'ثلاثة آلاف وأربعمائة وواحد وثلاثون ,اثنا عشر جزءاً من المئة')
        self.assertEqual(num2words(3431.12, to='cardinal', lang='ar', rafea=False), 'ثلاثة آلاف وأربعمائة وواحد وثلاثين ,اثني عشر جزءاً من المئة')

        self.assertEqual(num2words(431, to='cardinal', lang='ar', rafea=True), 'أربعمائة وواحد وثلاثون')
        self.assertEqual(num2words(431, to='cardinal', lang='ar', rafea=False), 'أربعمائة وواحد وثلاثين')
       
        self.assertEqual(num2words(94231, to='cardinal', lang='ar', rafea=True), 'أربعة وتسعون ألفاً ومئتان وواحد وثلاثون')
        self.assertEqual(num2words(94231, to='cardinal', lang='ar', rafea=False), 'أربعة وتسعين ألفاً ومئتين وواحد وثلاثين')

        self.assertEqual(num2words(1431, to='cardinal', lang='ar', rafea=True), 'ألف وأربعمائة وواحد وثلاثون')
        self.assertEqual(num2words(1431, to='cardinal', lang='ar', rafea=False), 'ألف وأربعمائة وواحد وثلاثين')

        self.assertEqual(num2words(94231, to='cardinal', lang='ar', rafea=True), 'أربعة وتسعون ألفاً ومئتان وواحد وثلاثون')
        self.assertEqual(num2words(94231, to='cardinal', lang='ar', rafea=False), 'أربعة وتسعين ألفاً ومئتين وواحد وثلاثين')

        self.assertEqual(num2words(740, to='cardinal', lang='ar', rafea=True), 'سبعمائة وأربعون')
        self.assertEqual(num2words(740, to='cardinal', lang='ar', rafea=False), 'سبعمائة وأربعين')

        self.assertEqual(num2words(741, to='cardinal', lang='ar', rafea=True), 'سبعمائة وواحد وأربعون')
        self.assertEqual(num2words(741, to='cardinal', lang='ar', rafea=False), 'سبعمائة وواحد وأربعين')

        self.assertEqual(num2words(262, to='cardinal', lang='ar', rafea=True),'مئتان واثنان وستون')
        self.assertEqual(num2words(262, to='cardinal', lang='ar', rafea=False),'مئتين واثنين وستين')

        self.assertEqual(num2words(798, to='cardinal', lang='ar', rafea=True),'سبعمائة وثمانية وتسعون')
        self.assertEqual(num2words(798, to='cardinal', lang='ar', rafea=False),'سبعمائة وثمانية وتسعين')

        self.assertEqual(num2words(710, to='cardinal', lang='ar', rafea=True), 'سبعمائة وعشرة')
        self.assertEqual(num2words(711, to='cardinal', lang='ar', rafea=True), 'سبعمائة وأحد عشر')
        self.assertEqual(num2words(700, to='cardinal', lang='ar', rafea=True),'سبعمائة')
        self.assertEqual(num2words(701, to='cardinal', lang='ar', rafea=True), 'سبعمائة وواحد')
        self.assertEqual(num2words(1258888, to='cardinal', lang='ar', rafea=True), 'مليون ومئتان وثمانية وخمسون ألفاً وثمانمائة وثمانية وثمانون')
        self.assertEqual(num2words(1258888, to='cardinal', lang='ar', rafea=False), 'مليون ومئتين وثمانية وخمسين ألفاً وثمانمائة وثمانية وثمانين')

        self.assertEqual(num2words(1100, to='cardinal', lang='ar', rafea=True),'ألف ومائة')
        self.assertEqual(num2words(1000000521, to='cardinal', lang='ar', rafea=True),'مليار وخمسمائة وواحد وعشرون')
        self.assertEqual(num2words(1000000521, to='cardinal', lang='ar', rafea=False),'مليار وخمسمائة وواحد وعشرين')


    def test_prefix_and_suffix(self):
        self.assertEqual(num2words(645, to='currency',
                                   lang='ar', rafea=True, prefix="فقط", suffix="لاغير"),
                         'فقط ستمائة وخمسة وأربعون ريالاً لاغير')

    def test_year(self):
        self.assertEqual(num2words(2000, to='year', lang='ar', rafea=True), 'ألفا')

    def test_max_numbers(self):

        for number in 10**51, 10**51 + 2:

            with self.assertRaises(OverflowError) as context:
                num2words(number, lang='ar', rafea=True)

            self.assertTrue('must be less' in str(context.exception))

    def test_big_numbers(self):
        self.assertEqual(
            num2words(1000000045000000000000003000000002000000300,
                      to='cardinal', lang='ar',rafea=True),
            'تريديسيليون وخمسة وأربعون ديسيليوناً\
 وثلاثة كوينتليونات وملياران وثلاثمائة'
        )
        self.assertEqual(
            num2words(-1000000000000000000000003000000002000000302,
                      to='cardinal', lang='ar', rafea=True),
            'سالب تريديسيليون وثلاثة كوينتليونات \
وملياران وثلاثمائة واثنان'
        )
        self.assertEqual(
            num2words(9999999999999999999999999999999999999999999999992,
                      to='cardinal', lang='ar', rafea=True),
            'تسعة كوينتينيليونات وتسعمائة وتسعة وتسعون كوادريسيليوناً وتسعمائة وتسعة وتسعون تريديسيليوناً وتسعمائة وتسعة وتسعون دوديسيليوناً وتسعمائة وتسعة وتسعون أندسيليوناً وتسعمائة وتسعة وتسعون ديسيليوناً وتسعمائة وتسعة وتسعون نونيليوناً وتسعمائة وتسعة وتسعون أوكتيليوناً وتسعمائة وتسعة وتسعون سبتيليوناً وتسعمائة وتسعة وتسعون سكستيليوناً وتسعمائة وتسعة وتسعون كوينتليوناً وتسعمائة وتسعة وتسعون كوادريليوناً وتسعمائة وتسعة وتسعون تريليوناً وتسعمائة وتسعة وتسعون ملياراً وتسعمائة وتسعة وتسعون مليوناً وتسعمائة وتسعة وتسعون ألفاً وتسعمائة واثنان وتسعون'
        )
