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

# Code modified from function đọc số thành chữ, số lớn bao nhiêu cũng cân tất obtained from https://daynhauhoc.com/t/share-code-doc-so-thanh-chu-so-lon-bao-nhieu-cung-can-tat/62701/18
# Thank to tntxtnt.
# Cảm ơn anh rất nhiều.

from __future__ import unicode_literals
from .base import Num2Word_Base
from .compat import to_s
from .currency import parse_currency_parts

class Num2Word_VI(Num2Word_Base):

    CURRENCY_FORMS = {
        'VND': ('đồng', 'xu'),
        'USD': ('đô la Mỹ', 'xu Mỹ'),
    }

    def __init__(self, mươi='mươi', nghìn='nghìn', tư='bốn', lăm='lăm', linh='lẻ', tỷ='tỷ', đọc_số_rỗng=True):
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
        self.negword = "âm "
        self.pointword = "phẩy"
        self.is_title = False
        self.precision = 2
        
    def to_vn_str(self, s):
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
            elif right: return self.chữ_số[0] + ' ' + hang + ' ' + right
            else: return right
        if not right: return left + ' ' + hang
        return left + ' ' + hang + ' ' + right
        
    def str_to_number(self, number):
        # No need because this code run on string
        return self.to_vn_str(number)
        
    def number_to_tr(self, number):
        # This code run on string not number
        number_str = str(number)
        return self.to_vn_str(number_str)
        
    def to_cardinal(self, value):
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = self.negword

        words = self.number_to_tr(value)
        return self.title(out + words)
        
    def to_cardinal_float(self, value):
        try:
            float(value) == value
        except (ValueError, TypeError, AssertionError, AttributeError):
            raise TypeError(self.errmsg_nonnum % value)

        pre, post = self.float2tuple(float(value))

        out = [self.to_cardinal(pre)]
        
        if self.precision:
            out.append(self.title(self.pointword))

        # 2 decimal places
        if post < 100:
            out.append(self.to_cardinal(post))

        # Maybe change to 2 decimal places only if it needed
        if post > 100:
            post = str(post)
            post = '0' * (self.precision - len(post)) + post

            for i in range(self.precision):
                curr = int(post[i])
                out.append(to_s(self.to_cardinal(curr)))

        return " ".join(out)
        
    def to_currency(self, number, currency="VND", cents=False, separator=',',
                    adjective=False):
        left, right, is_negative = parse_currency_parts(
            number, is_int_with_cents=cents)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]
            if (cents or right) and not cr2:
                raise ValueError('Decimals not supported for "%s"' % currency)
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        minus_str = self.negword if is_negative else ""
        return '%s%s %s%s %s' % (
            minus_str,
            ' '.join(self.to_cardinal(left).split()),
            cr1,
            ' ' + self.to_cardinal(right)
            if cr2 else '',
            cr2 if cr2 else '',
        )

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = 'TCN' if not suffix else suffix
        high, low = (val // 100, val % 100)
        valtext = 'Năm ' + self.to_cardinal(val)
        return (valtext if not suffix
                else "%s %s" % (valtext, suffix))