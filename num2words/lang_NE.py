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

from __future__ import division, print_function, unicode_literals

from num2words.currency import parse_currency_parts

from .lang_EU import Num2Word_EU


class Num2Word_NE(Num2Word_EU):
    """
    Nepali language (नेपाली) number to words converter with Devanagari script.

    Nepali numbering system: लाख (10^5), करोड (10^7), अर्ब (10^9), खर्ब (10^11)
    """

    CURRENCY_FORMS = {
        'NPR': (('रुपैयाँ', 'रुपैयाँ'), ('पैसा', 'पैसा')),
        'USD': (('डलर', 'डलर'), ('सेन्ट', 'सेन्ट')),
        'EUR': (('युरो', 'युरो'), ('सेन्ट', 'सेन्ट')),
    }

    def setup(self):
        """Set up Devanagari number words for Nepali."""

        self.cardinals = {
            0: 'शून्य',
            1: 'एक', 2: 'दुई', 3: 'तीन', 4: 'चार', 5: 'पाँच',
            6: 'छ', 7: 'सात', 8: 'आठ', 9: 'नौ', 10: 'दस',
            11: 'एघार', 12: 'बाह्र', 13: 'तेह्र', 14: 'चौध', 15: 'पन्ध्र',
            16: 'सोह्र', 17: 'सत्र', 18: 'अठार', 19: 'उन्नाइस', 20: 'बिस',
            21: 'एक्काइस', 22: 'बाइस', 23: 'तेइस', 24: 'चौबिस', 25: 'पच्चिस',
            26: 'छब्बिस', 27: 'सत्ताइस', 28: 'अट्ठाइस', 29: 'उनन्तिस',
            30: 'तिस', 31: 'एकतिस', 32: 'बत्तिस', 33: 'तेत्तिस', 34: 'चौतिस',
            35: 'पैँतिस', 36: 'छत्तिस', 37: 'सैँतिस', 38: 'अठतिस',
            39: 'उनन्चालिस', 40: 'चालिस', 41: 'एकचालिस',
            42: 'बयालिस', 43: 'त्रिचालिस', 44: 'चवालिस', 45: 'पैँतालिस',
            46: 'छयालिस', 47: 'सतचालिस', 48: 'अठचालिस', 49: 'उनन्चास',
            50: 'पचास', 51: 'एकाउन्न', 52: 'बाउन्न', 53: 'त्रिपन्न',
            54: 'चवन्न', 55: 'पचपन्न', 56: 'छपन्न', 57: 'सन्ताउन्न',
            58: 'अन्ठाउन्न', 59: 'उनान्साठी', 60: 'साठी', 61: 'एकसट्ठी',
            62: 'बैसट्ठी', 63: 'त्रिसट्ठी', 64: 'चौंसट्ठी', 65: 'पैंसट्ठी',
            66: 'छैसट्ठी', 67: 'सतसट्ठी', 68: 'अठसट्ठी', 69: 'उनन्सत्तरी',
            70: 'सत्तरी', 71: 'एकहत्तर', 72: 'बहत्तर', 73: 'त्रिहत्तर',
            74: 'चौहत्तर', 75: 'पचहत्तर', 76: 'छयहत्तर', 77: 'सतहत्तर',
            78: 'अठहत्तर', 79: 'उनासी', 80: 'असी', 81: 'एकासी',
            82: 'बयासी', 83: 'त्रियासी', 84: 'चौरासी', 85: 'पचासी',
            86: 'छयासी', 87: 'सतासी', 88: 'अठासी', 89: 'उनान्नब्बे',
            90: 'नब्बे', 91: 'एकान्नब्बे', 92: 'बयान्नब्बे',
            93: 'त्रियान्नब्बे', 94: 'चौरान्नब्बे', 95: 'पन्चान्नब्बे',
            96: 'छयान्नब्बे', 97: 'सन्तान्नब्बे', 98: 'अन्ठान्नब्बे',
            99: 'उनान्सय'
        }

        # Ordinal numbers (पहिलो, दोस्रो, etc.)
        self.ordinals = {
            1: 'पहिलो', 2: 'दोस्रो', 3: 'तेस्रो', 4: 'चौथो', 5: 'पाँचौं',
            6: 'छैटौं', 7: 'सातौं', 8: 'आठौं', 9: 'नवौं', 10: 'दशौं',
            11: 'एघारौं', 12: 'बाह्रौं', 13: 'तेह्रौं', 14: 'चौधौं',
            15: 'पन्ध्रौं', 16: 'सोह्रौं', 17: 'सत्रौं', 18: 'अठारौं',
            19: 'उन्नाइसौं', 20: 'बीसौं', 21: 'एक्काइसौं', 22: 'बाइसौं',
            23: 'तेइसौं', 24: 'चौबीसौं', 25: 'पच्चीसौं', 26: 'छब्बीसौं',
            27: 'सत्ताइसौं', 28: 'अठ्ठाइसौं', 29: 'उनन्तिसौँ', 30: 'तिसौँ',
        }

        self.negword = "माइनस "

    def _int_to_word(self, number):
        """
        Convert an integer to Devanagari words using Nepali numbering system.
        """
        if number == 0:
            return self.cardinals[0]

        if number < 0:
            return self.negword + self._int_to_word(-number)

        # Direct lookup for numbers 1-99 from cardinals dict
        if number <= 99:
            return self.cardinals.get(number, '')

        words = []

        # खर्ब (Kharba) = 10^11
        if number >= 100000000000:
            kharba = number // 100000000000
            kharba_words = self._int_to_word(kharba)
            if kharba_words:
                words.append(kharba_words)
                words.append('खर्ब')
            number %= 100000000000

        # अर्ब (Arba) = 10^9
        if number >= 1000000000:
            arba = number // 1000000000
            arba_words = self._int_to_word(arba)
            if arba_words:
                words.append(arba_words)
                words.append('अर्ब')
            number %= 1000000000

        # करोड (Crore) = 10^7
        if number >= 10000000:
            crore = number // 10000000
            crore_words = self._int_to_word(crore)
            if crore_words:
                words.append(crore_words)
                words.append('करोड')
            number %= 10000000

        # लाख (Lakh) = 10^5
        if number >= 100000:
            lakh = number // 100000
            lakh_words = self._int_to_word(lakh)
            if lakh_words:
                words.append(lakh_words)
                words.append('लाख')
            number %= 100000

        # हजार (Thousand) = 10^3
        if number >= 1000:
            thousand = number // 1000
            thousand_words = self._int_to_word(thousand)
            if thousand_words:
                words.append(thousand_words)
                words.append('हजार')
            number %= 1000

        # सय (Hundred)
        if number >= 100:
            hundred = number // 100
            words.append(self.cardinals[hundred])
            words.append('सय')
            number %= 100

        # Above 0
        if number > 0:
            above_zero = self.cardinals.get(number, '')
            if above_zero:
                words.append(above_zero)

        return ' '.join(words)

    def to_cardinal(self, number):
        """
        Convert a number to its cardinal word representation in Devanagari.
        """
        try:
            if isinstance(number, str):
                number = int(number)

            return self._int_to_word(int(number))

        except Exception:
            return self._int_to_word(int(number))

    def to_ordinal(self, number):
        """
        Convert a number to its ordinal representation in Nepali.
        """
        if number in self.ordinals:
            return self.ordinals[number]
        else:
            # For larger numbers, append "औं" suffix
            return self.to_cardinal(number) + 'औं'

    def to_currency(self, val, currency='NPR', cents=True, separator=','):
        """
        Convert numeric value to currency string with Nepali numbering.
        Pass is_int_with_cents=False so integers are treated as main units
        """
        left, right, is_negative = parse_currency_parts(
            val, is_int_with_cents=False
        )

        try:
            currency_forms = self.CURRENCY_FORMS[currency]
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        minus_str = "%s " % self.negword.strip() if is_negative else ""

        money_str = self._int_to_word(int(left))

        # Choose singular or plural
        main_currency = (
            currency_forms[0][0]
            if left == 1
            else currency_forms[0][1]
        )

        # Only include fractional part if it exists
        if right > 0 and cents:
            cents_str = self._int_to_word(int(right))
            minor_currency = (
                currency_forms[1][0]
                if right == 1
                else currency_forms[1][1]
            )
            return u'%s%s %s%s %s %s' % (
                minus_str,
                money_str,
                main_currency,
                separator,
                cents_str,
                minor_currency
            )
        else:
            return u'%s%s %s' % (
                minus_str,
                money_str,
                main_currency
            )

    def pluralize(self, n, forms):
        if n == 1:
            return forms[0]
        else:
            return forms[1]

    def _money_verbose(self, number, currency):
        """
        Convert money amount to Devanagari words.
        """
        return self._int_to_word(int(number))

    def _cents_verbose(self, number, currency):
        """
        Convert cents to Devanagari words.
        """
        return self._int_to_word(int(number))
