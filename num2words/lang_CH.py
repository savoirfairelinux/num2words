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

import math

ONES = {
    0: '零',
    1: '一',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '七',
    8: '八',
    9: '九'
}


DIGITS = {
    10: '十',
    100: '百',
    1000: '千',
    10000: '万', # 10,000
    100000: '十万', # 100,000
    1000000: '百万', # 1,000,000
    10000000: '千万', # 10,000,000
    100000000: '亿',# 100,000,000
    1000000000: '十亿',# 1,000,000,000
    10000000000: '百亿',# 10,000,000,000
    100000000000: '千亿',# 100,000,000,000
    1000000000000: '兆',# 1,000,000,000,000
    10000000000000: '十兆',# 10,000,000,000,000
    100000000000000: '百兆',# 100,000,000,000,000
    1000000000000000: '千兆',# 1,000,000,000,000,000
}

class Num2Word_CH(object):
    def get_digit(num_str):
        dec_place = len(num_str)
        dec_value = 10**(dec_place-1)
        return DIGITS.get(dec_value)

    def check_digits(words, num_str):
        digit = get_digit(num_str)
        if(words == ''):
            return words
        elif (len(digit) == 2):
            words = words[:-1]
        elif(digit == words[-1]):
            words = words[:-1]
        return words

    def convert_int(num_int):
        num_str = str(num_int)
        words = ""
        all_digits = "百千万亿兆"

        if(num_int < 10):
            return ONES.get(num_int)
        if(int(num_str[0]) == 1):
            words = get_digit(num_str)
            num_str = num_str[1:]

        while(len(num_str) != 0):
            digit = int(num_str[0])
            if(digit != 0):
                words = check_digits(words, num_str)
                words += ONES.get(digit)
                words += get_digit(num_str)
            elif(digit == 0 and len(num_str) != 1 and int(num_str[1])!= 0 ):
                words += ONES.get(digit)
            num_str = num_str[1:]

        if(len(words) != 0 and all_digits.find(words[0]) != -1):
            unit = str(num_int)[0]
            unit = int(unit)
            words = ONES.get(unit) + words
        return words

    def convert_dec(num): # function for in2words
        words = ""
        if num == 0:
            return words
        num_str = str(num)
        i = 0
        while(i < len(num_str)):
            if num_str[i] == '.':
                num_str = num_str[i+1:]
                break
            i += 1
        words = int2words(int(num_str))
        return words

    def int2words(num): # core function
        if n > 1000000000000000:  # doesn't yet work for numbers this big
            raise NotImplementedError()
        num_int = math.floor(num)
        num_dec = round(num - num_int, 2) # rounded to 2 decimal places
        word_int = convert_int(num_int)
        word_dec = convert_dec(num_dec, )
        if word_dec != '':
            return word_int + "点" + word_dec
        return word_int

    def to_currency(num):
        words = int2words(num)
        words += "人民币"
        return words

    def to_cardinal(self, number):
        return self.int2words(number)

    def to_ordinal(self, number):
        return self.int2words(number)
