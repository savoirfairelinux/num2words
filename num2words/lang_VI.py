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

from .base import Num2Word_Base

# This code for Vietnam number spelling. It based on tntxtnt's code on daynhauhoc.com

class Num2Word_VI(Num2Word_Base):

    def __init__(self, mươi='mươi', nghìn='nghìn', tư='bốn', lăm='lăm', linh='lẻ', tỷ='tỷ', đọc_số_rỗng=False):
        self.chữ_số = ('không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười')
        self.mươi = mươi
        self.trăm = 'trăm'
        self.nghìn = nghìn
        self.triệu = 'triệu'
        self.tỷ = tỷ
        self.mốt = 'mốt'
        self.tư = tư
        self.lăm = lăm
        self.linh = linh
        self.đọc_số_rỗng = đọc_số_rỗng
    def to_vn_str(self, s):
        s = str(s)
        return self._arbitrary(s.lstrip('0'))
    def _int(self, c):
        return ord(c) - ord('0') if c else 0
    def _LT1e2(self, s):
        if len(s) <= 1: return self.chữ_số[self._int(s)]
        if s[0] == '1':
            ret = self.chữ_số[10]
        else:
            ret = self.chữ_số[self._int(s[0])]
            if self.mươi: ret += ' ' + self.mươi
            elif s[1] == '0': ret += ' mươi'
        if s[1] != '0':
            ret += ' '
            if   s[1] == '1' and s[0] != '1': ret += self.mốt
            elif s[1] == '4' and s[0] != '1': ret += self.tư
            elif s[1] == '5': ret += self.lăm
            else: ret += self.chữ_số[self._int(s[1])]
        return ret
    def _LT1e3(self, s):
        if len(s) <= 2: return self._LT1e2(s)
        if s == '000': return ''
        ret = self.chữ_số[self._int(s[0])] + ' ' + self.trăm
        if s[1] != '0':
            ret += ' ' + self._LT1e2(s[1:])
        elif s[2] != '0':
            ret += ' ' + self.linh + ' ' + self.chữ_số[self._int(s[2])]
        return ret
    def _LT1e9(self, s):
        if len(s) <= 3: return self._LT1e3(s)
        if s == '000000' or s == '000000000': return ''
        mid = len(s) % 3 if len(s) % 3 else 3
        left, right = self._LT1e3(s[:mid]), self._LT1e9(s[mid:])
        hang = self.nghìn if len(s) <= 6 else self.triệu
        if not left:
            if not self.đọc_số_rỗng: return right
            else: return self.chữ_số[0] + ' ' + hang + ' ' + right
        if not right: return left + ' ' + hang
        return left + ' ' + hang + ' ' + right
    def _arbitrary(self, s):
        if len(s) <= 9: return self._LT1e9(s)
        mid = len(s) % 9 if len(s) % 9 else 9
        left, right = self._LT1e9(s[:mid]), self._arbitrary(s[mid:])
        hang = ' '.join([self.tỷ] * ((len(s) - mid) // 9))
        if not left:
            if not self.đọc_số_rỗng: return right
            elif right: return self.chữ_số[0] + ' ' + hang + ', ' + right
            else: return right
        if not right: return left + ' ' + hang
        return left + ' ' + hang + ', ' + right

    def number_to_text(self, number):
        number = '{:.2f}'.format(number)
        the_list = str(number).split('.')
        start_word = self.to_vn_str(the_list[0])
        final_result = start_word
        if len(the_list) > 1 and int(the_list[1]) > 0:
            end_word = self.to_vn_str(the_list[1])
            final_result = final_result + ' phẩy ' + end_word
        return final_result

    def to_cardinal(self, number):
        return self.to_vn_str(number)

    def to_cardinal_float(self, number):
        return self.number_to_text(number)

    #def verify_cardinal(self, value):
    #def verify_ordinal(self, value):
    
    def to_ordinal(self, number):
        return self.to_cardinal(number)

    #def to_splitnum(self, val):
    #def to_currency(self, value):

custom_converter = Num2Word_VI(đọc_số_rỗng=True, linh='linh', tư='tư', nghìn='ngàn', mươi=False, tỷ='tỉ', lăm='nhăm')