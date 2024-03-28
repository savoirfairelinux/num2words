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


class Num2WordsSLTest(TestCase):
    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(2, ordinal=True, lang='sl'), "drugi")
        self.assertEqual(num2words(4, ordinal=True, lang='sl'), "četrti")
        self.assertEqual(num2words(7, ordinal=True, lang='sl'), "sedmi")
        self.assertEqual(num2words(8, ordinal=True, lang='sl'), "osmi")
        self.assertEqual(num2words(12, ordinal=True, lang='sl'), "dvanajsti")
        self.assertEqual(num2words(17, ordinal=True, lang='sl'), "sedemnajsti")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            num2words(81, ordinal=True, lang='sl'), "enainosemdeseti"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(num2words(100, ordinal=True, lang='sl'), "stoti")
        self.assertEqual(num2words(1000, ordinal=True, lang='sl'), "tisoči")
        self.assertEqual(
            num2words(4000, ordinal=True, lang='sl'), "štiritisoči"
        )
        self.assertEqual(
            num2words(2000000, ordinal=True, lang='sl'), "dvamilijonti"
        )
        self.assertEqual(
            num2words(5000000000, ordinal=True, lang='sl'), "petmilijardti"
        )

    def test_ordinal_numbers_from_repository_of_test_cases(self):
        # Tests were compiled from cases in
        # https://github.com/gregopet/zapis-slovenskih-stevil
        # The male gender is used by the project so those test cases were
        # copied
        self.assertEqual(num2words(1, ordinal=True, lang='sl'), "prvi")
        self.assertEqual(num2words(2, ordinal=True, lang='sl'), "drugi")
        self.assertEqual(num2words(3, ordinal=True, lang='sl'), "tretji")
        self.assertEqual(num2words(4, ordinal=True, lang='sl'), "četrti")
        self.assertEqual(num2words(5, ordinal=True, lang='sl'), "peti")
        self.assertEqual(num2words(6, ordinal=True, lang='sl'), "šesti")
        self.assertEqual(num2words(7, ordinal=True, lang='sl'), "sedmi")
        self.assertEqual(num2words(8, ordinal=True, lang='sl'), "osmi")
        self.assertEqual(num2words(9, ordinal=True, lang='sl'), "deveti")
        self.assertEqual(num2words(10, ordinal=True, lang='sl'), "deseti")
        self.assertEqual(num2words(100, ordinal=True, lang='sl'), "stoti")
        self.assertEqual(num2words(101, ordinal=True, lang='sl'), "stoprvi")
        self.assertEqual(num2words(102, ordinal=True, lang='sl'), "stodrugi")
        self.assertEqual(num2words(103, ordinal=True, lang='sl'), "stotretji")
        self.assertEqual(num2words(104, ordinal=True, lang='sl'), "stočetrti")
        self.assertEqual(num2words(105, ordinal=True, lang='sl'), "stopeti")
        self.assertEqual(num2words(106, ordinal=True, lang='sl'), "stošesti")
        self.assertEqual(num2words(200, ordinal=True, lang='sl'), "dvestoti")
        self.assertEqual(num2words(1000, ordinal=True, lang='sl'), "tisoči")
        self.assertEqual(num2words(1001, ordinal=True, lang='sl'), "tisočprvi")
        self.assertEqual(num2words(1002, ordinal=True, lang='sl'),
                         "tisočdrugi")
        self.assertEqual(num2words(1003, ordinal=True, lang='sl'),
                         "tisočtretji")
        self.assertEqual(num2words(1004, ordinal=True, lang='sl'),
                         "tisoččetrti")
        self.assertEqual(num2words(1005, ordinal=True, lang='sl'),
                         "tisočpeti")
        self.assertEqual(num2words(1006, ordinal=True, lang='sl'),
                         "tisočšesti")
        self.assertEqual(num2words(2000, ordinal=True, lang='sl'),
                         "dvatisoči")
        self.assertEqual(num2words(20000, ordinal=True, lang='sl'),
                         "dvajsettisoči")
        self.assertEqual(num2words(200000, ordinal=True, lang='sl'),
                         "dvestotisoči")
        self.assertEqual(num2words(1000000, ordinal=True, lang='sl'),
                         "milijonti")
        self.assertEqual(num2words(2000000, ordinal=True, lang='sl'),
                         "dvamilijonti")
        self.assertEqual(num2words(3000000, ordinal=True, lang='sl'),
                         "trimilijonti")
        self.assertEqual(num2words(101000000, ordinal=True, lang='sl'),
                         "stoenmilijonti")
        self.assertEqual(num2words(202000000, ordinal=True, lang='sl'),
                         "dvestodvamilijonti")
        self.assertEqual(num2words(1121, ordinal=True, lang='sl'),
                         "tisočstoenaindvajseti")
        self.assertEqual(num2words(2405, ordinal=True, lang='sl'),
                         "dvatisočštiristopeti")

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(num2words(2, lang='sl'), "dve")
        self.assertEqual(num2words(4000, lang='sl'), "štiri tisoč")
        self.assertEqual(num2words(2000000, lang='sl'), "dva milijona")
        self.assertEqual(num2words(4000000000, lang='sl'), "štiri milijarde")

    def test_cardinal_numbers_from_repository_of_test_cases(self):
        # Tests were compiled from cases in
        # https://github.com/gregopet/zapis-slovenskih-stevil
        self.assertEqual(num2words(0, lang='sl'), "nič")
        self.assertEqual(num2words(1, lang='sl'), "ena")
        self.assertEqual(num2words(2, lang='sl'), "dve")
        self.assertEqual(num2words(3, lang='sl'), "tri")
        self.assertEqual(num2words(4, lang='sl'), "štiri")
        self.assertEqual(num2words(5, lang='sl'), "pet")
        self.assertEqual(num2words(6, lang='sl'), "šest")
        self.assertEqual(num2words(7, lang='sl'), "sedem")
        self.assertEqual(num2words(8, lang='sl'), "osem")
        self.assertEqual(num2words(9, lang='sl'), "devet")
        self.assertEqual(num2words(10, lang='sl'), "deset")
        self.assertEqual(num2words(11, lang='sl'), "enajst")
        self.assertEqual(num2words(12, lang='sl'), "dvanajst")
        self.assertEqual(num2words(13, lang='sl'), "trinajst")
        self.assertEqual(num2words(14, lang='sl'), "štirinajst")
        self.assertEqual(num2words(15, lang='sl'), "petnajst")
        self.assertEqual(num2words(16, lang='sl'), "šestnajst")
        self.assertEqual(num2words(17, lang='sl'), "sedemnajst")
        self.assertEqual(num2words(18, lang='sl'), "osemnajst")
        self.assertEqual(num2words(19, lang='sl'), "devetnajst")
        self.assertEqual(num2words(20, lang='sl'), "dvajset")
        self.assertEqual(num2words(21, lang='sl'), "enaindvajset")
        self.assertEqual(num2words(22, lang='sl'), "dvaindvajset")
        self.assertEqual(num2words(23, lang='sl'), "triindvajset")
        self.assertEqual(num2words(24, lang='sl'), "štiriindvajset")
        self.assertEqual(num2words(25, lang='sl'), "petindvajset")
        self.assertEqual(num2words(26, lang='sl'), "šestindvajset")
        self.assertEqual(num2words(27, lang='sl'), "sedemindvajset")
        self.assertEqual(num2words(28, lang='sl'), "osemindvajset")
        self.assertEqual(num2words(29, lang='sl'), "devetindvajset")
        self.assertEqual(num2words(30, lang='sl'), "trideset")
        self.assertEqual(num2words(40, lang='sl'), "štirideset")
        self.assertEqual(num2words(50, lang='sl'), "petdeset")
        self.assertEqual(num2words(60, lang='sl'), "šestdeset")
        self.assertEqual(num2words(70, lang='sl'), "sedemdeset")
        self.assertEqual(num2words(80, lang='sl'), "osemdeset")
        self.assertEqual(num2words(90, lang='sl'), "devetdeset")
        self.assertEqual(num2words(100, lang='sl'), "sto")
        self.assertEqual(num2words(101, lang='sl'), "sto ena")
        self.assertEqual(num2words(102, lang='sl'), "sto dve")
        self.assertEqual(num2words(103, lang='sl'), "sto tri")
        self.assertEqual(num2words(104, lang='sl'), "sto štiri")
        self.assertEqual(num2words(105, lang='sl'), "sto pet")
        self.assertEqual(num2words(106, lang='sl'), "sto šest")
        self.assertEqual(num2words(200, lang='sl'), "dvesto")
        self.assertEqual(num2words(300, lang='sl'), "tristo")
        self.assertEqual(num2words(400, lang='sl'), "štiristo")
        self.assertEqual(num2words(500, lang='sl'), "petsto")
        self.assertEqual(num2words(600, lang='sl'), "šeststo")
        self.assertEqual(num2words(700, lang='sl'), "sedemsto")
        self.assertEqual(num2words(800, lang='sl'), "osemsto")
        self.assertEqual(num2words(900, lang='sl'), "devetsto")
        self.assertEqual(num2words(1000, lang='sl'), "tisoč")
        self.assertEqual(num2words(1001, lang='sl'), "tisoč ena")
        self.assertEqual(num2words(1002, lang='sl'), "tisoč dve")
        self.assertEqual(num2words(1003, lang='sl'), "tisoč tri")
        self.assertEqual(num2words(1004, lang='sl'), "tisoč štiri")
        self.assertEqual(num2words(1005, lang='sl'), "tisoč pet")
        self.assertEqual(num2words(1006, lang='sl'), "tisoč šest")
        self.assertEqual(num2words(2000, lang='sl'), "dva tisoč")
        self.assertEqual(num2words(20000, lang='sl'), "dvajset tisoč")
        self.assertEqual(num2words(100000, lang='sl'), "sto tisoč")
        self.assertEqual(num2words(101000, lang='sl'), "sto en tisoč")
        self.assertEqual(num2words(200000, lang='sl'), "dvesto tisoč")
        self.assertEqual(num2words(1000000, lang='sl'), "milijon")
        self.assertEqual(num2words(2000000, lang='sl'), "dva milijona")
        self.assertEqual(num2words(3000000, lang='sl'), "trije milijoni")
        self.assertEqual(num2words(101000000, lang='sl'), "sto en milijon")
        self.assertEqual(num2words(202000000, lang='sl'),
                         "dvesto dva milijona")
        self.assertEqual(num2words(303000000, lang='sl'),
                         "tristo trije milijoni")
        self.assertEqual(num2words(304000000, lang='sl'),
                         "tristo štirje milijoni")
        self.assertEqual(num2words(1000000000, lang='sl'), "milijarda")
        self.assertEqual(num2words(2000000000, lang='sl'), "dve milijardi")
        self.assertEqual(num2words(1121, lang='sl'), "tisoč sto enaindvajset")
        self.assertEqual(num2words(2401, lang='sl'), "dva tisoč štiristo ena")
        self.assertEqual(num2words(201001004, lang='sl'),
                         "dvesto en milijon tisoč štiri")
        self.assertEqual(
            num2words(1803603801, lang='sl'),
            "milijarda osemsto trije milijoni šeststo tri tisoč osemsto ena")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(num2words(3.48, lang='sl'), "tri celih štiri osem")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='sl')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang='sl')
