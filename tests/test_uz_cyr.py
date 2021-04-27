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


class Num2WordsUZCYRTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='uz_cyr'), "юз")
        self.assertEqual(num2words(101, lang='uz_cyr'), "бир юз бир")
        self.assertEqual(num2words(110, lang='uz_cyr'), "бир юз ўн")
        self.assertEqual(num2words(115, lang='uz_cyr'), "бир юз ўн беш")
        self.assertEqual(num2words(123, lang='uz_cyr'), "бир юз йигирма уч")
        self.assertEqual(num2words(1000, lang='uz_cyr'), "бир минг")
        self.assertEqual(num2words(1001, lang='uz_cyr'), "бир минг бир")
        self.assertEqual(num2words(2012, lang='uz_cyr'), "икки минг ўн икки")
        self.assertEqual(
            num2words(12519.85, lang='uz_cyr'),
            "ўн икки минг беш юз ўн тўққиз вергул саксон беш")

        self.assertEqual(num2words(5, lang='uz_cyr'), "беш")
        self.assertEqual(num2words(15, lang='uz_cyr'), "ўн беш")
        self.assertEqual(num2words(154, lang='uz_cyr'), "бир юз эллик тўрт")
        self.assertEqual(
            num2words(1135, lang='uz_cyr'), "бир минг бир юз ўттиз беш"
        )
        self.assertEqual(
            num2words(418531, lang='uz_cyr'),
            "тўрт юз ўн саккиз минг беш юз ўттиз бир"
        )
        self.assertEqual(
            num2words(1000139, lang='uz_cyr'), "бир миллион бир юз ўттиз тўққиз"
        )
        self.assertEqual(num2words(-1, lang='uz_cyr'), "минус бир")
        self.assertEqual(num2words(-15, lang='uz_cyr'), "минус ўн беш")
        self.assertEqual(num2words(-100, lang='uz_cyr'), "минус бир юз")

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang='uz_cyr'), "беш вергул икки")
        self.assertEqual(
            num2words(561.42, lang='uz_cyr'),
            "беш юз олтмиш бир вергул қирқ икки"
        )

    def test_to_ordinal(self):
        self.assertEqual(
            num2words(1, lang='uz_cyr', to='ordinal'),
            'биринчи'
        )
        self.assertEqual(
            num2words(5, lang='uz_cyr', to='ordinal'),
            'бешинчи'
        )
        self.assertEqual(
            num2words(10, lang='uz_cyr', to='ordinal'),
            'ўнинчи'
        )

        self.assertEqual(
            num2words(13, lang='uz_cyr', to='ordinal'),
            'ўн учинчи'
        )
        self.assertEqual(
            num2words(20, lang='uz_cyr', to='ordinal'),
            'йигирманчи'
        )
        self.assertEqual(
            num2words(23, lang='uz_cyr', to='ordinal'),
            'йигирма учинчи'
        )
        self.assertEqual(
            num2words(40, lang='uz_cyr', to='ordinal'),
            'қирқинчи'
        )
        self.assertEqual(
            num2words(70, lang='uz_cyr', to='ordinal'),
            'етмишинчи'
        )
        self.assertEqual(
            num2words(100, lang='uz_cyr', to='ordinal'),
            'юзинчи'
        )
        self.assertEqual(
            num2words(136, lang='uz_cyr', to='ordinal'),
            'бир юз ўттиз олтинчи'
        )
        self.assertEqual(
            num2words(500, lang='uz_cyr', to='ordinal'),
            'беш юзинчи'
        )
        self.assertEqual(
            num2words(1000, lang='uz_cyr', to='ordinal'),
            'мингинчи'
        )
        self.assertEqual(
            num2words(1001, lang='uz_cyr', to='ordinal'),
            'минг биринчи'
        )


    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='uz_cyr', to='currency', currency='EUR'),
            'бир евро, нол цент'
        )
        self.assertEqual(
            num2words(1.0, lang='uz_cyr', to='currency', currency='UZS'),
            'бир сўм, нол тийин'
        )
        self.assertEqual(
            num2words(1234.56, lang='uz_cyr', to='currency', currency='EUR'),
            'бир минг икки юз ўттиз тўрт евро, эллик олти цент'
        )
        self.assertEqual(
            num2words(1234.56, lang='uz_cyr', to='currency', currency='UZS'),
            'бир минг икки юз ўттиз тўрт сўм, эллик олти тийин'
        )
        self.assertEqual(
            num2words(10111, lang='uz_cyr', to='currency', currency='EUR',
                      separator=','),
            'бир юз бир евро, ўн бир цент'
        )
        self.assertEqual(
            num2words(10121, lang='uz_cyr', to='currency', currency='UZS',
                      separator=','),
            'бир юз бир сўм, йигирма бир тийин'
        )
        self.assertEqual(
            num2words(10122, lang='uz_cyr', to='currency', currency='UZS',
                      separator=','),
            'бир юз бир сўм, йигирма икки тийин'
        )
        self.assertEqual(
            num2words(10121, lang='uz_cyr', to='currency', currency='EUR',
                      separator=','),
            'бир юз бир евро, йигирма бир цент'
        )
        self.assertEqual(
            num2words(-1251985, lang='uz_cyr', to='currency', currency='EUR',
                      cents=False),
            'минус ўн икки минг беш юз ўн тўққиз евро, 85 цент'
        )
        self.assertEqual(
            num2words('38.4', lang='uz_cyr', to='currency', separator=',',
                      cents=False, currency='EUR'),
            "ўттиз саккиз евро, 40 цент"
        )
        self.assertEqual(
            num2words('1230.56', lang='uz_cyr', to='currency', currency='USD'),
            'бир минг икки юз ўттиз доллар, эллик олти цент'
        )
        self.assertEqual(
            num2words('1031.56', lang='uz_cyr', to='currency', currency='USD'),
            'бир минг ўттиз бир доллар, эллик олти цент'
        )
