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

"""
Test suite for Num2Word_UZ (O'zbek tili, lotin yozuvi).

Struktura test_en_ng.py asosida qurilgan:
  - test_to_cardinal  : butun va o'nli sonlar
  - test_negative     : manfiy sonlar
  - test_to_ordinal   : tartib sonlar (-inchi / -nchi)
  - test_to_currency  : valyuta (UZS, USD)
"""

from unittest import TestCase

# -------------------------------------------------------------------
# To run standalone (without installing lang_UZ into num2words package):
#
#   python -m pytest test_uz.py -v
#
# To run after installing:
#   from num2words import num2words
#   and replace uz.to_cardinal(x) with num2words(x, lang='uz')
# -------------------------------------------------------------------

import sys
import os
import importlib.util

# --------------- bootstrap: resolve lang_UZ.py location -------------
# Folder layout inside the num2words source tree:
#
#   num2words-0.5.14/
#   ├── num2words/
#   │   ├── __init__.py
#   │   ├── base.py
#   │   ├── lang_UZ.py   ← place the file here
#   │   └── ...
#   └── tests/
#       └── test_uz.py   ← this file
#
# We locate num2words/ relative to this test file's directory.

_tests_dir  = os.path.dirname(os.path.abspath(__file__))
_pkg_dir    = os.path.join(_tests_dir, '..', 'num2words')
_lang_path  = os.path.normpath(os.path.join(_pkg_dir, 'lang_UZ.py'))

if not os.path.isfile(_lang_path):
    raise FileNotFoundError(
        f"\n\nCould not find lang_UZ.py at:\n  {_lang_path}\n\n"
        "Please copy lang_UZ.py into the num2words/ package folder "
        "(next to base.py, lang_DE.py, etc.) and try again."
    )

import num2words.base as _base
import num2words.utils as _utils

_spec = importlib.util.spec_from_file_location("num2words.lang_UZ", _lang_path)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

_uz = _mod.Num2Word_UZ()
# --------------------------------------------------------------------


class Num2WordsUZCardinalTest(TestCase):
    """to_cardinal() — kardinal (miqdor) sonlar"""

    def setUp(self):
        self.n = _uz

    # --- nol ---
    def test_zero(self):
        self.assertEqual(self.n.to_cardinal(0), "nol")

    # --- birliklar (1–9) ---
    def test_ones(self):
        self.assertEqual(self.n.to_cardinal(1), "bir")
        self.assertEqual(self.n.to_cardinal(5), "besh")
        self.assertEqual(self.n.to_cardinal(9), "to'qqiz")

    # --- o'nliklar (10–19) ---
    def test_ten(self):
        self.assertEqual(self.n.to_cardinal(10), "o'n")

    def test_teens(self):
        self.assertEqual(self.n.to_cardinal(11), "o'n bir")
        self.assertEqual(self.n.to_cardinal(12), "o'n ikki")
        self.assertEqual(self.n.to_cardinal(15), "o'n besh")
        self.assertEqual(self.n.to_cardinal(19), "o'n to'qqiz")

    # --- yigirma–to'qson ---
    def test_tens(self):
        self.assertEqual(self.n.to_cardinal(20), "yigirma")
        self.assertEqual(self.n.to_cardinal(21), "yigirma bir")
        self.assertEqual(self.n.to_cardinal(30), "o'ttiz")
        self.assertEqual(self.n.to_cardinal(40), "qirq")
        self.assertEqual(self.n.to_cardinal(50), "ellik")
        self.assertEqual(self.n.to_cardinal(60), "oltmish")
        self.assertEqual(self.n.to_cardinal(70), "yetmish")
        self.assertEqual(self.n.to_cardinal(80), "sakson")
        self.assertEqual(self.n.to_cardinal(90), "to'qson")
        self.assertEqual(self.n.to_cardinal(99), "to'qson to'qqiz")

    # --- yuzliklar ---
    def test_hundreds(self):
        self.assertEqual(self.n.to_cardinal(100), "yuz")
        self.assertEqual(self.n.to_cardinal(101), "bir yuz bir")
        self.assertEqual(self.n.to_cardinal(111), "bir yuz o'n bir")
        self.assertEqual(self.n.to_cardinal(200), "ikki yuz")
        self.assertEqual(self.n.to_cardinal(500), "besh yuz")
        self.assertEqual(
            self.n.to_cardinal(999),
            "to'qqiz yuz to'qson to'qqiz"
        )

    # --- mingliklar ---
    def test_thousands(self):
        self.assertEqual(self.n.to_cardinal(1000),  "ming")
        self.assertEqual(self.n.to_cardinal(1001),  "bir ming bir")
        self.assertEqual(self.n.to_cardinal(1100),  "bir ming bir yuz")
        self.assertEqual(
            self.n.to_cardinal(1999),
            "bir ming to'qqiz yuz to'qson to'qqiz"
        )
        self.assertEqual(self.n.to_cardinal(2000),   "ikki ming")
        self.assertEqual(self.n.to_cardinal(10000),  "o'n ming")
        self.assertEqual(self.n.to_cardinal(100000), "bir yuz ming")

    # --- millionlar va undan katta ---
    def test_large_numbers(self):
        self.assertEqual(self.n.to_cardinal(1_000_000),     "million")
        self.assertEqual(self.n.to_cardinal(1_000_000_000), "milliard")
        self.assertEqual(
            self.n.to_cardinal(1_234_567),
            "bir million ikki yuz o'ttiz to'rt ming besh yuz oltmish yetti"
        )

    # --- o'nli kasrlar ---
    def test_decimal(self):
        self.assertEqual(self.n.to_cardinal(3.14),  "uch butun o'n to'rt")
        self.assertEqual(self.n.to_cardinal(0.5),   "nol butun besh")
        self.assertEqual(self.n.to_cardinal(0.05),  "nol butun nol besh")
        self.assertEqual(self.n.to_cardinal(10.001),"o'n butun nol nol bir")


class Num2WordsUZNegativeTest(TestCase):
    """Manfiy sonlar"""

    def setUp(self):
        self.n = _uz

    def test_negative_small(self):
        self.assertEqual(self.n.to_cardinal(-3),   "minus uch")
        self.assertEqual(self.n.to_cardinal(-1),   "minus bir")

    def test_negative_hundred(self):
        self.assertEqual(self.n.to_cardinal(-100), "minus yuz")

    def test_negative_large(self):
        self.assertEqual(
            self.n.to_cardinal(-1234),
            "minus bir ming ikki yuz o'ttiz to'rt"
        )


class Num2WordsUZOrdinalTest(TestCase):
    """to_ordinal() — tartib sonlar"""

    def setUp(self):
        self.n = _uz

    # Undosh bilan tugagan so'zlarga "-inchi"
    def test_ordinal_consonant_ending(self):
        self.assertEqual(self.n.to_ordinal(1),  "birinchi")    # bir → birinchi
        self.assertEqual(self.n.to_ordinal(2),  "ikkinchi")    # ikki → ikkinchi
        self.assertEqual(self.n.to_ordinal(3),  "uchinchi")    # uch → uchinchi
        self.assertEqual(self.n.to_ordinal(4),  "to'rtinchi")  # to'rt → to'rtinchi
        self.assertEqual(self.n.to_ordinal(8),  "sakkizinchi") # sakkiz → sakkizinchi
        self.assertEqual(self.n.to_ordinal(10), "o'ninchi")    # o'n → o'ninchi
        self.assertEqual(self.n.to_ordinal(30), "o'ttizinchi") # o'ttiz → o'ttizinchi
        self.assertEqual(self.n.to_ordinal(40), "qirqinchi")   # qirq → qirqinchi
        self.assertEqual(self.n.to_ordinal(100),"yuzinchi")    # yuz → yuzinchi

    # Unli bilan tugagan so'zlarga "-nchi"
    def test_ordinal_vowel_ending(self):
        self.assertEqual(self.n.to_ordinal(5),  "beshinchi")   # besh → beshinchi
        self.assertEqual(self.n.to_ordinal(20), "yigirmanchi") # yigirma → yigirmanchi
        self.assertEqual(self.n.to_ordinal(50), "ellikinchi")  # ellik → ellikinchi

    # Qo'shma tartib sonlar
    def test_ordinal_compound(self):
        self.assertEqual(self.n.to_ordinal(11), "o'n birinchi")
        self.assertEqual(self.n.to_ordinal(15), "o'n beshinchi")
        self.assertEqual(self.n.to_ordinal(19), "o'n to'qqizinchi")
        self.assertEqual(self.n.to_ordinal(21), "yigirma birinchi")
        self.assertEqual(self.n.to_ordinal(101),"bir yuz birinchi")

    def test_ordinal_thousands(self):
        self.assertEqual(self.n.to_ordinal(1000),    "minginchi")
        self.assertEqual(self.n.to_ordinal(1_000_000),"millioninchi")


class Num2WordsUZCurrencyTest(TestCase):
    """
    to_currency() — valyuta.

    Ingliz test_en_ng.py bilan bir xil tuzilma:
      UZS (so'm / tiyin) va USD (dollar / sent) testlari.
    """

    def setUp(self):
        self.n = _uz

    # ----------------------------------------------------------------
    # UZS — so'm va tiyin
    # ----------------------------------------------------------------

    def test_uzs_zero(self):
        self.assertEqual(
            self.n.to_currency(0, currency='UZS'),
            "nol so'm, nol tiyin"
        )

    def test_uzs_whole(self):
        self.assertEqual(
            self.n.to_currency(1.00, currency='UZS'),
            "bir so'm, nol tiyin"
        )
        self.assertEqual(
            self.n.to_currency(2000.00, currency='UZS'),
            "ikki ming so'm, nol tiyin"
        )

    def test_uzs_one_tiyin(self):
        self.assertEqual(
            self.n.to_currency(1.01, currency='UZS'),
            "bir so'm, bir tiyin"
        )
        self.assertEqual(
            self.n.to_currency(4.01, currency='UZS'),
            "to'rt so'm, bir tiyin"
        )

    def test_uzs_ten_tiyin(self):
        self.assertEqual(
            self.n.to_currency(1.10, currency='UZS'),
            "bir so'm, o'n tiyin"
        )

    def test_uzs_partial_tiyin(self):
        # 38.4 → 38 so'm, 40 tiyin
        self.assertEqual(
            self.n.to_currency(38.40, currency='UZS'),
            "o'ttiz sakkiz so'm, qirq tiyin"
        )
        # 158.3 → 158 so'm, 30 tiyin
        self.assertEqual(
            self.n.to_currency(158.30, currency='UZS'),
            "bir yuz ellik sakkiz so'm, o'ttiz tiyin"
        )
        # 0.50 → nol so'm, ellik tiyin
        self.assertEqual(
            self.n.to_currency(0.50, currency='UZS'),
            "nol so'm, ellik tiyin"
        )

    def test_uzs_large_amount(self):
        self.assertEqual(
            self.n.to_currency(4778.00, currency='UZS'),
            "to'rt ming yetti yuz yetmish sakkiz so'm, nol tiyin"
        )
        self.assertEqual(
            self.n.to_currency(999999.99, currency='UZS'),
            "to'qqiz yuz to'qson to'qqiz ming to'qqiz yuz to'qson to'qqiz "
            "so'm, to'qson to'qqiz tiyin"
        )

    # ----------------------------------------------------------------
    # USD — dollar va sent
    # ----------------------------------------------------------------

    def test_usd_whole(self):
        self.assertEqual(
            self.n.to_currency(1.00, currency='USD'),
            "bir dollar, nol sent"
        )
        self.assertEqual(
            self.n.to_currency(100.00, currency='USD'),
            "yuz dollar, nol sent"
        )

    def test_usd_with_cents(self):
        self.assertEqual(
            self.n.to_currency(1.01, currency='USD'),
            "bir dollar, bir sent"
        )

    def test_usd_large(self):
        self.assertEqual(
            self.n.to_currency(4778.00, currency='USD'),
            "to'rt ming yetti yuz yetmish sakkiz dollar, nol sent"
        )


if __name__ == "__main__":
    import unittest
    unittest.main()
