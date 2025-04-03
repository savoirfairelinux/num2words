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


class Num2WordsMNTest(TestCase):
    def test_to_cardinal(self):
        self.maxDiff = None
        self.assertEqual(num2words(7, lang='mn'), "долоо")
        self.assertEqual(num2words(23, lang='mn'), "хорин гурав")
        self.assertEqual(num2words(145, lang='mn'), "зуун дөчин тав")
        self.assertEqual(num2words(100000, lang='mn'), "зуун мянга")
        self.assertEqual(num2words(130000, lang='mn'), "зуун гучин мянга")
        self.assertEqual(num2words(2000, lang='mn'), "хоёр мянга")
        self.assertEqual(num2words(9008, lang='mn'), "есөн мянга найм")
        self.assertEqual(
            num2words(2869, lang='mn'),
            "хоёр мянга найман зуун жаран ес"
        )
        self.assertEqual(
            num2words(-789000125, lang='mn'),
            "хасах долоон зуун наян есөн сая зуун хорин тав",
        )
        self.assertEqual(
            num2words(84932, lang='mn'),
            "наян дөрвөн мянга есөн зуун гучин хоёр"
        )

    def test_to_cardinal_floats(self):
        self.assertEqual(
            num2words(100.67, lang="mn"),
            "зуу, зууны жаран долоо",
        )
        self.assertEqual(num2words(0.7, lang='mn'), "тэг, аравны долоо")
        self.assertEqual(num2words(1.73, lang='mn'), "нэг, зууны далан гурав")
        self.assertEqual(
            num2words(5045.0, lang='mn'),
            "таван мянга дөчин тав"
        )
        self.assertEqual(
            num2words(10.02, lang='mn'),
            "арав, зууны хоёр"
        )
        self.assertEqual(
            num2words(15.007, lang='mn'),
            "арван тав, мянганы долоо"
        )

    def test_to_ordinal(self):
        self.assertEqual(
            num2words(105, lang='mn', to='ordinal'),
            "зуун тав дугаар"
        )
        self.assertEqual(
            num2words(123, lang='mn', to='ordinal'),
            "зуун хорин гурав дугаар"
        )
        self.assertEqual(
            num2words(540, lang='mn', to='ordinal'),
            "таван зуун дөч дүгээр"
        )
        self.assertEqual(
            num2words(79, lang='mn', to='ordinal'),
            "далан ес дүгээр"
        )

        self.assertEqual(
            num2words(1000, lang='mn', to='ordinal'),
            "нэг мянга дугаар"
        )

    def test_to_ordinal_num(self):
        self.assertEqual(
            num2words(105, lang='mn', to='ordinal_num'),
            "105 дугаар"
        )

        self.assertEqual(
            num2words(489, lang='mn', to='ordinal_num'),
            "489 дүгээр"
        )

    def test_to_year(self):
        self.assertEqual(
            num2words(2005, lang='mn', to="year"),
            "хоёр мянга таван он",
        )
        self.assertEqual(
            num2words(-670, lang='mn', to="year"),
            "МЭӨ зургаан зуун далан он",
        )

    def test_to_currency(self):
        self.assertEqual(
            num2words(407.52, lang='mn', to="currency", currency="AUD"),
            "дөрвөн зуун долоон Австралийн доллар, тавин хоёр цент",
        )
        self.assertEqual(
            num2words(19.45, lang='mn', to="currency", currency="MNT"),
            "арван есөн төгрөг, дөчин таван мөнгө",
        )
        self.assertEqual(
            num2words(67000, lang='mn', to="currency", currency="GBP"),
            "зургаан зуун далан фунт стерлинг",
        )
        self.assertEqual(
            num2words(12000.0, lang='mn', to="currency", currency="GBP"),
            "арван хоёр мянган фунт стерлинг",
        )
        self.assertEqual(
            num2words(4000.0, lang='mn', to="currency", currency="GBP"),
            "дөрвөн мянган фунт стерлинг",
        )
        self.assertEqual(
            num2words(500.0, lang='mn', to="currency", currency="SEK"),
            "таван зуун Шведийн крон",
        )
        self.assertEqual(
            num2words(
                499.0,
                lang="mn",
                to="currency",
                currency="SEK",
                adjective=False,
            ),
            "дөрвөн зуун ерэн есөн крон",
        )
        self.assertEqual(
            num2words(6002.0, lang='mn', to="currency", currency="USD"),
            "зургаан мянга хоёр Америк доллар",
        )
        self.assertEqual(
            num2words(6000.0, lang='mn', to="currency", currency="USD"),
            "зургаан мянган Америк доллар",
        )
