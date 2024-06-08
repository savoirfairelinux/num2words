# -*- coding: utf-8 -*-
# Copyright (c) 2024, Karwan Khalid.  All Rights Reserved.

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

from decimal import Decimal
from math import floor



class Num2Word_CKB(object):
    # Those are unused
    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0

    @staticmethod
    def to_cardinal(number):
        if not isinstance(number, (int, float, str)):
            return 'The entered number was not valid'

        number_str = str(number)

        if '.' in number_str:
            whole_part, fractional_part = number_str.split('.')
            whole_part_words = Num2Word_CKB.to_cardinal(whole_part)
            fractional_part_words = Num2Word_CKB.to_cardinal(fractional_part)
            return f"{whole_part_words} پۆینت {fractional_part_words}"
        elif int(number_str) < 0:
                return 'سالب ' + Num2Word_CKB.to_cardinal(abs(number))
        else:
            return Num2Word_CKB._convert_whole_number(number_str)
    @staticmethod
    def to_year( value):
        return  'ساڵی ' + Num2Word_CKB.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value)+"م"

    def to_ordinal(self, number):
        r = self.to_cardinal(number)
        if r[-1] == 'ە':
            return r[:-1] + 'م'
        return r + 'ەم'

    def to_currency(self, value):
        return self.to_cardinal(value) + " دینار"

    @staticmethod
    def _convert_whole_number(number):
        number = str(int(number))  # Ensure the number is an integer string
        number_type = Num2Word_CKB._get_number_type(number)
        if number_type == 'ones':
            return Num2Word_CKB._calculate_ones(number)
        elif number_type == 'tens':
            return Num2Word_CKB._calculate_tens(number)
        elif number_type == 'hundreds':
            return Num2Word_CKB._calculate_hundreds(number)
        elif number_type == 'thousands':
            return Num2Word_CKB._calculate_thousands(number)
        elif number_type == 'tens-thousands':
            return Num2Word_CKB._calculate_tens_thousands(number)
        elif number_type == 'hundreds-thousands':
            return Num2Word_CKB._calculate_hundreds_thousands(number)
        elif number_type == 'millions':
            return Num2Word_CKB._calculate_millions(number)
        elif number_type == 'tens-millions':
            return Num2Word_CKB._calculate_tens_millions(number)
        elif number_type == 'hundreds-millions':
            return Num2Word_CKB._calculate_hundreds_millions(number)
        elif number_type == 'large-number':
            return Num2Word_CKB._calculate_large_number(number)

    @staticmethod
    def _calculate_ones(n):
        _dict = {
            '0': 'سفر',
            '1': 'یەک',
            '2': 'دوو',
            '3': 'سێ',
            '4': 'چوار',
            '5': 'پێنج',
            '6': 'شەش',
            '7': 'حەوت',
            '8': 'هەشت',
            '9': 'نۆ'
        }
        return _dict[n]

    @staticmethod
    def _calculate_tens(n):
        if n.startswith('0'):
            return Num2Word_CKB._calculate_ones(n[1])
        _dict = {
            '10': 'دە',
            '11': 'یازدە',
            '12': 'دوازدە',
            '13': 'سێزدە',
            '14': 'چواردە',
            '15': 'پازدە',
            '16': 'شازدە',
            '17': 'حەڤدە',
            '18': 'هەژدە',
            '19': 'نۆزدە',
            '20': 'بیست',
            '30': 'سی',
            '40': 'چل',
            '50': 'پەنجا',
            '60': 'شەست',
            '70': 'حەفتا',
            '80': 'هەشتا',
            '90': 'نەوەت'
        }

        if n in _dict:
            return _dict[n]
        else:
            first_n = str(int(n[0]) * 10)
            second_n = n[1]
            return _dict[first_n] + Num2Word_CKB._get_joint() + Num2Word_CKB._calculate_ones(second_n)

    @staticmethod
    def _calculate_hundreds(n):
        if n == '100':
            return 'سەد'
        elif n.endswith('00'):
            first_n = n[0]
            return Num2Word_CKB._calculate_ones(first_n) + ' سەد'
        else:
            first_n = n[0]
            second_n = str(int(n[1:]))
            if len(second_n) == 1:
                return Num2Word_CKB._calculate_hundreds(str(int(first_n) * 100)) + Num2Word_CKB._get_joint() + Num2Word_CKB._calculate_ones(second_n)
            elif len(second_n) == 2:
                return Num2Word_CKB._calculate_hundreds(str(int(first_n) * 100)) + Num2Word_CKB._get_joint() + Num2Word_CKB._calculate_tens(second_n)

    @staticmethod
    def _calculate_thousands(n):
        if n == '1000':
            return 'هەزار'
        if n.endswith('000'):
            current_n = n[0]
            if n.startswith('5'):
                return 'پێنج' + ' ' + 'هەزار'
            else:
                return Num2Word_CKB._calculate_ones(current_n) + ' ' + 'هەزار'
        rest_int = int(n[1:])
        rest = ''
        if len(str(rest_int)) == 1:
            rest = Num2Word_CKB._calculate_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = Num2Word_CKB._calculate_tens(str(rest_int))
        else:
            rest = Num2Word_CKB._calculate_hundreds(str(rest_int))

        if n.startswith('5'):
            return 'پێنج' + ' ' + 'هەزار' + Num2Word_CKB._get_joint() + rest
        elif n.startswith('1'):
            return 'هەزار' + Num2Word_CKB._get_joint() + rest
        else:
            current_n = int(n[0])
            return Num2Word_CKB._calculate_ones(str(current_n)) + ' ' + 'هەزار' + Num2Word_CKB._get_joint() + rest

    @staticmethod
    def _calculate_tens_thousands(n):
        if n.endswith('000'):
            current_n = n[:2]
            return Num2Word_CKB._calculate_tens(current_n) + ' ' + 'هەزار'
        rest_int = int(n[2:])
        rest = ''
        if len(str(rest_int)) == 1:
            rest = Num2Word_CKB._calculate_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = Num2Word_CKB._calculate_tens(str(rest_int))
        else:
            rest = Num2Word_CKB._calculate_hundreds(str(rest_int))
        current_n = int(n[:2])
        return Num2Word_CKB._calculate_tens(str(current_n)) + ' ' + 'هەزار' + Num2Word_CKB._get_joint() + rest

    @staticmethod
    def _calculate_hundreds_thousands(n):
        if n.endswith('000'):
            current_n = n[:3]
            return Num2Word_CKB._calculate_hundreds(current_n) + ' ' + 'هەزار'
        rest_int = int(n[3:])
        rest = ''
        if len(str(rest_int)) == 1:
            rest = Num2Word_CKB._calculate_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = Num2Word_CKB._calculate_tens(str(rest_int))
        else:
            rest = Num2Word_CKB._calculate_hundreds(str(rest_int))
        current_n = int(n[:3])
        return Num2Word_CKB._calculate_hundreds(str(current_n)) + ' ' + 'هەزار' + Num2Word_CKB._get_joint() + rest

    @staticmethod
    def _calculate_millions(n):
        if n == '1000000':
            return 'ملیۆن'
        if n.endswith('000000'):
            current_n = n[0]
            if n.startswith('5'):
                return 'پێنج' + ' ' + 'ملیۆن'
            else:
                return Num2Word_CKB._calculate_ones(current_n) + ' ' + 'ملیۆن'
        rest_int = int(n[1:])
        rest = ''
        rest_len = len(str(rest_int))
        if rest_len == 1:
            rest = Num2Word_CKB._calculate_ones(str(rest_int))
        elif rest_len == 2:
            rest = Num2Word_CKB._calculate_tens(str(rest_int))
        elif rest_len == 3:
            rest = Num2Word_CKB._calculate_hundreds(str(rest_int))
        elif rest_len == 4:
            rest = Num2Word_CKB._calculate_thousands(str(rest_int))
        elif rest_len == 5:
            rest = Num2Word_CKB._calculate_tens_thousands(str(rest_int))
        else:
            rest = Num2Word_CKB._calculate_hundreds_thousands(str(rest_int))
        current_n = int(n[:2])
        return Num2Word_CKB._calculate_tens(str(current_n)) + ' ' + 'ملیۆن' + Num2Word_CKB._get_joint() + rest

    @staticmethod
    def _calculate_tens_millions(n):
        if n.endswith('000000'):
            current_n = n[:2]
            return Num2Word_CKB._calculate_tens(current_n) + ' ' + 'ملیۆن'
        rest_int = int(n[2:])
        rest = ''
        rest_len = len(str(rest_int))
        if rest_len == 1:
            rest = Num2Word_CKB._calculate_ones(str(rest_int))
        elif rest_len == 2:
            rest = Num2Word_CKB._calculate_tens(str(rest_int))
        elif rest_len == 3:
            rest = Num2Word_CKB._calculate_hundreds(str(rest_int))
        elif rest_len == 4:
            rest = Num2Word_CKB._calculate_thousands(str(rest_int))
        elif rest_len == 5:
            rest = Num2Word_CKB._calculate_tens_thousands(str(rest_int))
        else:
            rest = Num2Word_CKB._calculate_hundreds_thousands(str(rest_int))
        current_n = int(n[:2])
        return Num2Word_CKB._calculate_tens(str(current_n)) + ' ' + 'ملیۆن' + Num2Word_CKB._get_joint() + rest

    @staticmethod
    def _calculate_hundreds_millions(n):
        if n.endswith('000000'):
            current_n = n[:3]
            return Num2Word_CKB._calculate_hundreds(current_n) + ' ' + 'ملیۆن'
        rest_int = int(n[3:])
        rest = ''
        rest_len = len(str(rest_int))
        if rest_len == 1:
            rest = Num2Word_CKB._calculate_ones(str(rest_int))
        elif rest_len == 2:
            rest = Num2Word_CKB._calculate_tens(str(rest_int))
        elif rest_len == 3:
            rest = Num2Word_CKB._calculate_hundreds(str(rest_int))
        elif rest_len == 4:
            rest = Num2Word_CKB._calculate_thousands(str(rest_int))
        elif rest_len == 5:
            rest = Num2Word_CKB._calculate_tens_thousands(str(rest_int))
        else:
            rest = Num2Word_CKB._calculate_hundreds_thousands(str(rest_int))
        current_n = int(n[:3])
        return Num2Word_CKB._calculate_hundreds(str(current_n)) + ' ' + 'ملیۆن' + Num2Word_CKB._get_joint() + rest

    @staticmethod
    def _calculate_large_number(n):
        if n == '1000000000':
            return 'ملیار'
        else:
            return ' '.join([Num2Word_CKB._calculate_ones(digit) for digit in n])

    @staticmethod
    def _get_number_type(n):
        length = len(n)
        if length == 1:
            return 'ones'
        elif length == 2:
            return 'tens'
        elif length == 3:
            return 'hundreds'
        elif length == 4:
            return 'thousands'
        elif length == 5:
            return 'tens-thousands'
        elif length == 6:
            return 'hundreds-thousands'
        elif length == 7:
            return 'millions'
        elif length == 8:
            return 'tens-millions'
        elif length == 9:
            return 'hundreds-millions'
        else:
            return 'large-number'

    @staticmethod
    def _get_joint():
        return ' و '