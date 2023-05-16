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


class Num2WordsROTest(TestCase):
    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="mn", to="ordinal"), "нэгдүгээр")
        self.assertEqual(
            num2words(22, lang="mn", to="ordinal"), "хорин хоёрдугаар"
        )
        self.assertEqual(
            num2words(21, lang="mn", to="ordinal"), "хорин нэгдүгээр"
        )
        self.assertEqual(
            num2words(12, lang="mn", to="ordinal"), "арван хоёрдугаар"
        )
        self.assertEqual(
            num2words(130, lang="mn", to="ordinal"), "нэг зуун гучдугаар"
        )
        self.assertEqual(
            num2words(1003, lang="mn", to="ordinal"), "нэг мянга гуравдугаар"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(1, lang="mn", to="ordinal_num"), "1-р")
        self.assertEqual(num2words(10, lang="mn", to="ordinal_num"), "10-р")
        self.assertEqual(num2words(21, lang="mn", to="ordinal_num"), "21-р")
        self.assertEqual(num2words(102, lang="mn", to="ordinal_num"), "102-р")
        self.assertEqual(num2words(73, lang="mn", to="ordinal_num"), "73-р")

    def test_cardinal(self):
        self.assertEqual(num2words(10, lang="mn"), "арав")
        self.assertEqual(num2words(100, lang="mn"), "нэг зуу")
        self.assertEqual(num2words(1000, lang="mn"), "нэг мянга")
        self.assertEqual(num2words(10000, lang="mn"), "арван мянга")
        self.assertEqual(num2words(100000, lang="mn"), "нэг зуун мянга")
        self.assertEqual(num2words(1000000, lang="mn"), "нэг сая")
        self.assertEqual(num2words(167, lang="mn"), "нэг зуун жаран долоо")
        self.assertEqual(num2words(421, lang="mn"), "дөрвөн зуун хорин нэг")
        self.assertEqual(
            num2words(1947, lang="mn"), "нэг мянга есөн зуун дөчин долоо"
        )
        self.assertEqual(
            num2words(1250, lang="mn"), "нэг мянга хоёр зуун тавь"
        )
        self.assertEqual(
            num2words(12160, lang="mn"), "арван хоёр мянга нэг зуун жар"
        )
        self.assertEqual(
            num2words(12500, lang="mn"), "арван хоёр мянга таван зуу"
        )
        self.assertEqual(num2words(50070, lang="mn"), "тавин мянга дал")
        self.assertEqual(num2words(50005, lang="mn"), "тавин мянга тав")
        self.assertEqual(num2words(20002, lang="mn"), "хорин мянга хоёр")
        self.assertEqual(num2words(1000000, lang="mn"), "нэг сая")
        self.assertEqual(
            num2words(1245000, lang="mn"),
            "нэг сая хоёр зуун дөчин таван мянга",
        )

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang="mn"), "арван хоёр аравны тав")
        self.assertEqual(
            num2words(12.51, lang="mn"), "арван хоёр зууны тавин нэг"
        )
        self.assertEqual(
            num2words(12.53, lang="mn"), "арван хоёр зууны тавин гурав"
        )
        self.assertEqual(
            num2words(12.59, lang="mn"), "арван хоёр зууны тавин ес"
        )

    def test_big_numbers(self):
        self.assertEqual(num2words(1000000, lang="mn"), "нэг сая")
        self.assertEqual(num2words(1000000000, lang="mn"), "нэг тэрбум")
        self.assertEqual(num2words(33000000, lang="mn"), "гучин гурван сая")
        self.assertEqual(
            num2words(247000000000, lang="mn"),
            "хоёр зуун дөчин долоон тэрбум",
        )

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words(
                "100000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "0000000000000000000000000000000000000"
            )

    def test_to_currency(self):

        self.assertEqual(
            num2words(
                "1100",
                lang="mn",
                to="currency",
                currency="MNT",
            ),
            "нэг мянга нэг зуун төгрөг",
        )
        self.assertEqual(
            num2words("3000", lang="mn", to="currency", currency="USD"),
            "гурван мянган доллар",
        )
        self.assertEqual(
            num2words("101", lang="mn", to="currency"), "нэг зуун нэг төгрөг"
        )
        self.assertEqual(
            num2words("100", lang="mn", to="currency"), "нэг зуун төгрөг"
        )
        self.assertEqual(
            num2words("38.4", lang="mn", to="currency"),
            "гучин найман төгрөг дөчин мөнгө",
        )
        self.assertEqual(
            num2words("1.01", lang="mn", to="currency"),
            "нэг төгрөг нэг мөнгө",
        )
        self.assertEqual(
            num2words("4778.00", lang="mn", to="currency"),
            "дөрвөн мянга долоон зуун далан найман төгрөг",
        )
        self.assertEqual(
            num2words("4778.32", lang="mn", to="currency"),
            "дөрвөн мянга долоон зуун далан найман төгрөг гучин хоёр мөнгө",
        )
        self.assertEqual(
            num2words("1207", lang="mn", to="currency"),
            "нэг мянга хоёр зуун долоон төгрөг",
        )
        self.assertEqual(
            num2words("22000", lang="mn", to="currency"),
            "хорин хоёр мянган төгрөг",
        )
        self.assertEqual(
            num2words("80000", lang="mn", to="currency"),
            "наян мянган төгрөг",
        )
        self.assertEqual(
            num2words("123456789", lang="mn", to="currency"),
            "нэг зуун хорин гурван сая дөрвөн зуун тавин зургаан мянга долоон зуун наян есөн төгрөг",
        )

    def test_to_year(self):
        self.assertEqual(
            num2words(1990, lang="mn", to="year"), "мянга есөн зуун ерэн он"
        )
        self.assertEqual(
            num2words(5555, lang="mn", to="year"),
            "таван мянга таван зуун тавин таван он",
        )
        self.assertEqual(
            num2words(2017, lang="mn", to="year"),
            "хоёр мянга арван долоон он",
        )
        self.assertEqual(
            num2words(1066, lang="mn", to="year"), "мянга жаран зургаан он"
        )
        self.assertEqual(
            num2words(1865, lang="mn", to="year"),
            "мянга найман зуун жаран таван он",
        )
        self.assertEqual(
            num2words(3000, lang="mn", to="year"), "гурван мянган он"
        )
        self.assertEqual(
            num2words(3001, lang="mn", to="year"), "гурван мянга нэг он"
        )
        self.assertEqual(
            num2words(1901, lang="mn", to="year"), "мянга есөн зуун нэг он"
        )
        self.assertEqual(
            num2words(2000, lang="mn", to="year"), "хоёр мянган он"
        )
        self.assertEqual(
            num2words(905, lang="mn", to="year"), "есөн зуун таван он"
        )
        self.assertEqual(
            num2words(6600, lang="mn", to="year"),
            "зургаан мянга зургаан зуун он",
        )
        self.assertEqual(
            num2words(1900, lang="mn", to="year"), "мянга есөн зуун он"
        )
        self.assertEqual(
            num2words(600, lang="mn", to="year"), "зургаан зуун он"
        )
        self.assertEqual(num2words(50, lang="mn", to="year"), "тавин он")
        self.assertEqual(num2words(0, lang="mn", to="year"), "тэг он")
        # suffixes
        self.assertEqual(
            num2words(-44, lang="mn", to="year"), "НТӨ дөчин дөрвөн он"
        )
        self.assertEqual(
            num2words(-44, lang="mn", to="year", suffix="МЭӨ"),
            "МЭӨ дөчин дөрвөн он",
        )
        self.assertEqual(
            num2words(1, lang="mn", to="year", suffix="МТӨ"), "МТӨ нэг он"
        )
        self.assertEqual(
            num2words(66, lang="mn", to="year", suffix="мтө"),
            "мтө жаран зургаан он",
        )
        self.assertEqual(
            num2words(-66000000, lang="mn", to="year"),
            "НТӨ жаран зургаан сая он",
        )
