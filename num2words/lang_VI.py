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
from .currency import parse_currency_parts, prefix_currency

# This code for Vietnam number spelling. It based on tntxtnt's code on daynhauhoc.com

class Num2Word_VI(Num2Word_Base):

    CURRENCY_FORMS = {
        'VND': (('đồng', 'đồng'), ('xu', 'xu')),
        'USD': (('Đô la Mỹ', 'Đô la Mỹ'), ('xu', 'xu')),
    }

    def __init__(self, vn_muoi='mươi', vn_nghin='nghìn', vn_bon='bốn', vn_lam='lăm', vn_le='lẻ', vn_ty='tỷ', vn_doc_so_rong=False):
        
        self.vn_chu_so = ('không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười')
        self.vn_muoi = vn_muoi
        self.vn_tram = 'trăm'
        self.vn_nghin = vn_nghin
        self.vn_trieu = 'triệu'
        self.vn_ty = vn_ty
        self.vn_mot = 'mốt'
        self.vn_bon = vn_bon
        self.vn_lam = vn_lam
        self.vn_le = vn_le
        self.vn_doc_so_rong = vn_doc_so_rong
    def to_vn_str(self, s):
        return self._arbitrary(s.lstrip('0'))
    def _int(self, c):
        return ord(c) - ord('0') if c else 0
    def _LT1e2(self, s):
        if len(s) <= 1: return self.vn_chu_so[self._int(s)]
        if s[0] == '1':
            ret = self.vn_chu_so[10]
        else:
            ret = self.vn_chu_so[self._int(s[0])]
            if self.vn_muoi: ret += ' ' + self.vn_muoi
            elif s[1] == '0': ret += ' mươi'
        if s[1] != '0':
            ret += ' '
            if   s[1] == '1' and s[0] != '1': ret += self.vn_mot
            elif s[1] == '4' and s[0] != '1': ret += self.vn_bon
            elif s[1] == '5': ret += self.vn_lam
            else: ret += self.vn_chu_so[self._int(s[1])]
        return ret
    def _LT1e3(self, s):
        if len(s) <= 2: return self._LT1e2(s)
        if s == '000': return ''
        ret = self.vn_chu_so[self._int(s[0])] + ' ' + self.vn_tram
        if s[1] != '0':
            ret += ' ' + self._LT1e2(s[1:])
        elif s[2] != '0':
            ret += ' ' + self.vn_le + ' ' + self.vn_chu_so[self._int(s[2])]
        return ret
    def _LT1e9(self, s):
        if len(s) <= 3: return self._LT1e3(s)
        if s == '000000' or s == '000000000': return ''
        mid = len(s) % 3 if len(s) % 3 else 3
        left, right = self._LT1e3(s[:mid]), self._LT1e9(s[mid:])
        vn_hang = self.vn_nghin if len(s) <= 6 else self.vn_trieu
        if not left:
            if not self.vn_doc_so_rong: return right
            else: return self.vn_chu_so[0] + ' ' + vn_hang + ' ' + right
        if not right: return left + ' ' + vn_hang
        return left + ' ' + vn_hang + ' ' + right
    def _arbitrary(self, s):
        if len(s) <= 9: return self._LT1e9(s)
        mid = len(s) % 9 if len(s) % 9 else 9
        left, right = self._LT1e9(s[:mid]), self._arbitrary(s[mid:])
        vn_hang = ' '.join([self.vn_ty] * ((len(s) - mid) // 9))
        if not left:
            if not self.vn_doc_so_rong: return right
            elif right: return self.vn_chu_so[0] + ' ' + vn_hang + ', ' + right
            else: return right
        if not right: return left + ' ' + vn_hang
        return left + ' ' + vn_hang + ' ' + right

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
        return self.number_to_text(number)

    def to_cardinal_float(self, number):
        return self.to_cardinal(number)

    def verify_cardinal(self, value):
        raise NotImplementedError()

    def verify_ordinal(self, value):
        raise NotImplementedError()
    
    def to_ordinal(self, number):
        raise NotImplementedError()

    #def to_splitnum(self, val):
    def to_currency(self, val, currency='VND', cents=False, separator=',',
                    adjective=False):
        """
        Args:
            val: Numeric value
            currency (str): Currency code
            cents (bool): Verbose cents
            separator (str): Cent separator
            adjective (bool): Prefix currency name with adjective
        Returns:
            str: Formatted string

        """
        left, right, is_negative = parse_currency_parts(val)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]

        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            cr1 = prefix_currency(self.CURRENCY_ADJECTIVES[currency], cr1)

        minus_str = "%s " % self.negword if is_negative else ""
        cents_str = self._cents_verbose(right, currency) \
            if cents else self._cents_terse(right, currency)

        return u'%s%s %s%s %s %s' % (
            minus_str,
            self.to_cardinal(left),
            self.pluralize(left, cr1),
            separator,
            cents_str,
            self.pluralize(right, cr2)
        )      