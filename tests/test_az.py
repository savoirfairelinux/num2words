# -*- coding, utf-8 -*-
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


class Num2WordAZTest(TestCase):
    lang = 'az'

    CARDINAL_TEST_CASES = (
        (0, 'sıfır',),
        (1, 'bir',),
        (2, 'iki',),
        (3, 'üç',),
        (4, 'dörd',),
        (5, 'beş',),
        (6, 'altı',),
        (7, 'yeddi',),
        (8, 'səkkiz',),
        (9, 'doqquz',),
        (10, 'on',),
        (11, 'on bir',),
        (20, 'iyirmi',),
        (22, 'iyirmi iki',),
        (30, 'otuz',),
        (33, 'otuz üç',),
        (40, 'qırx',),
        (44, 'qırx dörd',),
        (50, 'əlli',),
        (55, 'əlli beş',),
        (60, 'altmış',),
        (66, 'altmış altı',),
        (70, 'yetmiş',),
        (77, 'yetmiş yeddi',),
        (80, 'səksən',),
        (88, 'səksən səkkiz',),
        (90, 'doxsan',),
        (99, 'doxsan doqquz',),
        (100, 'yüz',),
        (200, 'iki yüz',),
        (678, 'altı yüz yetmiş səkkiz',),
        (999, 'doqquz yüz doxsan doqquz',),
        (1000, 'min',),
        (100_000, 'yüz min',),
        (328_914, 'üç yüz iyirmi səkkiz min doqquz yüz on dörd',),
        (1_000_000, 'bir milyon',),
        (1_000_000_000, 'bir milyard',),
        (10**12, 'bir trilyon',),
        (10**15, 'bir katrilyon',),
        (10**18, 'bir kentilyon',),
        (10**21, 'bir sekstilyon',),
        (10**24, 'bir septilyon',),
        (10**27, 'bir oktilyon',),
        (10**30, 'bir nonilyon',),
        (10**33, 'bir desilyon',),
        (10**36, 'bir undesilyon',),
        (10**39, 'bir dodesilyon',),
        (10**42, 'bir tredesilyon',),
        (10**45, 'bir katordesilyon',),
        (10**48, 'bir kendesilyon',),
        (10**51, 'bir seksdesilyon',),
        (10**54, 'bir septendesilyon',),
        (10**57, 'bir oktodesilyon',),
        (10**60, 'bir novemdesilyon',),
        (10**63, 'bir vigintilyon',),
        (-0, 'sıfır',),
        (-1, 'mənfi bir',),
        (-2, 'mənfi iki',),
        (-3, 'mənfi üç',),
        (-4, 'mənfi dörd',),
        (-5, 'mənfi beş',),
        (-6, 'mənfi altı',),
        (-7, 'mənfi yeddi',),
        (-8, 'mənfi səkkiz',),
        (-9, 'mənfi doqquz',),
        (-10, 'mənfi on',),
        (-11, 'mənfi on bir',),
        (-20, 'mənfi iyirmi',),
        (-22, 'mənfi iyirmi iki',),
        (-30, 'mənfi otuz',),
        (-33, 'mənfi otuz üç',),
        (-40, 'mənfi qırx',),
        (-44, 'mənfi qırx dörd',),
        (-50, 'mənfi əlli',),
        (-55, 'mənfi əlli beş',),
        (-60, 'mənfi altmış',),
        (-66, 'mənfi altmış altı',),
        (-70, 'mənfi yetmiş',),
        (-77, 'mənfi yetmiş yeddi',),
        (-80, 'mənfi səksən',),
        (-88, 'mənfi səksən səkkiz',),
        (-90, 'mənfi doxsan',),
        (-99, 'mənfi doxsan doqquz',),
        (-100, 'mənfi yüz',),
        (-200, 'mənfi iki yüz',),
        (-678, 'mənfi altı yüz yetmiş səkkiz',),
        (-999, 'mənfi doqquz yüz doxsan doqquz',),
        (-1000, 'mənfi min',),
        (-100_000, 'mənfi yüz min',),
        (-328_914, 'mənfi üç yüz iyirmi səkkiz min doqquz yüz on dörd',),
        (-1_000_000, 'mənfi bir milyon',),
        (-1_000_000_000, 'mənfi bir milyard',),
        (-10**12, 'mənfi bir trilyon',),
        (-10**15, 'mənfi bir katrilyon',),
        (-10**18, 'mənfi bir kentilyon',),
        (-10**21, 'mənfi bir sekstilyon',),
        (-10**24, 'mənfi bir septilyon',),
        (-10**27, 'mənfi bir oktilyon',),
        (-10**30, 'mənfi bir nonilyon',),
        (-10**33, 'mənfi bir desilyon',),
        (-10**36, 'mənfi bir undesilyon',),
        (-10**39, 'mənfi bir dodesilyon',),
        (-10**42, 'mənfi bir tredesilyon',),
        (-10**45, 'mənfi bir katordesilyon',),
        (-10**48, 'mənfi bir kendesilyon',),
        (-10**51, 'mənfi bir seksdesilyon',),
        (-10**54, 'mənfi bir septendesilyon',),
        (-10**57, 'mənfi bir oktodesilyon',),
        (-10**60, 'mənfi bir novemdesilyon',),
        (-10**63, 'mənfi bir vigintilyon'),
    )

    CARDINAL_FRACTION_TEST_CASES = (
        (0.2, 'sıfır nöqtə iki',),
        (0.02, 'sıfır nöqtə sıfır iki',),
        (0.23, 'sıfır nöqtə iyirmi üç',),
        (0.0023, 'sıfır nöqtə sıfır sıfır iyirmi üç',),
        (1.43, 'bir nöqtə qırx üç',),
        (-0.2, 'mənfi sıfır nöqtə iki',),
        (-0.02, 'mənfi sıfır nöqtə sıfır iki',),
        (-0.23, 'mənfi sıfır nöqtə iyirmi üç',),
        (-0.0023, 'mənfi sıfır nöqtə sıfır sıfır iyirmi üç',),
        (-1.43, 'mənfi bir nöqtə qırx üç',),
    )

    ORDINAL_TEST_CASES = (
        (0, 'sıfırıncı',),
        (1, 'birinci',),
        (2, 'ikinci',),
        (3, 'üçüncü',),
        (4, 'dördüncü',),
        (5, 'beşinci',),
        (6, 'altıncı',),
        (7, 'yeddinci',),
        (8, 'səkkizinci',),
        (9, 'doqquzuncu',),
        (10, 'onuncu',),
        (11, 'on birinci',),
        (20, 'iyirminci',),
        (22, 'iyirmi ikinci',),
        (30, 'otuzuncu',),
        (33, 'otuz üçüncü',),
        (40, 'qırxıncı',),
        (44, 'qırx dördüncü',),
        (50, 'əllinci',),
        (55, 'əlli beşinci',),
        (60, 'altmışıncı',),
        (66, 'altmış altıncı',),
        (70, 'yetmişinci',),
        (77, 'yetmiş yeddinci',),
        (80, 'səksəninci',),
        (88, 'səksən səkkizinci',),
        (90, 'doxsanıncı',),
        (99, 'doxsan doqquzuncu',),
        (100, 'yüzüncü',),
        (1000, 'mininci',),
        (328_914, 'üç yüz iyirmi səkkiz min doqquz yüz on dördüncü',),
        (1_000_000, 'bir milyonuncu'),
    )

    ORDINAL_NUM_TEST_CASES = (
        (0, '0-cı',),
        (1, '1-ci',),
        (2, '2-ci',),
        (3, '3-cü',),
        (4, '4-cü',),
        (5, '5-ci',),
        (6, '6-cı',),
        (7, '7-ci',),
        (8, '8-ci',),
        (9, '9-cu',),
        (10, '10-cu',),
        (11, '11-ci',),
        (20, '20-ci',),
        (22, '22-ci',),
        (30, '30-cu',),
        (33, '33-cü',),
        (40, '40-cı',),
        (44, '44-cü',),
        (50, '50-ci',),
        (55, '55-ci',),
        (60, '60-cı',),
        (66, '66-cı',),
        (70, '70-ci',),
        (77, '77-ci',),
        (80, '80-ci',),
        (88, '88-ci',),
        (90, '90-cı',),
        (99, '99-cu',),
        (100, '100-cü',),
        (1000, '1000-ci',),
        (328_914, '328914-cü',),
        (1_000_000, '1000000-cu'),
    )

    YEAR_TEST_CASES = (
        (167, 'yüz altmış yeddi'),
        (1552, 'min beş yüz əlli iki'),
        (1881, 'min səkkiz yüz səksən bir'),
        (2022, 'iki min iyirmi iki'),
        (-1, 'e.ə. bir'),
        (-500, 'e.ə. beş yüz'),
        (-5000, 'e.ə. beş min'),
    )

    CURRENCY_TEST_CASES = (
        (0.0, 'sıfır manat, sıfır qəpik'),
        (0.01, 'sıfır manat, bir qəpik'),
        (0.1, 'sıfır manat, on qəpik'),
        (1.5, 'bir manat, əlli qəpik'),
        (1.94, 'bir manat, doxsan dörd qəpik'),
        (17.82, 'on yeddi manat, səksən iki qəpik'),
    )

    def test_cardinal(self):
        """Test cardinal conversion for integer numbers."""

        for number, expected in self.CARDINAL_TEST_CASES:
            actual = num2words(number, lang=self.lang, to='cardinal')

            self.assertEqual(actual, expected)

    def test_cardinal_fracion(self):
        """Test cardinal conversion for numbers with fraction."""

        for number, expected in self.CARDINAL_FRACTION_TEST_CASES:
            actual = num2words(number, lang=self.lang, to='cardinal')

            self.assertEqual(actual, expected)

    def test_ordinal(self):
        """Test ordinal conversion."""

        for number, expected in self.ORDINAL_TEST_CASES:
            actual = num2words(number, lang=self.lang, to='ordinal')

            self.assertEqual(actual, expected)

    def test_ordinal_num(self):
        """Test 'ordinal_num' conversion."""

        for number, expected in self.ORDINAL_NUM_TEST_CASES:
            actual = num2words(number, lang=self.lang, to='ordinal_num')

            self.assertEqual(actual, expected)

    def test_year(self):
        """Test year conversion."""

        for number, expected in self.YEAR_TEST_CASES:
            actual = num2words(number, lang=self.lang, to='year')

            self.assertEqual(actual, expected)

    def test_currency(self):
        """Test currency conversion."""

        for number, expected in self.CURRENCY_TEST_CASES:
            actual = num2words(
                number, lang=self.lang, currency='AZN', to='currency')

            self.assertEqual(actual, expected)
