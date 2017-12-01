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

from num2words.currency import parse_currency_parts
from num2words.utils import splitbyx

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
    result = splitbyx(num_txt, 6, format_int=False)
    result = list(result)[::-1]
    number_list = []
    for i in result:
        number_list.append(i[::-1])
    return number_list


def add_text_million(word_num):
    result = ''

    for index, t in enumerate(reversed(word_num)):
        if index == 0:
            result = t
        else:
            result = result + 'ล้าน' + t

    return result


def round_2_decimal(number):
    integer, cents, negative = parse_currency_parts(
        number, is_int_with_cents=False
    )
    text_num = '{:0.2f}'.format(integer + (cents/100))
    return text_num, negative


def left_num_to_text(number):

    left_num_list = split_six(number)

    left_text_list = []
    for i in left_num_list:
        left_text_list.append(six_num_to_text(i))

    left_text = add_text_million(left_text_list)
    return left_text


def num_to_words(number):

    negative = number < 0

    text_num = '{}'.format(number)

    if negative:
        text_num = text_num.lstrip('-')

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

    if negative:
        result = 'ติดลบ' + result

    return result


def num_to_currency(number):

    number, negative = round_2_decimal(number)

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

    if negative:
        result = 'ติดลบ' + result

    return result


class Num2Word_TH(object):

    def to_cardinal(self, number):
        return num_to_words(number)

    def to_ordinal(self, number):
        return num_to_words(number)

    def to_currency(self, number):
        return num_to_currency(number)
