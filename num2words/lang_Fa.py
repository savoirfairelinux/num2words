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

from .base import Num2Word_Base


CURRENCY_ir = {
    1: ("ريال",),
    2:("تومان",),
}

ONES = {
    1: ('یک',),
    2: ('دو',),
    3: ('سه',),
    4: ('چهار',),
    5: ('پنج',),
    6: ('شش',),
    7: ('هفت',),
    8: ('هشت',),
    9: ('نه',),
}

TENS = {
    0: ('ده',),
    1: ('یازده',),
    2: ('دوازده',),
    3: ('سیزده',),
    4: ('چهارده',),
    5: ('پانزده',),
    6: ('شانزده',),
    7: ('هفده',),
    8: ('هجده',),
    9: ('نوزده',),
}

TWENTIES = {
    2: ('بیست',),
    3: ('سی',),
    4: ('چهل',),
    5: ('پنجاه',),
    6: ('شصت',),
    7: ('هفتاد',),
    8: ('هشتاد',),
    9: ('نود',),
}

HUNDREDS = {
    1: ('صد',),
    2: ('دویست',),
    3: ('سیصد',),
    4: ('چهارصد',),
    5: ('پانصد',),
    6: ('ششصد',),
    7: ('هفتصد',),
    8: ('هشتصد',),
    9: ('نهصد',),
}

THOUSANDS = {
    1: ('هزار',),  # 10^3
    2: ('میلیون', ),  # 10^6
    3: ('میلیارد', ),  # 10^9
    4: ('بیلیون', ),  # 10^12
    5: ('بیلیارد', ),  # 10^15
    6: ('تریلیون', ),  # 10^18
    7: ('تریلیارد',),  # 10^21
    8: ('کوآدریلیون', ),  # 10^24
    9: ('کادریلیارد', ),  # 10^27
    10: ('کوینتیلیون', ),  # 10^30
}

class Num2Word_FA(Num2Word_Base):
    def __init__():
