# -*- encoding: utf-8 -*-
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

from num2words.base import Num2Word_Base
from num2words.currency import parse_currency_parts


class Num2Word_SI(Num2Word_Base):
    """
    Sinhala (si) Num2Word class.

    Uses formal written Sinhala. Numbers combine a standalone form
    (used when a word ends the expression) with a combining stem
    (used before a following word), e.g. 2 is "දෙක" alone but "දෙ"
    in "දෙදහස" (2000) and "දෙසීය" (200).
    """

    CURRENCY_FORMS = {
        "LKR": ("රුපියල්", "ශත"),
    }

    errmsg_toobig = "abs(%s) must be less than %s."

    # 0-10 standalone
    ones = [
        "බින්දුව", "එක", "දෙක", "තුන", "හතර",
        "පහ", "හය", "හත", "අට", "නවය", "දහය",
    ]

    # 11-19 standalone
    teens = [
        "එකොළහ", "දොළහ", "දහතුන", "දහහතර", "පහළොව",
        "දහසය", "දහහත", "දහඅට", "දහනවය",
    ]

    # 20, 30 ... 90 standalone
    tens = [
        "විස්ස", "තිහ", "හතළිහ", "පනහ", "හැට",
        "හැත්තෑව", "අසූව", "අනූව",
    ]

    # 20, 30 ... 90 combining (before a following unit: "විසි එක" = 21)
    tens_comb = [
        "විසි", "තිස්", "හතළිස්", "පනස්", "හැට",
        "හැත්තෑ", "අසූ", "අනූ",
    ]

    # 1-9 combining stems used before scale words (සිය/දහස/ලක්ෂ)
    scale_stems = [
        None, "එක්", "දෙ", "තුන්", "හාර", "පන්", "හය", "හත්", "අට", "නව",
    ]

    # 10-19 combining stems before දහස (10,000 = "දසදහස")
    teen_stems = [
        "දස", "එකොළොස්", "දොළොස්", "දහතුන්", "දාහතර", "පහළොස්",
        "දාසය", "දාහත්", "දහඅට", "දහනව",
    ]

    # 100, 200 ... 900 exact (end of expression)
    hundreds_exact = [
        "සියය", "දෙසීය", "තුන්සියය", "හාරසියය", "පන්සියය",
        "හයසියය", "හත්සියය", "අටසියය", "නවසියය",
    ]

    # 100, 200 ... 900 combining (followed by more: "එකසිය විසි දෙක" = 122)
    hundreds_comb = [
        "එකසිය", "දෙසීය", "තුන්සිය", "හාරසිය", "පන්සිය",
        "හයසිය", "හත්සිය", "අටසිය", "නවසිය",
    ]

    # standalone word -> combining stem, for ordinals (2 -> "දෙවැනි")
    ordinal_stems = {
        "එක": "එක්", "දෙක": "දෙ", "තුන": "තුන්", "හතර": "හතර",
        "පහ": "පස්", "හය": "හය", "හත": "හත්", "අට": "අට",
        "නවය": "නව", "දහය": "දහ",
        "එකොළහ": "එකොළොස්", "දොළහ": "දොළොස්", "දහතුන": "දහතුන්",
        "දහහතර": "දාහතර", "පහළොව": "පහළොස්", "දහසය": "දාසය",
        "දහහත": "දාහත්", "දහඅට": "දහඅට", "දහනවය": "දහනව",
        "විස්ස": "විසි", "තිහ": "තිස්", "හතළිහ": "හතළිස්",
        "පනහ": "පනස්", "හැට": "හැට", "හැත්තෑව": "හැත්තෑ",
        "අසූව": "අසූ", "අනූව": "අනූ",
        "සියය": "සිය", "දෙසීය": "දෙසීය", "දහස": "දහස්",
        "ලක්ෂය": "ලක්ෂ", "මිලියනය": "මිලියන", "බිලියනය": "බිලියන",
    }

    ordinal_suffix = "වැනි"

    def setup(self):
        self.negword = "සෘණ "
        self.pointword = "දශම"
        # Custom decomposition below; cards only anchors MAXVAL.
        self.cards = {10**12: "ට්‍රිලියනය"}
        self.MAXVAL = 10**12

    def set_numwords(self):
        # All lookup tables are class attributes; nothing to build.
        pass

    # ------------------------------------------------------------------
    # Cardinals
    # ------------------------------------------------------------------

    def _under_hundred(self, n):
        """1-99, standalone (ends the expression)."""
        if n <= 10:
            return self.ones[n]
        if n < 20:
            return self.teens[n - 11]
        t, u = divmod(n, 10)
        if u == 0:
            return self.tens[t - 2]
        return "%s %s" % (self.tens_comb[t - 2], self.ones[u])

    def _under_thousand(self, n):
        """1-999, standalone."""
        if n < 100:
            return self._under_hundred(n)
        h, rem = divmod(n, 100)
        if rem == 0:
            return self.hundreds_exact[h - 1]
        return "%s %s" % (self.hundreds_comb[h - 1], self._under_hundred(rem))

    def _thousands_part(self, m, exact):
        """m thousands (1 <= m <= 99): stem-joined to දහස/දහස්."""
        suffix = "දහස" if exact else "දහස්"
        if m == 1:
            return "එක්" + suffix
        if m <= 9:
            return self.scale_stems[m] + suffix
        if m <= 19:
            return self.teen_stems[m - 10] + suffix
        t, u = divmod(m, 10)
        if u == 0:
            return self.tens_comb[t - 2] + suffix
        return "%s %s" % (
            self.tens_comb[t - 2], self.scale_stems[u] + suffix
        )

    def _lakhs_part(self, count, exact):
        """count lakhs (1 <= count <= 9): stem-joined to ලක්ෂය/ලක්ෂ."""
        suffix = "ලක්ෂය" if exact else "ලක්ෂ"
        return self.scale_stems[count] + suffix

    def _int_to_words(self, value):
        if value == 0:
            return self.ones[0]

        parts = []
        billions, rem = divmod(value, 10**9)
        millions, rem = divmod(rem, 10**6)
        lakhs, rem = divmod(rem, 10**5)
        thousands, rem = divmod(rem, 10**3)

        # Borrowed scale words prefix the multiplier ("මිලියන දෙක"),
        # except exactly one, which takes the noun form ("මිලියනය").
        if billions:
            parts.append(
                "බිලියනය" if billions == 1
                else "බිලියන %s" % self._under_thousand(billions)
            )
        if millions:
            parts.append(
                "මිලියනය" if millions == 1
                else "මිලියන %s" % self._under_thousand(millions)
            )
        if lakhs:
            exact = rem == 0 and thousands == 0
            parts.append(self._lakhs_part(lakhs, exact))
        if thousands:
            parts.append(self._thousands_part(thousands, rem == 0))
        if rem:
            parts.append(self._under_thousand(rem))

        return " ".join(parts)

    def to_cardinal(self, value):
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = self.negword
        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))
        return out + self._int_to_words(int(value))

    def to_cardinal_float(self, value):
        """3.14 -> "තුනයි දශම එකයි හතර".

        The integer part and every decimal digit except the last take
        the clitic "යි"; digits are read out individually.
        """
        pre, post = self.float2tuple(float(value))

        out = ""
        if value < 0:
            pre = abs(pre)
            out = self.negword

        digits = "%0*d" % (self.precision, post) if self.precision else ""
        words = [self._int_to_words(pre) + "යි", self.pointword]
        digit_words = [self.ones[int(d)] for d in digits]
        words.extend(w + "යි" for w in digit_words[:-1])
        if digit_words:
            words.append(digit_words[-1])
        return out + " ".join(words)

    # ------------------------------------------------------------------
    # Ordinals
    # ------------------------------------------------------------------

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 1:
            return "පළමු" + self.ordinal_suffix
        cardinal = self.to_cardinal(value)
        words = cardinal.split(" ")
        last = words[-1]
        words[-1] = self.ordinal_stems.get(last, last)
        return "".join([" ".join(words), self.ordinal_suffix])

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%d%s" % (value, self.ordinal_suffix)

    # ------------------------------------------------------------------
    # Currency: "රුපියල් එක්දහස් දෙසිය පනහයි ශත පනහයි"
    # ------------------------------------------------------------------

    def to_currency(self, val, currency="LKR", cents=True, separator=" ",
                    adjective=False):
        left, right, is_negative = parse_currency_parts(val)
        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"'
                % (currency, self.__class__.__name__)
            )
        minus = self.negword if is_negative else ""
        out = "%s%s %sයි" % (minus, cr1, self.to_cardinal(left))
        if right:
            cents_text = (
                self.to_cardinal(right) if cents
                else self.to_ordinal_num(right)
            )
            out += "%s%s %sයි" % (separator, cr2, cents_text)
        return out

    def to_year(self, val, **kwargs):
        return self.to_cardinal(val)
