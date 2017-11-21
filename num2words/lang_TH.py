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

from __future__ import unicode_literals

import decimal

thai_num = (
    'ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่',
    'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า'
)

thai_multiplier = ('', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน')


def six_num_to_text(six_num):
    length = len(six_num) > 1
    word_num = ''

    for index, num in enumerate(map(int, six_num)):
        if num:
            if index:
                word_num = thai_multiplier[index] + word_num

            if length and num == 1 and index == 0:
                word_num += 'เอ็ด'
            elif index == 1 and num == 2:
                word_num = 'ยี่' + word_num
            elif index != 1 or num != 1:
                word_num = thai_num[num] + word_num

        elif num == 0 and index == 0 and length == 0:
            word_num = 'ศูนย์'

    return word_num


def split_six(num_txt):
    num_txt = num_txt[::-1]
    list_six_num = range(0, len(num_txt), 6)

    result = list(map(
        lambda i: num_txt[i:i+6],  list_six_num
    ))

    return result


def add_text_million(word_num):
    result = ''

    for index, t in enumerate(reversed(word_num)):
        if index == 0:
            result = t
        else:
            result = result + 'ล้าน' + t

    return result


def round_2_decimal(number):
    number = decimal.Decimal(number)
    number = number.quantize(
        decimal.Decimal('.01'),
        rounding=decimal.ROUND_HALF_UP
    )

    text_num = '{:0.2f}'.format(number)
    return text_num


def left_num_to_text(number):

    left_num_list = split_six(number)

    left_text_list = []
    for i in left_num_list:
        left_text_list.append(six_num_to_text(i))

    left_text = add_text_million(left_text_list)
    return left_text


def num_to_words(number):

    text_num = '{}'.format(number)

    split_num = text_num.split('.')

    left_num = split_num[0]

    result = left_num_to_text(left_num)

    if len(split_num) > 1:
        right_num = split_num[1]
        right_text = ''
        if not right_num == '0':
            for i in map(int, right_num):
                right_text = right_text + thai_num[i]
            result = result + 'จุด' + right_text

    return result


def num_to_currency(number):

    number = round_2_decimal(number)

    split_num = number.split('.')

    left_num = split_num[0]
    left_text = left_num_to_text(left_num)

    right_num = split_num[1]
    right_text = six_num_to_text(right_num[::-1].rstrip('0'))

    if right_num == '00':
        result = left_text + 'บาทถ้วน'
    else:
        if left_num == '0':
            result = right_text + 'สตางค์'
        else:
            result = left_text + 'บาท' + right_text + 'สตางค์'

    return result


class Num2Word_TH(object):
    def to_cardinal(self, number):
        return num_to_words(number)

    def to_ordinal(self, number):
        return num_to_words(number)

    def to_currency(self, number):
        return num_to_currency(number)
