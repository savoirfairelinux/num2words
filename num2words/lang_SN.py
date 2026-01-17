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
Shona (chiShona) number to words conversion.

Shona is a Bantu language spoken by approximately 7 million people,
primarily in Zimbabwe where it is an official language alongside
English and Ndebele.
"""

from __future__ import division, print_function, unicode_literals

from .base import Num2Word_Base


class Num2Word_SN(Num2Word_Base):
    """Convert numbers to Shona words."""

    CURRENCY_FORMS = {
        'ZWL': (('dora', 'madora'), ('sendi', 'masendi')),
        'USD': (('dora', 'madora'), ('sendi', 'masendi')),
    }

    def setup(self):
        super(Num2Word_SN, self).setup()

        self.negword = "mainasi "
        self.pointword = "poindi"
        self.exclude_title = ["ne", "poindi", "mainasi"]

        # Units 0-9
        self.ones = [
            "chiposhi",    # 0
            "motsi",       # 1
            "piri",        # 2
            "tatu",        # 3
            "ina",         # 4
            "shanu",       # 5
            "tanhatu",     # 6
            "nomwe",       # 7
            "sere",        # 8
            "pfumbamwe",   # 9
        ]

        # 10-19
        self.teens = [
            "gumi",              # 10
            "gumi nemotsi",      # 11
            "gumi nepiri",       # 12
            "gumi netatu",       # 13
            "gumi neina",        # 14
            "gumi neshanu",      # 15
            "gumi netanhatu",    # 16
            "gumi nenomwe",      # 17
            "gumi nesere",       # 18
            "gumi nepfumbamwe",  # 19
        ]

        # Tens 20-90
        self.tens = [
            "",                    # 0 (placeholder)
            "gumi",                # 10
            "makumi maviri",       # 20
            "makumi matatu",       # 30
            "makumi mana",         # 40
            "makumi mashanu",      # 50
            "makumi matanhatu",    # 60
            "makumi manomwe",      # 70
            "makumi masere",       # 80
            "makumi mapfumbamwe",  # 90
        ]

        # Ordinal mappings
        self.ords = {
            "motsi": "wokutanga",
            "piri": "wechipiri",
            "tatu": "wechitatu",
            "ina": "wechina",
            "shanu": "wechishanu",
            "tanhatu": "wechitanhatu",
            "nomwe": "wechinomwe",
            "sere": "wechisere",
            "pfumbamwe": "wechipfumbamwe",
            "gumi": "wechigumi",
        }

        self.MAXVAL = 10 ** 15  # Up to trillions

    def _int_to_word(self, n, level=0):
        """
        Convert an integer to its Shona word representation.

        Args:
            n: Integer to convert
            level: Recursion level for handling larger numbers

        Returns:
            String representation of the number in Shona
        """
        if n < 0:
            return self.negword.strip() + " " + self._int_to_word(-n, level)

        if n == 0:
            return self.ones[0] if level == 0 else ""

        if n < 10:
            return self.ones[n]

        if n < 20:
            return self.teens[n - 10]

        if n < 100:
            tens_digit = n // 10
            ones_digit = n % 10
            if ones_digit == 0:
                return self.tens[tens_digit]
            else:
                return self.tens[tens_digit] + " ne" + self.ones[ones_digit]

        if n < 1000:
            hundreds = n // 100
            remainder = n % 100
            if hundreds == 1:
                result = "zana"
            else:
                result = "mazana " + self.ones[hundreds]
            if remainder:
                result += " ne" + self._int_to_word(remainder, level + 1)
            return result

        if n < 1000000:
            thousands = n // 1000
            remainder = n % 1000
            if thousands == 1:
                result = "chiuru"
            else:
                result = "zviuru " + self._int_to_word(thousands, level + 1)
            if remainder:
                result += " ne" + self._int_to_word(remainder, level + 1)
            return result

        if n < 1000000000:
            millions = n // 1000000
            remainder = n % 1000000
            if millions == 1:
                result = "miriyoni"
            else:
                result = "mamiriyoni " + self._int_to_word(millions, level + 1)
            if remainder:
                result += " ne" + self._int_to_word(remainder, level + 1)
            return result

        if n < 1000000000000:
            billions = n // 1000000000
            remainder = n % 1000000000
            if billions == 1:
                result = "bhiriyoni"
            else:
                result = "mabhiriyoni " + self._int_to_word(billions, level + 1)
            if remainder:
                result += " ne" + self._int_to_word(remainder, level + 1)
            return result

        if n < 1000000000000000:
            trillions = n // 1000000000000
            remainder = n % 1000000000000
            if trillions == 1:
                result = "tiriyoni"
            else:
                result = "matiriyoni " + self._int_to_word(trillions, level + 1)
            if remainder:
                result += " ne" + self._int_to_word(remainder, level + 1)
            return result

        raise OverflowError(self.errmsg_toobig % (n, self.MAXVAL))

    def to_cardinal(self, value):
        """Convert a number to its cardinal representation in Shona."""
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        return self.title(self._int_to_word(int(value)))

    def to_cardinal_float(self, value):
        """Convert a float to its Shona word representation."""
        try:
            value = float(value)
        except (ValueError, TypeError, AttributeError):
            raise TypeError(self.errmsg_nonnum % value)

        pre, post = self.float2tuple(value)
        post = str(post)
        post = '0' * (self.precision - len(post)) + post

        out = [self.to_cardinal(pre)]
        if value < 0 and pre == 0:
            out = [self.negword.strip()] + out

        if self.precision:
            out.append(self.title(self.pointword))

        for i in range(self.precision):
            curr = int(post[i])
            out.append(self.to_cardinal(curr))

        return " ".join(out)

    def to_ordinal(self, value):
        """Convert a number to its ordinal representation in Shona."""
        self.verify_ordinal(value)
        cardinal = self.to_cardinal(value)

        # Split the cardinal and get the last word
        words = cardinal.split()
        last_word = words[-1]

        # Check if we have a special ordinal form
        if last_word in self.ords:
            words[-1] = self.ords[last_word]
        else:
            # Default ordinal suffix
            words[-1] = "wechi" + last_word

        return " ".join(words)

    def to_ordinal_num(self, value):
        """Convert a number to ordinal number format (e.g., 1st, 2nd)."""
        self.verify_ordinal(value)
        # In Shona, we append a suffix indicator
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def pluralize(self, n, forms):
        """Return singular or plural form based on count."""
        if n == 1:
            return forms[0]
        return forms[1]

    def to_year(self, val, suffix=None, longval=True):
        """Convert a year number to words."""
        if val < 0:
            val = abs(val)
            suffix = 'BC' if not suffix else suffix

        return self.to_cardinal(val) if not suffix else \
            "%s %s" % (self.to_cardinal(val), suffix)
