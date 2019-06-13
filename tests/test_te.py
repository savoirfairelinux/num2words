# -*- coding: utf-8 -*-

from unittest import TestCase

from num2words import num2words


class Num2WordsTETest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(42, lang="te"), u"నలభై రెండు")
        self.assertEqual(num2words(893, lang="te"), u"ఎనిమిది వందల తొంబై మూడు")
        self.assertEqual(
            num2words(1729, lang="te"), u"ఒక వేయి ఏడు వందల ఇరవై తొమ్మిది ")
        self.assertEqual(num2words(123, lang="te"), u"ఒక వంద ఇరవై  మూడు")
        self.assertEqual(num2words(32211, lang="te"),
        		u"ముప్పై రెండు వేల రెండు వందల పదకొండు")

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            num2words(3.14, lang="te"), 
            u"మూడుబిందువు ఒకటి నాలుగు"
            )
        self.assertEqual(num2words(1.61803, lang="te"),
                         u"ఒకటి బిందువు ఆరు ఒకటి ఎనిమిది సున్నా మూడు ")

    def test_ordinal(self):
        self.assertEqual(
            num2words(1, lang='te', to='ordinal'),
            u'ఒకటివ '
        )
        self.assertEqual(
            num2words(22, lang='te', to='ordinal'),
            u'ఇరవై రెండవ '
        )
        self.assertEqual(
            num2words(12, lang='te', to='ordinal'),
            u'పన్నెండవ'
        )
        self.assertEqual(
            num2words(130, lang='te', to='ordinal'),
            u'ఒక వంద ముప్పయ్యవ '
        )
        self.assertEqual(
            num2words(1003, lang='te', to='ordinal'),
            u'ఒక వెయ్యి  మూడవ'
        )

    def test_ordinal_num(self):
        self.assertEqual(
            num2words(2, lang="te", ordinal=True), u"రెండవ")
        self.assertEqual(num2words(5, lang="te", ordinal=True), u"అయిదవ ")
        self.assertEqual(
            num2words(16, lang="te", ordinal=True), u"పదహారవ ")
        self.assertEqual(
            num2words(113, lang="te", ordinal=True), u"ఒక వంద పదమూడవ")
