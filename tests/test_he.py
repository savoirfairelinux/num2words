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
from num2words.lang_HE import Num2Word_HE, int2word


class Num2WordsHETest(TestCase):
    maxDiff = None

    def test_negative(self):
        self.assertEqual(num2words(-1, lang="he"), u'מינוס אחת')

    def test_0(self):
        self.assertEqual(num2words(0, lang="he"), u'אפס')

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="he"), u'אחת')
        self.assertEqual(num2words(2, lang="he"), u'שתיים')
        self.assertEqual(num2words(7, lang="he"), u'שבע')
        self.assertEqual(num2words(10, lang="he"), u'עשר')
        self.assertEqual(num2words(
            10, lang="he", gender='m', construct=True), u'עשרת')

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="he"), u'אחת עשרה')
        self.assertEqual(num2words(11, lang="he", gender='m'), u'אחד עשר')
        self.assertEqual(num2words(13, lang="he"), u'שלוש עשרה')
        self.assertEqual(num2words(
            13, lang="he", construct=True), u'שלוש עשרה')
        self.assertEqual(num2words(15, lang="he"), u'חמש עשרה')
        self.assertEqual(num2words(16, lang="he"), u'שש עשרה')
        self.assertEqual(num2words(16, lang="he", gender='m'), u'שישה עשר')
        self.assertEqual(num2words(
            16, lang="he", gender='m', construct=True), u'שישה עשר')
        self.assertEqual(num2words(19, lang="he"), u'תשע עשרה')

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="he"), u'עשרים')
        self.assertEqual(num2words(23, lang="he"), u'עשרים ושלוש')
        self.assertEqual(num2words(23, lang="he", gender='m'), u'עשרים ושלושה')
        self.assertEqual(num2words(
            23, lang="he", construct=True), u'עשרים ושלוש')
        self.assertEqual(num2words(
            23, lang="he", gender='m', construct=True), u'עשרים ושלושה')
        self.assertEqual(num2words(28, lang="he"), u'עשרים ושמונה')
        self.assertEqual(num2words(31, lang="he"), u'שלושים ואחת')
        self.assertEqual(num2words(40, lang="he"), u'ארבעים')
        self.assertEqual(num2words(66, lang="he"), u'שישים ושש')
        self.assertEqual(num2words(92, lang="he"), u'תשעים ושתיים')

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="he"), u'מאה')
        self.assertEqual(num2words(100, lang="he", construct=True), u'מאת')
        self.assertEqual(num2words(111, lang="he"), u'מאה ואחת עשרה')
        self.assertEqual(num2words(
            111, lang="he", construct=True), u'מאה ואחת עשרה')
        self.assertEqual(num2words(150, lang="he"), u'מאה וחמישים')
        self.assertEqual(num2words(196, lang="he"), u'מאה תשעים ושש')
        self.assertEqual(num2words(
            196, lang="he", gender='m'), u'מאה תשעים ושישה')
        self.assertEqual(num2words(
            196, lang="he", gender='m', construct=True), u'מאה תשעים ושישה')
        self.assertEqual(num2words(200, lang="he"), u'מאתיים')
        self.assertEqual(num2words(200, lang="he", construct=True), u'מאתיים')
        self.assertEqual(num2words(210, lang="he"), u'מאתיים ועשר')
        self.assertEqual(num2words(701, lang="he"), u'שבע מאות ואחת')

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="he"), u'אלף')
        self.assertEqual(num2words(1000, lang="he", construct=True), u'אלף')
        self.assertEqual(num2words(1001, lang="he"), u'אלף ואחת')
        self.assertEqual(num2words(1002, lang="he"), u'אלף ושתיים')
        self.assertEqual(num2words(1002, lang="he", gender='m'), u'אלף ושניים')
        self.assertEqual(num2words(
            1002, lang="he", gender='m', construct=True), u'אלף ושניים')
        self.assertEqual(num2words(1003, lang="he"), u'אלף ושלוש')
        self.assertEqual(num2words(1003, lang="he", gender='m'), u'אלף ושלושה')
        self.assertEqual(num2words(
            1003, lang="he", gender='m', construct=True), u'אלף ושלושה')
        self.assertEqual(num2words(1010, lang="he"), u'אלף ועשר')
        self.assertEqual(num2words(1010, lang="he", gender='m'), u'אלף ועשרה')
        self.assertEqual(num2words(
            1010, lang="he", gender='m', construct=True), u'אלף ועשרה')
        self.assertEqual(num2words(1500, lang="he"), u'אלף וחמש מאות')
        self.assertEqual(num2words(2000, lang="he"), u'אלפיים')
        self.assertEqual(num2words(2000, lang="he", construct=True), u'אלפיים')
        self.assertEqual(num2words(2002, lang="he"), u'אלפיים ושתיים')
        self.assertEqual(num2words(
            2002, lang="he", construct=True), u'אלפיים ושתיים')
        self.assertEqual(num2words(3000, lang="he"), u'שלושת אלפים')
        self.assertEqual(num2words(
            3000, lang="he", construct=True), u'שלושת אלפי')
        self.assertEqual(num2words(3001, lang="he"), u'שלושת אלפים ואחת')
        self.assertEqual(num2words(
            3001, lang="he", construct=True), u'שלושת אלפים ואחת')
        self.assertEqual(num2words(3100, lang="he"), u'שלושת אלפים ומאה')
        self.assertEqual(num2words(
            3100, lang="he", construct=True), u'שלושת אלפים ומאה')
        self.assertEqual(num2words(
            6870, lang="he"), u'ששת אלפים שמונה מאות ושבעים')
        self.assertEqual(num2words(
            7378, lang="he"), u'שבעת אלפים שלוש מאות שבעים ושמונה')
        self.assertEqual(num2words(
            9999, lang="he"), u'תשעת אלפים תשע מאות תשעים ותשע')

    def test_10000_to_99999(self):
        self.assertEqual(num2words(10000, lang="he"), u'עשרת אלפים')
        self.assertEqual(num2words(
            10000, lang="he", construct=True), u'עשרת אלפי')
        self.assertEqual(num2words(10001, lang="he"), u'עשרת אלפים ואחת')
        self.assertEqual(num2words(
            10001, lang="he", construct=True), u'עשרת אלפים ואחת')
        self.assertEqual(num2words(
            10999, lang="he"), u'עשרת אלפים תשע מאות תשעים ותשע')
        self.assertEqual(num2words(11000, lang="he"), u'אחד עשר אלף')
        self.assertEqual(num2words(15000, lang="he"), u'חמישה עשר אלף')
        self.assertEqual(num2words(
            15000, lang="he", gender='m'), u'חמישה עשר אלף')
        self.assertEqual(num2words(20000, lang="he"), u'עשרים אלף')
        self.assertEqual(num2words(
            20000, lang="he", construct=True), u'עשרים אלף')
        self.assertEqual(num2words(21000, lang="he"), u'עשרים ואחד אלף')
        self.assertEqual(num2words(25000, lang="he"), u'עשרים וחמישה אלף')
        self.assertEqual(num2words(
            25000, lang="he", construct=True), u'עשרים וחמישה אלף')
        self.assertEqual(num2words(
            68700, lang="he"), u'שישים ושמונה אלף ושבע מאות')
        self.assertEqual(num2words(
            73781, lang="he"), u'שבעים ושלושה אלף שבע מאות שמונים ואחת')
        self.assertEqual(num2words(
            99999, lang="he"), u'תשעים ותשעה אלף תשע מאות תשעים ותשע')

    def test_100000_to_999999(self):
        self.assertEqual(num2words(100000, lang="he"), u'מאה אלף')
        self.assertEqual(num2words(
            100000, lang="he", construct=True), u'מאה אלף')
        self.assertEqual(num2words(100001, lang="he"), u'מאה אלף ואחת')
        self.assertEqual(num2words(
            199999, lang="he"), u'מאה תשעים ותשעה אלף תשע מאות תשעים ותשע')
        self.assertEqual(num2words(110000, lang="he"), u'מאה ועשרה אלף')
        self.assertEqual(num2words(150000, lang="he"), u'מאה וחמישים אלף')
        self.assertEqual(num2words(200000, lang="he"), u'מאתיים אלף')
        self.assertEqual(num2words(210000, lang="he"), u'מאתיים ועשרה אלף')
        self.assertEqual(num2words(
            687000, lang="he"), u'שש מאות שמונים ושבעה אלף')
        self.assertEqual(num2words(
            687000, lang="he", construct=True), u'שש מאות שמונים ושבעה אלף')
        self.assertEqual(num2words(737812, lang="he"),
                         u'שבע מאות שלושים ושבעה אלף שמונה מאות ושתים עשרה')
        self.assertEqual(num2words(999999, lang="he"),
                         u'תשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשע')

    def test_1000000_to_999999999999999(self):
        self.assertEqual(num2words(1000000, lang="he"), u'מיליון')
        self.assertEqual(num2words(
            1000000, lang="he", construct=True), u'מיליון')
        self.assertEqual(num2words(1000002, lang="he"), u'מיליון ושתיים')
        self.assertEqual(num2words(
            1000002, lang="he", construct=True), u'מיליון ושתיים')
        self.assertEqual(num2words(2000000, lang="he"), u'שני מיליון')
        self.assertEqual(num2words(
            2000000, lang="he", construct=True), u'שני מיליוני')
        self.assertEqual(num2words(3000000, lang="he"), u'שלושה מיליון')
        self.assertEqual(num2words(
            3000000, lang="he", construct=True), u'שלושת מיליוני')
        self.assertEqual(num2words(3000002, lang="he"), u'שלושה מיליון ושתיים')
        self.assertEqual(num2words(
            3000002, lang="he", construct=True), u'שלושה מיליון ושתיים')
        self.assertEqual(num2words(10000000, lang="he"), u'עשרה מיליון')
        self.assertEqual(num2words(
            10000000, lang="he", construct=True), 'עשרת מיליוני')
        self.assertEqual(num2words(11000000, lang="he"), u'אחד עשר מיליון')
        self.assertEqual(num2words(
            11000000, lang="he", construct=True), 'אחד עשר מיליוני')

        self.assertEqual(num2words(1000000000, lang="he"), u'מיליארד')
        self.assertEqual(num2words(
            1000000000, lang="he", construct=True), u'מיליארד')
        self.assertEqual(num2words(1000000002, lang="he"), u'מיליארד ושתיים')
        self.assertEqual(num2words(
            1000000002, lang="he", construct=True), u'מיליארד ושתיים')
        self.assertEqual(num2words(2000000000, lang="he"), u'שני מיליארד')
        self.assertEqual(num2words(
            2000000000, lang="he", construct=True), u'שני מיליארדי')
        self.assertEqual(num2words(3000000000, lang="he"), u'שלושה מיליארד')
        self.assertEqual(num2words(
            3000000000, lang="he", construct=True), u'שלושת מיליארדי')
        self.assertEqual(num2words(
            3000000002, lang="he"), u'שלושה מיליארד ושתיים')
        self.assertEqual(num2words(
            3000000002, lang="he", construct=True), u'שלושה מיליארד ושתיים')
        self.assertEqual(num2words(10000000000, lang="he"), u'עשרה מיליארד')
        self.assertEqual(num2words(
            10000000000, lang="he", construct=True), 'עשרת מיליארדי')
        self.assertEqual(num2words(
            10000000002, lang="he"), u'עשרה מיליארד ושתיים')
        self.assertEqual(num2words(
            10000000002, lang="he", construct=True), 'עשרה מיליארד ושתיים')
        self.assertEqual(num2words(11000000000, lang="he"), u'אחד עשר מיליארד')
        self.assertEqual(num2words(
            11000000000, lang="he", construct=True), 'אחד עשר מיליארדי')

        self.assertEqual(num2words(1000000000000, lang="he"), u'טריליון')
        self.assertEqual(num2words(
            1000000000000, lang="he", construct=True), u'טריליון')
        self.assertEqual(num2words(
            1000000000002, lang="he"), u'טריליון ושתיים')
        self.assertEqual(num2words(
            1000000000002, lang="he", construct=True), u'טריליון ושתיים')
        self.assertEqual(num2words(2000000000000, lang="he"), u'שני טריליון')
        self.assertEqual(num2words(
            2000000000000, lang="he", construct=True), u'שני טריליוני')
        self.assertEqual(num2words(3000000000000, lang="he"), u'שלושה טריליון')
        self.assertEqual(num2words(
            3000000000000, lang="he", construct=True), u'שלושת טריליוני')
        self.assertEqual(num2words(
            3000000000002, lang="he"), u'שלושה טריליון ושתיים')
        self.assertEqual(num2words(
            3000000000002, lang="he", construct=True), u'שלושה טריליון ושתיים')
        self.assertEqual(num2words(10000000000000, lang="he"), u'עשרה טריליון')
        self.assertEqual(num2words(
            10000000000000, lang="he", construct=True), 'עשרת טריליוני')
        self.assertEqual(num2words(
            10000000000002, lang="he"), u'עשרה טריליון ושתיים')
        self.assertEqual(num2words(
            10000000000002, lang="he", construct=True), 'עשרה טריליון ושתיים')
        self.assertEqual(num2words(
            11000000000000, lang="he"), u'אחד עשר טריליון')
        self.assertEqual(num2words(
            11000000000000, lang="he", construct=True), 'אחד עשר טריליוני')

        self.assertEqual(num2words(999999999999999, lang="he"),
                         u'תשע מאות תשעים ותשעה טריליון '
                         u'תשע מאות תשעים ותשעה מיליארד '
                         u'תשע מאות תשעים ותשעה מיליון '
                         u'תשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשע')
        self.assertEqual(num2words(999999999999999, lang="he", gender='m'),
                         u'תשע מאות תשעים ותשעה טריליון '
                         u'תשע מאות תשעים ותשעה מיליארד '
                         u'תשע מאות תשעים ותשעה מיליון '
                         u'תשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשעה')
        self.assertEqual(num2words(999999999999999, lang="he", construct=True),
                         u'תשע מאות תשעים ותשעה טריליון '
                         u'תשע מאות תשעים ותשעה מיליארד '
                         u'תשע מאות תשעים ותשעה מיליון '
                         u'תשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשע')
        self.assertEqual(num2words(
            999999999999999, lang="he", gender='m', construct=True),
            u'תשע מאות תשעים ותשעה טריליון '
            u'תשע מאות תשעים ותשעה מיליארד '
            u'תשע מאות תשעים ותשעה מיליון '
            u'תשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשעה')

    def test_pluralize(self):
        n = Num2Word_HE()
        cr1, cr2 = n.CURRENCY_FORMS['ILS']
        self.assertEqual(n.pluralize(1, cr1), u'שקל')
        self.assertEqual(n.pluralize(2, cr1), u'שקלים')
        self.assertEqual(n.pluralize(1, cr2), u'אגורה')
        self.assertEqual(n.pluralize(2, cr2), u'אגורות')

        cr1, cr2 = n.CURRENCY_FORMS['USD']
        self.assertEqual(n.pluralize(1, cr1), u'דולר')
        self.assertEqual(n.pluralize(2, cr1), u'דולרים')
        self.assertEqual(n.pluralize(1, cr2), u'סנט')
        self.assertEqual(n.pluralize(2, cr2), u'סנטים')

    def test_to_currency(self):
        n = Num2Word_HE()
        self.assertEqual(n.to_currency(
            20.0, currency='ILS'), u'עשרים שקלים ואפס אגורות')
        self.assertEqual(n.to_currency(
            100.0, currency='ILS'), u'מאה שקלים ואפס אגורות')
        self.assertEqual(n.to_currency(
            100.50, currency='ILS'), u'מאה שקלים וחמישים אגורות')
        self.assertEqual(n.to_currency(
            101.51, currency='ILS'), u'מאה ואחד שקלים וחמישים ואחת אגורות')
        self.assertEqual(n.to_currency(
            -101.51, currency='ILS'),
            u'מינוס מאה ואחד שקלים וחמישים ואחת אגורות')
        self.assertEqual(n.to_currency(
            -101.51, currency='ILS', prefer_singular=True),
            u'מינוס מאה ואחד שקל וחמישים ואחת אגורות')
        self.assertEqual(n.to_currency(
            -101.51, currency='ILS', prefer_singular_cents=True),
            u'מינוס מאה ואחד שקלים וחמישים ואחת אגורה')
        self.assertEqual(n.to_currency(
            -101.51, currency='ILS', prefer_singular=True,
            prefer_singular_cents=True),
            u'מינוס מאה ואחד שקל וחמישים ואחת אגורה')
        self.assertEqual(n.to_currency(
            5.05, currency='ILS', prefer_singular=True,
            prefer_singular_cents=True), u'חמישה שקלים וחמש אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', prefer_singular=True,
            prefer_singular_cents=True), u'מינוס חמישה שקלים וחמש אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False),
            u'מינוס חמישה שקלים ו-05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator='ו'),
            u'מינוס חמישה שקלים ו-05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator='ו-'),
            u'מינוס חמישה שקלים ו-05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator=''),
            u'מינוס חמישה שקלים 05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator='ועוד '),
            u'מינוס חמישה שקלים ועוד 05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator=' ו'),
            u'מינוס חמישה שקלים ו-05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator=' ו-'),
            u'מינוס חמישה שקלים ו-05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator=' '),
            u'מינוס חמישה שקלים 05 אגורות')
        self.assertEqual(n.to_currency(
            -5.05, currency='ILS', cents=False, separator=' ועוד '),
            u'מינוס חמישה שקלים ועוד 05 אגורות')
        self.assertEqual(n.to_currency(
            1.01, currency='ILS'), u'שקל אחד ואגורה אחת')
        self.assertEqual(n.to_currency(
            -1.01, currency='ILS'), u'מינוס שקל אחד ואגורה אחת')
        self.assertEqual(n.to_currency(
            2.02, currency='ILS'), u'שני שקלים ושתי אגורות')
        self.assertEqual(n.to_currency(
            1002.02, currency='ILS'), u'אלף ושניים שקלים ושתי אגורות')
        self.assertEqual(n.to_currency(
            1000002.02, currency='ILS'), u'מיליון ושניים שקלים ושתי אגורות')
        self.assertEqual(n.to_currency(
            5.05, currency='USD'), u'חמישה דולרים וחמישה סנטים')
        self.assertEqual(n.to_currency(
            5.05, currency='USD', prefer_singular=True),
            u'חמישה דולר וחמישה סנטים')
        self.assertEqual(n.to_currency(
            5.05, currency='USD', prefer_singular_cents=True),
            u'חמישה דולרים וחמישה סנט')
        self.assertEqual(n.to_currency(
            5.05, currency='USD', prefer_singular=True,
            prefer_singular_cents=True), u'חמישה דולר וחמישה סנט')
        n.CURRENCY_FORMS['pruta'] = (('פרוטה', 'פרוטות'), ('מאית', 'מאיות'))
        self.assertEqual(n.to_currency(
            5.05, currency='pruta'), u'חמש פרוטות וחמש מאיות')

    def test_to_currency_errors(self):
        n = Num2Word_HE()
        with self.assertRaises(NotImplementedError):
            n.to_currency(1, '')

    def test_to_cardinal(self):
        n = Num2Word_HE()
        self.assertEqual(n.to_cardinal(1500), u'אלף וחמש מאות')
        self.assertEqual(n.to_cardinal(1501), u'אלף חמש מאות ואחת')
        self.assertEqual(num2words(1, lang='he'), u'אחת')
        self.assertEqual(num2words(1, lang='he', gender='m'), u'אחד')

    def test_to_ordinal(self):
        n = Num2Word_HE()
        self.assertEqual(n.to_ordinal(1001), u'האלף ואחד')
        self.assertEqual(n.to_ordinal(1500), u'האלף וחמש מאות')
        self.assertEqual(n.to_ordinal(1501), u'האלף חמש מאות ואחד')
        self.assertEqual(n.to_ordinal(
            1501, definite=True), u'האלף חמש מאות ואחד')
        self.assertEqual(n.to_ordinal(1), u'ראשון')
        self.assertEqual(n.to_ordinal(1, definite=True), u'הראשון')
        self.assertEqual(n.to_ordinal(1, gender='f'), u'ראשונה')
        self.assertEqual(n.to_ordinal(
            1, gender='f', definite=True), u'הראשונה')
        self.assertEqual(n.to_ordinal(10), u'עשירי')
        self.assertEqual(n.to_ordinal(10, definite=True), u'העשירי')
        self.assertEqual(n.to_ordinal(10, gender='f'), u'עשירית')
        self.assertEqual(n.to_ordinal(
            10, gender='f', definite=True), u'העשירית')
        self.assertEqual(n.to_ordinal(17), u'השבעה עשר')
        self.assertEqual(n.to_ordinal(17, definite=True), u'השבעה עשר')
        self.assertEqual(n.to_ordinal(17, gender='f'), u'השבע עשרה')
        self.assertEqual(n.to_ordinal(
            17, gender='f', definite=True), u'השבע עשרה')
        self.assertEqual(n.to_ordinal(0), u'האפס')
        self.assertEqual(n.to_ordinal(0, definite=True), u'האפס')
        self.assertEqual(n.to_ordinal(0, gender='f'), u'האפס')
        self.assertEqual(n.to_ordinal(0, gender='f', definite=True), u'האפס')
        self.assertEqual(n.to_ordinal(
            999999), u'התשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשעה')
        self.assertEqual(n.to_ordinal(
            999999, gender='f'),
            u'התשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשע')
        self.assertEqual(num2words(1, ordinal=True, lang='he'), u'ראשון')
        self.assertEqual(num2words(
            1, ordinal=True, lang='he', gender='f'), u'ראשונה')
        self.assertEqual(num2words(
            1, ordinal=True, lang='he', definite=True), u'הראשון')
        self.assertEqual(num2words(
            1, ordinal=True, lang='he', gender='f', definite=True), u'הראשונה')

    def test_to_ordinal_plural(self):
        n = Num2Word_HE()
        self.assertEqual(n.to_ordinal(1001, plural=True), u'האלף ואחד')
        self.assertEqual(n.to_ordinal(1500, plural=True), u'האלף וחמש מאות')
        self.assertEqual(n.to_ordinal(
            1501, plural=True), u'האלף חמש מאות ואחד')
        self.assertEqual(n.to_ordinal(
            1501, definite=True, plural=True), u'האלף חמש מאות ואחד')
        self.assertEqual(n.to_ordinal(1, plural=True), u'ראשונים')
        self.assertEqual(n.to_ordinal(
            1, definite=True, plural=True), u'הראשונים')
        self.assertEqual(n.to_ordinal(1, gender='f', plural=True), u'ראשונות')
        self.assertEqual(n.to_ordinal(
            1, gender='f', definite=True, plural=True), u'הראשונות')
        self.assertEqual(n.to_ordinal(10, plural=True), u'עשיריים')
        self.assertEqual(n.to_ordinal(
            10, definite=True, plural=True), u'העשיריים')
        self.assertEqual(n.to_ordinal(
            10, gender='f', plural=True), u'עשיריות')
        self.assertEqual(n.to_ordinal(
            10, gender='f', definite=True, plural=True), u'העשיריות')
        self.assertEqual(n.to_ordinal(17, plural=True), u'השבעה עשר')
        self.assertEqual(n.to_ordinal(
            17, definite=True, plural=True), u'השבעה עשר')
        self.assertEqual(n.to_ordinal(
            17, gender='f', plural=True), u'השבע עשרה')
        self.assertEqual(n.to_ordinal(
            17, gender='f', definite=True, plural=True), u'השבע עשרה')
        self.assertEqual(n.to_ordinal(0, plural=True), u'האפס')
        self.assertEqual(n.to_ordinal(0, definite=True, plural=True), u'האפס')
        self.assertEqual(n.to_ordinal(0, gender='f', plural=True), u'האפס')
        self.assertEqual(n.to_ordinal(
            0, gender='f', definite=True, plural=True), u'האפס')
        self.assertEqual(n.to_ordinal(999999, plural=True),
                         u'התשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשעה')
        self.assertEqual(n.to_ordinal(999999, gender='f', plural=True),
                         u'התשע מאות תשעים ותשעה אלף תשע מאות תשעים ותשע')
        self.assertEqual(num2words(
            1, ordinal=True, lang='he', plural=True), u'ראשונים')
        self.assertEqual(num2words(
            1, ordinal=True, lang='he', gender='f', plural=True), u'ראשונות')
        self.assertEqual(num2words(1, ordinal=True, lang='he',
                                   definite=True, plural=True), u'הראשונים')
        self.assertEqual(num2words(1, ordinal=True, lang='he', gender='f',
                                   definite=True, plural=True), u'הראשונות')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='he'), u'שתים עשרה נקודה חמש')
        self.assertEqual(num2words(
            12.51, lang='he'), u'שתים עשרה נקודה חמש אחת')
        self.assertEqual(num2words(
            12.53, lang='he'), u'שתים עשרה נקודה חמש שלוש')
        self.assertEqual(num2words(
            12.59, lang='he'), u'שתים עשרה נקודה חמש תשע')
        self.assertEqual(num2words(
            12.5, lang='he', gender='m'), u'שנים עשר נקודה חמש')
        self.assertEqual(num2words(
            12.51, lang='he', gender='m'), u'שנים עשר נקודה חמש אחת')
        self.assertEqual(num2words(
            12.53, lang='he', gender='m'), u'שנים עשר נקודה חמש שלוש')
        self.assertEqual(num2words(
            12.59, lang='he', gender='m'), u'שנים עשר נקודה חמש תשע')
        self.assertEqual(num2words(12.594132, lang='he', gender='m'),
                         u'שנים עשר נקודה חמש תשע ארבע אחת שלוש שתיים')

    def test_cardinal_float_precision(self):
        n = Num2Word_HE()
        self.assertEqual(n.to_cardinal_float("1.23"), 'אחת נקודה שתיים שלוש')
        n.precision = 1
        self.assertEqual(n.to_cardinal_float("1.2"), 'אחת נקודה שתיים')

    def test_error_to_cardinal_float(self):
        n = Num2Word_HE()
        with self.assertRaises(TypeError):
            n.to_cardinal_float("a")

    def test_overflow(self):
        n = Num2Word_HE()
        num2words(n.MAXVAL - 1, lang="he")
        num2words(n.MAXVAL - 1, ordinal=True, lang="he")

        with self.assertRaises(OverflowError):
            num2words(n.MAXVAL, lang="he")

        with self.assertRaises(OverflowError):
            num2words(n.MAXVAL, lang="he", ordinal=True)

        with self.assertRaises(OverflowError):
            int2word(n.MAXVAL)
