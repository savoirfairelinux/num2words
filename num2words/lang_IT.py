# -*- encoding: utf-8 -*-
#
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

# TODO: Implement commas for long numbers
# TODO: Accents on "tre"

from __future__ import unicode_literals
from .lang_EU import Num2Word_EU

ZERO = "zero"

STR_0_to_19 = [
    ZERO, "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto",
    "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici",
    "sedici", "diciassette", "diciotto", "diciannove"
]

STR_TENS = {2: "venti", 3: "trenta", 4: "quaranta", 6: "sessanta"}

# Utils
# =====

def as_number(digits):
    return int("".join(map(str, digits)) or "0")

def stringify_exponent(exponent):
    mod = exponent % 6
    prefix = {6: "m", 12: "b", 18: "tr", 24: "quadr"}[exponent - mod]
    return prefix + ("ilione" if mod == 0 else "iliardo")

def omitt_if_zero(number_to_string):
    return "" if number_to_string == ZERO else number_to_string

# Big numbers helpers
# ===================

def break_into_blocks(digits, length):
    if length < 4:
        return digits
    elif length <= 30:
        mod = length % 3 or 3
        return [digits[:mod], digits[mod:]]
    else:
        mod = length % 27 # We use "quadriliardi" for very big numbers
        return break_into_blocks(digits[:mod], mod) + digits[mod:]

class Num2Word_IT(Num2Word_EU):

    def __init__(self):
        pass

    def float_to_cardinal(self, float_number):
        decimal_part_as_int = int(str(float_number % 1)[1:])
        whole_part_to_string = self.to_cardinal(int(float_number))
        decimal_part_to_string = self.to_cardinal(decimal_part_as_int)
        return whole_part_to_string + " virgola " + decimal_part_to_string

    def two_digits_to_cardinal(self, number):
        tens = number / 10
        units = number % 10
        if tens in STR_TENS:
            tens_to_string = STR_TENS[tens]
        else:
            tens_to_string = STR_0_to_19[tens][:-1] + "anta"
        if units in [1, 8]: # Ottant(a)otto, sessant(a)uno
            tens_to_string = tens_to_string[:-1] # Drop last
        units_to_string = omitt_if_zero(STR_0_to_19[units])
        return tens_to_string + units_to_string

    def hundreds_to_cardinal(self, number):
        hundreds = number / 100
        hundreds_to_string = "cento"
        if hundreds != 1:
            hundreds_to_string = STR_0_to_19[hundreds] + hundreds_to_string
        remainder_to_string = omitt_if_zero(self.to_cardinal(number % 100))
        return hundreds_to_string + remainder_to_string

    def thousands_to_cardinal(self, number):
        thousands = number / 1000
        if thousands == 1:
            thousands_to_string = "mille"
        else:
            thousands_to_string = self.to_cardinal(thousands) + "mila"
        remainder_to_string = omitt_if_zero(self.to_cardinal(number % 1000))
        return thousands_to_string + remainder_to_string

    def big_exponent_to_cardinal(self, number):
        digits = [int(c) for c in str(number)]
        blocks = break_into_blocks(digits, len(digits))
        length = len(blocks)
        if length == 2:
            num_1, num_2 = [as_number(x) for x in blocks]
            exponent_to_string = stringify_exponent(len(blocks[1]))
            if num_1 == 1:
                string = "un {}".format(exponent_to_string)
            else:
                multiplier = self.to_cardinal(num_1)
                string = multiplier + " " + exponent_to_string[:-1] + "i"
            if num_2 != 0:
                string += " e " + self.to_cardinal(num_2)
            return string
        else:
            pass # TODO *BIG* numbers (> 10^30) support

    def to_cardinal(self, number):
        if number % 1 != 0:
            return self.float_to_cardinal(number)
        if number < 0:
            return "meno " + self.to_cardinal(-number)
        if number < 20:
            return STR_0_to_19[number]
        elif number < 100:
            return self.two_digits_to_cardinal(number)
        elif number < 1000:
            return self.hundreds_to_cardinal(number)
        elif number < 1000000:
            return self.thousands_to_cardinal(number)
        else:
            return self.big_exponent_to_cardinal(number)

    def to_ordinal(self, n):
        if n < 0:
            return "meno " + self.to_ordinal(n)
        if n == 0:
            return ZERO
        if n < 20:
            return [
                "primo", "secondo", "terzo", "quarto", "quinto", "sesto",
                "settimo", "ottavo", "nono", "decimo", "undicesimo",
                "dodicesimo", "tredicesimo", "quattordicesimo", "quindicesimo",
                "sedicesimo", "diciassettesimo", "diciassettesimo",
                "diciannovesimo"
            ][n-1]
        else:
            return self.to_cardinal(n)[:-1] + "esimo"
