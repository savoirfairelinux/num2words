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

# ── reusable fixtures ───────────────────────────────────────────────────────


CARDINAL_CASES = [
    (0,    "nullus"),
    (1,    "ūnus"),
    (2,    "duo"),
    (3,    "trēs"),
    (4,    "quattuor"),
    (5,    "quīnque"),
    (6,    "sex"),
    (7,    "septem"),
    (8,    "octō"),
    (9,    "novem"),
    (10,   "decem"),
    (11,   "ūndecim"),
    (12,   "duodecim"),
    (13,   "tredecim"),
    (14,   "quattuordecim"),
    (15,   "quīndecim"),
    (16,   "sēdecim"),
    (17,   "septendecim"),
    (18,   "duodēvīgintī"),
    (19,   "ūndēvīgintī"),
    (20,   "vīgintī"),
    (21,   "vīgintī ūnus"),
    (24,   "vīgintī quattuor"),
    (30,   "trīgintā"),
    (50,   "quīnquāgintā"),
    (99,   "nōnāgintā novem"),
    (100,  "centum"),
    (101,  "centum ūnus"),
    (123,  "centum vīgintī trēs"),
    (199,  "centum nōnāgintā novem"),
    (200,  "ducentī"),
    (300,  "trecentī"),
    (400,  "quadringentī"),
    (500,  "quīngentī"),
    (600,  "sescentī"),
    (700,  "septingentī"),
    (800,  "octingentī"),
    (900,  "nōngentī"),
    (666,  "sescentī sexāgintā sex"),
    (999,  "nōngentī nōnāgintā novem"),
    (1000, "mīlle"),
    (1001, "mīlle ūnus"),
    (1999, "mīlle nōngentī nōnāgintā novem"),
    (2000, "duo mīlia"),
    (3000, "tria mīlia"),
    (3333, "tria mīlia trecentī trīgintā trēs"),
    (1_000_000,         "ūnus milio"),
    (2_000_000,         "duo miliones"),
    # The Loci-prompt example — every digit position exercised.
    (38_630_666,
     "trīgintā octō miliones sescenta trīgintā mīlia "
     "sescentī sexāgintā sex"),
    (1_000_000_000,     "ūnus miliardus"),
    (2_000_000_000,     "duo miliardi"),
    (1_000_000_000_000, "ūnus billio"),
    (2_000_000_000_000, "duo billiones"),
]


CARDINAL_ASCII_CASES = [
    (1,    "unus"),
    (3,    "tres"),
    (50,   "quinquaginta"),
    (200,  "ducenti"),
    (1000, "mille"),
    (2024, "duo milia viginti quattuor"),
    (38_630_666,
     "triginta octo miliones sescenta triginta milia "
     "sescenti sexaginta sex"),
]


GENDER_CASE_CASES = [
    # 1 — fully declined across 3 × 6
    (1, "m", "nom", "ūnus"),
    (1, "f", "nom", "ūna"),
    (1, "n", "nom", "ūnum"),
    (1, "m", "gen", "ūnīus"),
    (1, "f", "gen", "ūnīus"),
    (1, "n", "gen", "ūnīus"),
    (1, "m", "dat", "ūnī"),
    (1, "m", "acc", "ūnum"),
    (1, "f", "acc", "ūnam"),
    (1, "m", "abl", "ūnō"),
    (1, "f", "abl", "ūnā"),          # ← key macron distinction vs ūna
    (1, "n", "abl", "ūnō"),
    (1, "m", "voc", "ūne"),
    (1, "f", "voc", "ūna"),
    (1, "n", "voc", "ūnum"),
    # 2 — "duo / duae / duo"
    (2, "m", "nom", "duo"),
    (2, "f", "nom", "duae"),
    (2, "n", "nom", "duo"),
    (2, "m", "gen", "duōrum"),
    (2, "f", "gen", "duārum"),
    (2, "n", "gen", "duōrum"),
    (2, "m", "acc", "duōs"),
    (2, "f", "acc", "duās"),
    (2, "n", "acc", "duo"),
    (2, "m", "abl", "duōbus"),
    (2, "f", "abl", "duābus"),
    (2, "n", "abl", "duōbus"),
    (2, "m", "voc", "duo"),
    # 3 — "trēs / trēs / tria"
    (3, "m", "nom", "trēs"),
    (3, "f", "nom", "trēs"),
    (3, "n", "nom", "tria"),
    (3, "m", "gen", "trium"),
    (3, "n", "abl", "tribus"),
    (3, "m", "voc", "trēs"),
    # 4..99 are invariant (macrons in the lemma stick)
    (4, "f", "abl", "quattuor"),
    (37, "n", "gen", "trīgintā septem"),
    # 100 invariant in the singular
    (100, "f", "abl", "centum"),
    # Hundreds 200..900 — fully declined like 1st/2nd-decl. adjectives
    (200, "m", "nom", "ducentī"),
    (200, "f", "nom", "ducentae"),
    (200, "n", "nom", "ducenta"),
    (200, "m", "gen", "ducentōrum"),
    (200, "f", "gen", "ducentārum"),
    (200, "n", "abl", "ducentīs"),
    (200, "m", "acc", "ducentōs"),
    (200, "f", "acc", "ducentās"),
    (600, "n", "abl", "sescentīs"),
    (900, "f", "nom", "nōngentae"),
    (900, "m", "voc", "nōngentī"),
    # Higher numbers: gender/case applies to the final <1000 group
    # (the implicit head noun); higher units use their own gender.
    (2_001,         "f", "nom", "duo mīlia ūna"),
    (1_000_000_001, "f", "nom", "ūnus miliardus ūna"),
]


MILIA_CASE_CASES = [
    (2000, "nom", "duo mīlia"),
    (2000, "gen", "duo mīlium"),
    (2000, "dat", "duo mīlibus"),
    (2000, "acc", "duo mīlia"),
    (2000, "abl", "duo mīlibus"),
    (2000, "voc", "duo mīlia"),
    (3000, "abl", "tria mīlibus"),
]


YEAR_CASES = [
    (1,    "ūnus"),
    (44,   "quadrāgintā quattuor"),
    (476,  "quadringentī septuāgintā sex"),
    (1492, "mīlle quadringentī nōnāgintā duo"),
    (2024, "duo mīlia vīgintī quattuor"),
    (-44,  "ante Chrīstum quadrāgintā quattuor"),
    (-753, "ante Chrīstum septingentī quīnquāgintā trēs"),
]


ORDINAL_CASES = [
    (1,    "prīmus"),
    (2,    "secundus"),
    (3,    "tertius"),
    (4,    "quārtus"),
    (5,    "quīntus"),
    (6,    "sextus"),
    (7,    "septimus"),
    (8,    "octāvus"),
    (9,    "nōnus"),
    (10,   "decimus"),
    (11,   "ūndecimus"),
    (12,   "duodecimus"),
    (18,   "duodēvīcēsimus"),
    (19,   "ūndēvīcēsimus"),
    (20,   "vīcēsimus"),
    (50,   "quīnquāgēsimus"),
    (100,  "centēsimus"),
    (1000, "mīllēsimus"),
]


ORDINAL_GENDER_CASE_CASES = [
    (1, "f", "nom", "prīma"),
    (1, "n", "nom", "prīmum"),
    (1, "m", "gen", "prīmī"),
    (1, "f", "abl", "prīmā"),
    (2, "n", "abl", "secundō"),
    (3, "f", "acc", "tertiam"),
    (10, "n", "gen", "decimī"),
    # Compound ordinal (13th) — both head and tail inflect
    (13, "f", "nom", "tertia decima"),
    (13, "m", "abl", "tertiō decimō"),
]


ROMAN_CASES = [
    (1,    "I"),
    (4,    "IV"),
    (5,    "V"),
    (9,    "IX"),
    (10,   "X"),
    (40,   "XL"),
    (49,   "XLIX"),
    (90,   "XC"),
    (100,  "C"),
    (400,  "CD"),
    (1999, "MCMXCIX"),
    (2024, "MMXXIV"),
    (3999, "MMMCMXCIX"),
]


# ── tests ───────────────────────────────────────────────────────────────────


class Num2WordsLATest(TestCase):
    """Latin number-to-words coverage. Default citation form is
    masculine nominative with Classical macrons; opt out of macrons
    with ``macrons=False`` for plain ASCII."""

    def test_cardinal(self):
        for n, expected in CARDINAL_CASES:
            with self.subTest(n=n):
                self.assertEqual(num2words(n, lang="la"), expected)

    def test_cardinal_ascii(self):
        for n, expected in CARDINAL_ASCII_CASES:
            with self.subTest(n=n):
                self.assertEqual(
                    num2words(n, lang="la", macrons=False), expected
                )

    def test_macrons_strip_yields_pure_ascii(self):
        """Every long vowel introduced by the tables must round-trip
        cleanly through ``macrons=False`` (no stray non-ASCII left)."""
        for n in (0, 1, 3, 8, 11, 50, 100, 200, 666, 1000, 38_630_666):
            with self.subTest(n=n):
                plain = num2words(n, lang="la", macrons=False)
                plain.encode("ascii")    # raises if any byte > 0x7F

    def test_cardinal_gender_case(self):
        for n, gender, case, expected in GENDER_CASE_CASES:
            with self.subTest(n=n, gender=gender, case=case):
                self.assertEqual(
                    num2words(n, lang="la", gender=gender, case=case),
                    expected,
                )

    def test_milia_case_inflection(self):
        for n, case, expected in MILIA_CASE_CASES:
            with self.subTest(n=n, case=case):
                self.assertEqual(
                    num2words(n, lang="la", gender="n", case=case),
                    expected,
                )

    def test_negative(self):
        self.assertEqual(num2words(-7, lang="la"), "minus septem")
        self.assertEqual(
            num2words(-1_000_000, lang="la"), "minus ūnus milio"
        )
        # Negative + gender/case kwargs propagate through the recursive call.
        self.assertEqual(
            num2words(-1, lang="la", gender="f", case="abl"), "minus ūnā"
        )

    def test_decimal_float(self):
        # 3.14 → "trēs virgula ūnus quattuor" — base-class behaviour
        # (digit-by-digit after the pointword).
        result = num2words(3.14, lang="la")
        self.assertTrue(result.startswith("trēs virgula"))
        tail = result.split("virgula", 1)[1]
        self.assertIn("ūnus", tail)
        self.assertIn("quattuor", tail)

    def test_decimal_float_ascii(self):
        result = num2words(3.14, lang="la", macrons=False)
        self.assertTrue(result.startswith("tres virgula"))

    def test_overflow_raises(self):
        with self.assertRaises(OverflowError):
            num2words(10 ** 18, lang="la")

    def test_invalid_gender(self):
        with self.assertRaisesRegex(ValueError, r"gender must be"):
            num2words(1, lang="la", gender="x")

    def test_invalid_case(self):
        with self.assertRaisesRegex(ValueError, r"case must be"):
            num2words(1, lang="la", case="bogus")

    def test_year(self):
        for year, expected in YEAR_CASES:
            with self.subTest(year=year):
                self.assertEqual(
                    num2words(year, lang="la", to="year"), expected
                )

    def test_year_ascii(self):
        self.assertEqual(
            num2words(2024, lang="la", to="year", macrons=False),
            "duo milia viginti quattuor",
        )
        self.assertEqual(
            num2words(-44, lang="la", to="year", macrons=False),
            "ante Christum quadraginta quattuor",
        )

    def test_ordinal_masc_nom(self):
        for n, expected in ORDINAL_CASES:
            with self.subTest(n=n):
                self.assertEqual(
                    num2words(n, lang="la", to="ordinal"), expected
                )

    def test_ordinal_gender_case(self):
        for n, gender, case, expected in ORDINAL_GENDER_CASE_CASES:
            with self.subTest(n=n, gender=gender, case=case):
                self.assertEqual(
                    num2words(n, lang="la", to="ordinal",
                              gender=gender, case=case),
                    expected,
                )

    def test_ordinal_falls_back_to_cardinal_for_compounds(self):
        # 21 isn't in _ORDINALS_LOW → returns the cardinal.
        self.assertEqual(
            num2words(21, lang="la", to="ordinal"),
            num2words(21, lang="la"),
        )

    def test_ordinal_ascii(self):
        self.assertEqual(
            num2words(1, lang="la", to="ordinal", macrons=False), "primus"
        )
        self.assertEqual(
            num2words(20, lang="la", to="ordinal", macrons=False),
            "vicesimus",
        )

    def test_ordinal_num_roman(self):
        for n, expected in ROMAN_CASES:
            with self.subTest(n=n):
                self.assertEqual(
                    num2words(n, lang="la", to="ordinal_num"), expected
                )

    def test_ordinal_num_above_3999_falls_back_to_digits(self):
        # Romans didn't standardise notation > 3999; we fall back to
        # digits (the overline convention can't be represented in ASCII).
        self.assertEqual(
            num2words(4000, lang="la", to="ordinal_num"), "4000"
        )

    def test_loci_examples(self):
        """Three concrete cases from a real-world consumer of this
        library — every digit position exercised."""
        self.assertEqual(num2words(1, lang="la", macrons=False), "unus")
        self.assertEqual(
            num2words(50, lang="la", macrons=False), "quinquaginta"
        )
        self.assertEqual(
            num2words(38_630_666, lang="la", macrons=False),
            "triginta octo miliones sescenta triginta milia "
            "sescenti sexaginta sex",
        )
