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

from unittest import TestCase

from num2words import CONVERTER_CLASSES, num2words


class CurrencyKeywordTest(TestCase):
    def test_supported_local_currency_preserves_existing_output(self):
        for lang, currency in (
            ('bn', 'BDT'), ('da', 'DKK'), ('id', 'IDR'), ('tr', 'TRY'),
            ('es_CO', 'COP'), ('es_CR', 'CRC'), ('es_GT', 'GTQ'),
            ('es_VE', 'VEF'),
        ):
            for value in (0, 1, 100.55):
                with self.subTest(lang=lang, value=value):
                    self.assertEqual(
                        num2words(value, lang=lang, to='currency',
                                  currency=currency),
                        num2words(value, lang=lang, to='currency'),
                    )

    def test_unsupported_currency_uses_standard_error(self):
        for lang in ('bn', 'da', 'fa', 'id', 'tr', 'es_CO', 'es_CR',
                     'es_GT', 'es_VE'):
            for currency in ('USD', 'XYZ'):
                with self.subTest(lang=lang, currency=currency):
                    with self.assertRaises(NotImplementedError) as error:
                        num2words(100.55, lang=lang, to='currency',
                                  currency=currency)
                    self.assertEqual(
                        str(error.exception),
                        'Currency code "%s" not implemented for "%s"' %
                        (currency, CONVERTER_CLASSES[lang].__class__.__name__),
                    )

    def test_farsi_tomans_are_not_reported_as_rials(self):
        self.assertEqual(num2words(1, lang='fa', to='currency'), 'یک تومان')
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='fa', to='currency', currency='IRR')

    def test_explicit_venezuelan_currency_selects_historical_unit(self):
        self.assertEqual(
            num2words(1, lang='es_VE', to='currency', currency='VEB'),
            'un bolívar',
        )
        self.assertEqual(
            num2words(2, lang='es_VE', to='currency', currency='VEF',
                      old=True),
            'dos bolívares fuertes',
        )
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='es_VE', to='currency', currency='VES')

    def test_legacy_positional_options(self):
        for lang in ('da', 'es_CO', 'es_CR', 'es_GT', 'es_VE'):
            converter = CONVERTER_CLASSES[lang]
            with self.subTest(lang=lang):
                self.assertEqual(converter.to_currency(125, False),
                                 converter.to_currency(125, longval=False))
        converter = CONVERTER_CLASSES['es_VE']
        self.assertEqual(converter.to_currency(1, True, True), 'un bolívar')
