# encoding: UTF-8

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

from __future__ import print_function, unicode_literals

from .lang_ES import Num2Word_ES
from .currency import parse_currency_parts


class Num2Word_ES_MX(Num2Word_ES):

    def to_currency(self, val, longval=True, old=False):
        left, right, is_negative = parse_currency_parts(val, is_int_with_cents=False)
        result = self.to_splitnum(left, hightxt="peso/s",
                                  divisor=1, longval=longval, cents=False)
        result = "%s, %02d/100 M. N." % (result, right)
        # Handle exception, in spanish is "un euro" and not "uno euro"
        return result.replace("uno", "un")
