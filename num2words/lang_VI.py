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

# This code for Vietnam number spelling. It based on tntxtnt's code on daynhauhoc.com

class Num2Word_VI(object):

    def __init__(self, mươi='mươi', nghìn='nghìn', tư='tư', lăm='lăm', linh='linh', tỷ='tỷ', đọc_số_rỗng=True):
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

# if __name__ == '__main__':
#     test_cases_1 = (
#         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
#         "10", "11", "12", "20", "21", "22", "24", "90", "91", "97",
#         "300", "999", "121", "215", "5121", "39500",
#         "1025217", "51105500", "51000000", "999999999",
#         "5120625952200", "12000000000000000000", "18446744073709551615",
#         "18000000000709551615", "11000000000",
#         "1000015", "1002015", "1000000024",
#         "03215", "", "0000", "00001", "00100",
#         "1844674407370955161518000000000000000000709551615",
#         "0321", "000345", "15", "40430203", "3209", "3500", "3901", "21",
#         "3005", "3055", "9031", "9330",
#         "9000005", "9001005",
#     )
#     test_cases_2 = (
#         ("32000000", "ba mươi hai triệu"),
#         ("32516000", "ba mươi hai triệu năm trăm mười sáu nghìn"),
#         ("32516497", "ba mươi hai triệu năm trăm mười sáu nghìn bốn trăm chín mươi bảy"),
#         ("834291712", "tám trăm ba mươi tư triệu hai trăm chín mươi mốt nghìn bảy trăm mười hai"),
#         ("308250705", "ba trăm linh tám triệu hai trăm năm mươi nghìn bảy trăm linh năm"),
#         ("500209037", "năm trăm triệu hai trăm linh chín nghìn không trăm ba mươi bảy"),
#         ("7312836", "bảy triệu ba trăm mười hai nghìn tám trăm ba mươi sáu"),
#         ("57602511", "năm mươi bảy triệu sáu trăm linh hai nghìn năm trăm mười một"),
#         ("351600307", "ba trăm năm mươi mốt triệu sáu trăm nghìn ba trăm linh bảy"),
#         ("900370200", "chín trăm triệu ba trăm bảy mươi nghìn hai trăm"),
#         ("400070192", "bốn trăm triệu không trăm bảy mươi nghìn một trăm chín mươi hai"),
#         ("10250214", "mười triệu hai trăm năm mươi nghìn hai trăm mười bốn"),
#         ("253564888", "hai trăm năm mươi ba triệu năm trăm sáu mươi tư nghìn tám trăm tám mươi tám"),
#         ("400036105", "bốn trăm triệu không trăm ba mươi sáu nghìn một trăm linh năm"),
#         ("700000231", "bảy trăm triệu không nghìn hai trăm ba mươi mốt"),
#     )

#     custom_converter = NumToVnStr(đọc_số_rỗng=True, linh='lẻ', tư='bốn', nghìn='ngàn', mươi=False, tỷ='tỉ', lăm='nhăm')
#     for i in test_cases_1:
#         print('{} = {}'.format(i, custom_converter.to_vn_str(i)))
#     default_converter = NumToVnStr()
#     for test_case in test_cases_2:
#         i, o = test_case
#         assert default_converter.to_vn_str(i) == o
#         print('\n{}\n{}\n{}'.format(i, default_converter.to_vn_str(i), o))


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

    #def to_cardinal_float(self, value):
    #def verify_cardinal(self, value):
    #def verify_ordinal(self, value):
    
    def to_ordinal(self, number):
        return self.to_cardinal(number)

    #def to_splitnum(self, val):
    #def to_currency(self, value):