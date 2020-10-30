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
from decimal import Decimal
from .base import Num2Word_Base
#-------------数字转中文字符 Number to Chinese character----------by icn.bing@gmail.com-
#Support any [int string] type of number
#Only MAX 15 numbers for float types are supported,!han 15 numbers not accurate!!!
#If you have any questions, please contact:icn.bing@gmail.com
class Num2Word_ZH(Num2Word_Base):
    CURRENCY_FORMS = {
        'CNY': ('元', ('角', '分')),
        'USD': ('美元', '美分'),
        'EUR': ('欧元', '分')
        }
    
    def set_high_numwords(self, high):
        max = 4 * len(high)
        for word, n in zip(high, range(max, 0, -4)):
            self.cards[10 ** n] = word

    def str_to_number(self, value):
        # delete [,'] char, 
        # return:string
        if ',' in value:
            value = value.replace(',', '' )
        elif '\'' in value:
            value = value.replace('\'','')
        # verify the value if it is a number!
        try:
           value = Decimal(value)
        except Exception as e:
            raise TypeError(self.errmsg_nonnum % value)
        # Processing the beginning and end [0 .]
        return str(value)
    def num_to_str(self, value):
        #[int float] to string
        #return:string
        if not isinstance(value, str):
            val  = str(value)
            if isinstance(value, int):
                return val
            elif 'e' not in str(value) and len(str(value)) < 16:
                return val
            else:
                raise  TypeError('the float (%s) lens than 16,\
                dot not suppurt,use [string] to suppurt' % value)
        return value
    def to_cardinal(self, value, capital = False):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        try:
            assert '.' not in value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value, capital)
       
        out = ""
        if value[0] == '-':
            value = value[1:]
            out = self.negword
        val = self.splitnum(value)
        out = out + val
        if capital:
            out = self.zh_to_cap(out)
        return out

    def to_cardinal_float(self, value, capital = False):

        pre, post = self.float2tuple(value)

        out = self.to_cardinal(pre) + (self.pointword) + self.num_to_base(post)
        if capital:
            out = self.zh_to_cap(out)
        return out
    def splitnum(self, value):
        #string
        #int(value) >= 0
        out = ''
        value = value[::-1]
        val_bit = 1
        for num in value:
            i = int(num)
            x, y = divmod(val_bit, 4) 
            if y != 0:
                n = y
            elif x % 2 != 0:
                n = 4
            else:
                n = 8
            out = out + self.cards[i] + self.cards[10**n]
            val_bit = val_bit + 1
        out = out[-2::-1]
        out = self.clean(out)
        return out
    
    def num_to_base(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        out = ''
        for i in range(len(value)):
            x = int(value[i])
            out = out + self.cards[x]
        return out
    
    def float2tuple(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        if '.' in value:
            pre, post = str(value).split('.')
            return pre , post
        else:
            raise  TypeError('The value (%s) no them a float number' % value) 

    def clean(self, value):
        #clear chars in REP_map 
        out = value
        for rep_w in self.REP_map:
            while rep_w[0] in out:
                out = out.replace(rep_w[0],rep_w[1])
        if len(out) > 1 and out[-1] == '零':
            out = out [:-1]
        return out

    def verify_ordinal(self, value):
        if '.' in value:
            raise TypeError(self.errmsg_floatord % value)
        if '-' in value:
            raise TypeError(self.errmsg_negord % value)

    def to_ordinal(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        self.verify_ordinal(value)
        out = self.to_cardinal(value).replace('零', '〇')
        if len(out) >= 2 and out[0] == '一' and out[1] == '十':
            out = out[1:]
        out = '第' + out
        return out

    def to_ordinal_num(self, value):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        self.verify_ordinal(value)
        return '第' + value

    def to_year(self, value, **kwargs):
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        self.verify_ordinal(value)
        return self.num_to_base(value).replace('零', '〇')+'年'

    def to_currency(self, value, currency='CNY', capital=True):
        #Only 2 decimal places are supported
        #More than [0.00] digits are rounded 
        """
        Args:
            val: Numeric value
            currency (str): Currency code
            capital (bool): Select the capital form of a Chinese numeral
        Returns:
            str: 

        """
        if not isinstance(value, str):
            value  = self.num_to_str(value)
        try:
            cr = self.CURRENCY_FORMS[currency]
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))
        out = ''
        if '.' not in value:
            out = out + self.to_cardinal(value) + cr[0] + '整'
        else:
            out = out + self.to_currency_float(value,currency, capital)
            
        if capital:
            out = self.zh_to_cap(out)

        return  out
    
    def to_currency_float(self, value, currency, capital):

        cr = self.CURRENCY_FORMS[currency]
        out = ''
        pre, post = self.float2tuple(value)
        if len(post) == 1:
            post = post+'0'
        elif len(post) > 2 and int(post[2]) >= 5:
            post = format(int(post[:2]) + 1, '02d')
        else:
            post = post[:2]
        if post == '00':
            return self.to_currency(pre, currency, capital)
        if pre != '0':
            out = self.to_cardinal(pre) + cr[0]
        if currency == 'CNY':          
            for i in range(2):
                curr = int(post[i])
                out = out + self.cards[curr]
                if curr != 0:
                    out = out + cr[1][i]
            out = out.lstrip('零圆元').rstrip('零')
        else:
            out = out + self.to_cardinal(int(post)) + cr[1] 
            out = out.strip('零欧美圆元')
        return out

    def zh_to_cap(self,value):
        #Select the capital form of a Chinese numeral
        out = value
        for cap_w in self.CAP_map:
            if cap_w[0] in out:
                out = out.replace(cap_w[0],cap_w[1])
        return out
    def setup(self):
        self.errmsg_nonnum = "The value (%s) no them a number,don't Decimal to [long, int, float]"
        self.errmsg_floatord = "Cannot treat float %s as ordinal|year."
        self.errmsg_negord = "Cannot treat negative num %s as ordinal|year."
        self.precision = 2
        self.negword = "负"
        self.pointword = "点"
        self.high_numwords = [
            '亿',
            '万'
            ]
        self.mid_numwords = [
            (1000,'千'),
            (100,'百'),
            (10,'十')
            ]
        self.low_numwords = [
            "九",
            "八",
            "七",
            "六",
            "五",
            "四",
            "三",
            "二",
            "一",
            "零"
            ]
        
    CAP_map = [
        ("千", "仟"), 
        ("百", "佰"),  
        ("十", "拾"),
        ("九", "玖"),
        ("八", "捌"),
        ("七", "柒"),
        ("六", "陆"),
        ("五", "伍"),
        ("四", "肆"),
        ("三", "叁"),
        ("二", "贰"),
        ("一", "壹"),
        ("元", "圆"),
    ]
    REP_map = [
        ('零千','零'),
        ('零百','零'),
        ('零十','零'),
        ('零零','零'),
        ('零万','万'),
        ('零亿','亿'),
        ('亿万','亿')
        ]

