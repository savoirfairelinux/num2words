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

import contextlib
import io
import runpy
import sys
from unittest import TestCase
from unittest.mock import patch


class RunpyTest(TestCase):
    def invoke(self, *args):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(sys, 'argv', ['num2words'] + list(args)):
            with contextlib.redirect_stdout(stdout):
                with contextlib.redirect_stderr(stderr):
                    with self.assertRaises(SystemExit) as result:
                        runpy.run_module('num2words', run_name='__main__')
        code = result.exception.code
        return (0 if code is None else code,
                stdout.getvalue().replace('\r\n', '\n'), stderr.getvalue())

    def test_conversion(self):
        self.assertEqual(self.invoke('150')[:2],
                         (0, 'one hundred and fifty\n'))
        self.assertEqual(self.invoke('150', '--lang', 'es')[:2],
                         (0, 'ciento cincuenta\n'))

    def test_information(self):
        for option in ('--help', '--version', '--list-languages',
                       '--list-converters'):
            with self.subTest(option=option):
                code, output, error = self.invoke(option)
                self.assertEqual(code, 0)
                self.assertTrue(output)
                self.assertEqual(error, '')
        self.assertIn('num2words==', self.invoke('--version')[1])

    def test_invalid_arguments(self):
        self.assertNotEqual(self.invoke()[0], 0)
        code, output, error = self.invoke('not-a-number')
        self.assertEqual(code, 1)
        self.assertIn('not-a-number', error)
