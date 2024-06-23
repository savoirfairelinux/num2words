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
import itertools
import re
import math
  
    
kurdish_vowels = [
        'a',
        'e',
        'ê',
        'i',
        'î',
        'o',
        'u',
        'û'
    ]
class Num2Word_KU(object):
    # Those are unused
    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0
    
    
    def to_cardinal(self, value):
        number = str(value)
        if len(number) == 1:
            return self._convert_ones(number)
        elif len(number) == 2:
            return self._convert_tens(number)
        elif len(number) == 3:
            return self._convert_hundreds(number)
        elif len(number) == 4:
            return self._convert_thousands(number)
        elif len(number) == 5:
            return self._convert_tens_thousands(number)
        elif len(number) == 6:
            return self._convert_hundreds_thousands(number)
        elif len(number) == 7:
            return self._convert_millions(number)
        elif len(number) == 8:
            return self._convert_tens_millions(number)
        elif len(number) == 9:
            return self._convert_hundreds_millions(number)
        else:
            return self._convert_large_numbers(number)
    
    
    def _convert_ones(self, value):
        _dict = {
            '0': 'sifir',
            '1': 'yek',
            '2': 'du',
            '3': 'sê',
            '4': 'çar',
            '5': 'pênc',
            '6': 'şeş',
            '7': 'heft',
            '8': 'heşt',
            '9': 'neh'
        }
    
        return _dict[value]
    
    
    def _convert_tens(self, n):
        if n[0] == '0':
            return _convert_ones(n)
    
        _dict = {
            '10': 'deh',
            '11': 'yanzdeh',
            '12': 'dwanzdeh',
            '13': 'sêzdeh',
            '14': 'çardeh',
            '15': 'panzdeh',
            '16': 'şanzdeh',
            '17': 'hivdeh',
            '18': 'hijdeh',
            '19': 'nozdeh',
            '20': 'bîst',
            '30': 'sî',
            '40': 'çil',
            '50': 'pêncî',
            '60': 'şêst',
            '70': 'heftê',
            '80': 'heştê',
            '90': 'nod'
        }
    
        if n in _dict:
            return _dict[n]
        first_n = str(int(str(n)[0:1]) * 10)
        second_n = str(int(str(n)[1:2]))
        return _dict[first_n] + self._get_joint() + self._convert_ones(second_n)
    
    
    def _convert_hundreds(self, n):
        if n == '100':
            return 'sed'
    
        if n.endswith('00'):
            first_n = n[0:1]
            return _convert_ones(first_n) + 'sed'
    
        first_n = n[0:1]
        second_n = str(int(n[1:]))
    
        if len(second_n) == 1:
            return _convert_hundreds(str(int(first_n) * 100)) + self._get_joint() + _convert_ones(second_n)
        elif len(second_n) == 2:
            return _convert_hundreds(str(int(first_n) * 100)) + self._get_joint() + _convert_tens(second_n)
    
    
    def _convert_thousands(self, n):
        if n == '1000':
            return 'hezar'
    
        if n.endswith('000'):
            current_n = n[0:1]
            if n[0] == '5':
                return 'pênj' + ' ' + 'hezar'
            else:
                return _convert_ones(current_n) + ' ' + 'hezar'
    
        rest_int = int(n[1:])
        rest = ''
        if len(str(rest_int)) == 1:
            rest = _convert_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = _convert_tens(str(rest_int))
        elif len(str(rest_int)) == 3:
            rest = _convert_hundreds(str(rest_int))
    
        if n[0] == '5':
            return 'pênj' + ' ' + 'hezar' + self._get_joint() + rest
        elif n[0] == '1':
            return 'hezar' + self._get_joint() + rest
        else:
            current_n = int(n[0:1])
            return _convert_ones(str(current_n)) + ' ' + 'hezar' + self._get_joint() + rest
    
    
    def _convert_tens_thousands(self, n):
        if n.endswith('000'):
            current_n = n[0:2]
            return _convert_tens(current_n) + ' ' + 'hezar'
    
        rest_int = int(n[2:])
        rest = ''
    
        if len(str(rest_int)) == 1:
            rest = _convert_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = _convert_tens(str(rest_int))
        else:
            rest = _convert_hundreds(str(rest_int))
    
        current_n = int(n[0:2])
        return _convert_tens(str(current_n)) + ' ' + 'hezar' + self._get_joint() + rest
    
    
    def _convert_hundreds_thousands(self, n):
        if n.endswith('000'):
            current_n = n[0:3]
            return _convert_hundreds(current_n) + ' ' + 'hezar'
    
        rest_int = int(n[3:])
        rest = ''
    
        if len(str(rest_int)) == 1:
            rest = _convert_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = _convert_tens(str(rest_int))
        else:
            rest = _convert_hundreds(str(rest_int))
    
        current_n = int(n[0:3])
        return _convert_hundreds(str(current_n)) + ' ' + 'hezar' + self._get_joint() + rest
    
    
    def _convert_millions(self, n):
        if n == '1000000':
            return 'milyon'
    
        if n.endswith('000000'):
            current_n = n[0:1]
            if n[0] == '5':
                return 'pênj' + ' ' + 'milyon'
            else:
                return _convert_ones(current_n) + ' ' + 'milyon'
    
        rest_int = int(n[1:])
        rest = ''
        if len(str(rest_int)) == 1:
            rest = _convert_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = _convert_tens(str(rest_int))
        elif len(str(rest_int)) == 3:
            rest = _convert_hundreds(str(rest_int))
        elif len(str(rest_int)) == 4:
            rest = _convert_thousands(str(rest_int))
        elif len(str(rest_int)) == 5:
            rest = _convert_tens_thousands(str(rest_int))
        elif len(str(rest_int)) == 6:
            rest = _convert_hundreds_thousands(str(rest_int))
    
        if n[0] == '5':
            return 'pênj' + ' ' + 'milyon' + self._get_joint() + rest
        elif n[0] == '1':
            return 'milyon' + self._get_joint() + rest
        else:
            current_n = int(n[0:1])
            return _convert_ones(str(current_n)) + ' ' + 'milyon' + self._get_joint() + rest
    
    
    def _convert_tens_millions(self, n):
        if n.endswith('000000'):
            current_n = n[0:2]
            return _convert_tens(current_n) + ' ' + 'milyon'
    
        rest_int = int(n[2:])
        rest = ''
    
        if len(str(rest_int)) == 1:
            rest = _convert_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = _convert_tens(str(rest_int))
        elif len(str(rest_int)) == 3:
            rest = _convert_hundreds(str(rest_int))
        elif len(str(rest_int)) == 4:
            rest = _convert_thousands(str(rest_int))
        elif len(str(rest_int)) == 5:
            rest = _convert_tens_thousands(str(rest_int))
        elif len(str(rest_int)) == 6:
            rest = _convert_hundreds_thousands(str(rest_int))
    
        current_n = int(n[0:2])
        return _convert_tens(str(current_n)) + ' ' + 'milyon' + self._get_joint() + rest
    
    
    def _convert_hundreds_millions(self, n):
        if n.endswith('000000'):
            current_n = n[0:3]
            return _convert_hundreds(current_n) + ' ' + 'milyon'
    
        rest_int = int(n[3:])
        rest = ''
    
        if len(str(rest_int)) == 1:
            rest = _convert_ones(str(rest_int))
        elif len(str(rest_int)) == 2:
            rest = _convert_tens(str(rest_int))
        elif len(str(rest_int)) == 3:
            rest = _convert_hundreds(str(rest_int))
        elif len(str(rest_int)) == 4:
            rest = _convert_thousands(str(rest_int))
        elif len(str(rest_int)) == 5:
            rest = _convert_tens_thousands(str(rest_int))
        elif len(str(rest_int)) == 6:
            rest = _convert_hundreds_thousands(str(rest_int))
    
        current_n = int(n[0:3])
        return _convert_hundreds(str(current_n)) + ' ' + 'milyon' + self._get_joint() + rest
    
    
    def _convert_large_numbers(self, n):
        if n == '1000000000':
            return 'milyar'
        else:
            res = []
            n = str(n)
            for number in n:
                res.append(_convert_ones(number))
            return ' '.join(res)
    
    
    def _get_joint(self):
        return ' û '
    
    
    def to_ordinal(self, value):
        number_text = self.to_cardinal(value)
        number_text = number_text.strip()
        last_letter = number_text[len(number_text) - 1]
        if last_letter in kurdish_vowels:
            return number_text + 'yemîn'
        else:
            return number_text + 'emîn'
    def to_ordinal_num(self, value):
        return "%s%s" % (value, self.to_ordinal(value)[-4:])
    
    def to_year(self, value):
        return self.to_cardinal(value)
    
    def to_currency(self, value):
        return self.to_cardinal(value) + " Lira"
 