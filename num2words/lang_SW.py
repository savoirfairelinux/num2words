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

from __future__ import print_function, unicode_literals

from decimal import Decimal

# Units 0-9.
UNITS = {
    0: "sifuri",
    1: "moja",
    2: "mbili",
    3: "tatu",
    4: "nne",
    5: "tano",
    6: "sita",
    7: "saba",
    8: "nane",
    9: "tisa",
}

# Tens 10-90.  Compound numbers join the ten and the unit with "na".
TENS = {
    1: "kumi",
    2: "ishirini",
    3: "thelathini",
    4: "arobaini",
    5: "hamsini",
    6: "sitini",
    7: "sabini",
    8: "themanini",
    9: "tisini",
}

# Scale words, using the international (long-form) system: each step is a
# group of three decimal digits.
SCALE = {
    1: "elfu",       # 10 ** 3
    2: "milioni",    # 10 ** 6
    3: "bilioni",    # 10 ** 9
    4: "trilioni",   # 10 ** 12
    5: "kvadrilioni",  # 10 ** 15
}

# Ordinal forms.  Swahili ordinals are formed analytically with the
# possessive "-a" connector, e.g. "ya kwanza" (first), "ya pili" (second).
# The bare ("ya"-less) stems are stored here; "kwanza" and the borrowed
# "sufuri" replace the cardinal roots for first/zeroth.
ORDINAL_STEMS = {
    0: "sufuri",
    1: "kwanza",
    2: "pili",
    3: "tatu",
    4: "nne",
    5: "tano",
    6: "sita",
    7: "saba",
    8: "nane",
    9: "tisa",
}


class Num2Word_SW(object):
    """Swahili (Kiswahili) number-to-words converter.

    Cardinal numbers follow the regular Swahili composition rules:

    * Units and tens are joined by the coordinator ``na`` ("and"),
      e.g. ``arobaini na saba`` (47).
    * Hundreds are ``mia`` followed by the multiplier, e.g. ``mia mbili``
      (200).  When the hundred multiplier is one and a remainder follows,
      the ``moja`` is dropped: ``mia na moja`` (101), ``mia na kumi``
      (110).
    * Thousands and larger groups keep their multiplier (``elfu moja`` for
      1000) and are linked to the rest with ``na``.
    """

    negword = "kasoro"
    pointword = "pointi"
    errmsg_floatord = "Cannot treat float %s as ordinal."
    errmsg_negord = "Cannot treat negative number %s as ordinal."
    errmsg_toobig = "abs(%s) must be less than %s."
    MAXVAL = 10 ** 18

    def str_to_number(self, value):
        return Decimal(value)

    def _two_digits(self, number):
        """Spell a number in the range 1..99 (0 returns an empty list)."""
        words = []
        tens, unit = divmod(number, 10)
        if tens:
            words.append(TENS[tens])
        if unit:
            if tens:
                words.append("na")
            words.append(UNITS[unit])
        return words

    def _three_digits(self, number):
        """Spell a number in the range 1..999."""
        hundreds, rest = divmod(number, 100)
        if not hundreds:
            return self._two_digits(rest)

        words = ["mia"]
        if hundreds == 1:
            # "mia moja" alone, but "mia na ..." when a remainder follows.
            if rest:
                words.append("na")
                words.extend(self._two_digits(rest))
            else:
                words.append(UNITS[1])
        else:
            words.append(UNITS[hundreds])
            if rest:
                words.append("na")
                words.extend(self._two_digits(rest))
        return words

    def _split_groups(self, number):
        """Split an integer into groups of three digits, least significant
        first.  ``1234567`` -> ``[567, 234, 1]``."""
        groups = []
        while number:
            number, group = divmod(number, 1000)
            groups.append(group)
        return groups

    def _int_to_words(self, number):
        if number == 0:
            return UNITS[0]

        groups = self._split_groups(number)
        chunks = []
        # Walk from the most significant group down to the units group.
        for index in range(len(groups) - 1, -1, -1):
            group = groups[index]
            if not group:
                continue
            group_words = self._three_digits(group)
            if index:
                # Prefix the scale word: "elfu", "milioni", ...
                chunks.append(" ".join([SCALE[index]] + group_words))
            else:
                chunks.append(" ".join(group_words))
        # Successive groups are joined by the coordinator "na".
        return " na ".join(chunks)

    def to_cardinal(self, number):
        if abs(number) >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))

        if isinstance(number, float):
            return self._float_to_words(number)
        if (isinstance(number, Decimal)
                and number != number.to_integral_value()):
            return self._float_to_words(number)

        number = int(number)
        if number < 0:
            return "%s %s" % (self.negword, self._int_to_words(abs(number)))
        return self._int_to_words(number)

    def _float_to_words(self, number):
        negative = number < 0
        number = abs(number)
        left = int(number)
        # Render the fractional part digit by digit after "pointi".
        fraction = str(number).split(".")[1] if "." in str(number) else ""
        words = [self._int_to_words(left), self.pointword]
        for digit in fraction:
            words.append(UNITS[int(digit)])
        result = " ".join(words)
        if negative:
            result = "%s %s" % (self.negword, result)
        return result

    def verify_ordinal(self, value):
        if not value == int(value):
            raise TypeError(self.errmsg_floatord % value)
        if not abs(value) == value:
            raise TypeError(self.errmsg_negord % value)

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        number = int(number)
        if number == 0:
            return "ya %s" % ORDINAL_STEMS[0]
        if number == 1:
            return "ya %s" % ORDINAL_STEMS[1]
        if number == 2:
            return "ya %s" % ORDINAL_STEMS[2]
        # For three and above the cardinal form is reused after "ya".
        return "ya %s" % self._int_to_words(number)

    def to_ordinal_num(self, number):
        self.verify_ordinal(number)
        return "ya %d" % int(number)

    def to_year(self, value, **kwargs):
        return self.to_cardinal(value)

    def to_currency(self, value, currency="TZS", **kwargs):
        names = {
            "TZS": ("shilingi", "senti"),
            "KES": ("shilingi", "senti"),
            "USD": ("dola", "senti"),
        }
        main, frac = names.get(currency, names["TZS"])
        left = int(value)
        cents = int(round((abs(value) - abs(left)) * 100))
        result = "%s %s" % (self.to_cardinal(left), main)
        if cents:
            result += " na %s %s" % (self.to_cardinal(cents), frac)
        return result
