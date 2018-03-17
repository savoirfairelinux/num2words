# encoding: UTF-8

# Copyright (c) 2018, Agustín Cruz <agustin.cruz@openpyme.mx>.
# All Rights Reserved.

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


from .lang_ES import Num2Word_ES


class Num2Word_ES_MX(Num2Word_ES):
    CURRENCY_FORMS = {
        'USD': (
            ('dolar', 'dolares'), ('', '')
        ),
        'EUR': (
            ('euro', 'euros'), ('', '')
        ),
        'MXN': (
            ('peso', 'pesos'), ('', '')
        ),
    }

    def _cents_verbose(self, number, currency):
        return '%02d/100' % number

    def to_currency(self, val, currency='MXN', cents=True, seperator=',',
                    adjective=False, is_int_with_cents=False):
        result = super(Num2Word_ES_MX, self).to_currency(
            val, currency=currency, cents=cents, seperator=seperator,
            adjective=adjective, is_int_with_cents=is_int_with_cents,
        )
        if currency == 'MXN':
            result += 'M. N.'
        else:
            result += currency

        return result
