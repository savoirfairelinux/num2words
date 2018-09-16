#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import unittest

import delegator
import num2words


class CliCaller(object):

    def __init__(self):
        self.cmd = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                    "..", "bin", "num2words"))
        self.cmd_list = ["python", self.cmd]

    def run_cmd(self, *args):
        cmd_list = self.cmd_list + [str(arg) for arg in args]
        cmd = " ".join(cmd_list)
        return delegator.run(cmd)


class CliTestCase(unittest.TestCase):
    """Test the command line app"""

    def setUp(self):
        self.cli = CliCaller()

    def test_cli_help(self):
        """num2words without arguments should exit with status 1
        and show docopt's default short usage message
        """
        output = self.cli.run_cmd()
        self.assertEqual(output.return_code, 1)
        self.assertTrue(output.err.startswith('Usage:'))

    def test_cli_list_langs(self):
        """You should be able to list all availabe languages
        """
        output = self.cli.run_cmd('--list-languages')
        self.assertEqual(
            sorted(list(num2words.CONVERTER_CLASSES.keys())),
            output.out.strip().split(os.linesep)
        )
        output = self.cli.run_cmd('-L')
        self.assertEqual(
            sorted(list(num2words.CONVERTER_CLASSES.keys())),
            output.out.strip().split(os.linesep)
        )

    def test_cli_list_converters(self):
        """You should be able to list all available converters
        """
        output = self.cli.run_cmd('--list-converters')
        self.assertEqual(
            sorted(list(num2words.CONVERTES_TYPES)),
            output.out.strip().split(os.linesep)
        )
        output = self.cli.run_cmd('-C')
        self.assertEqual(
            sorted(list(num2words.CONVERTES_TYPES)),
            output.out.strip().split(os.linesep)
        )

    def test_cli_default_lang(self):
        """Default to english
        """
        output = self.cli.run_cmd(150)
        self.assertEqual(output.return_code, 0)
        self.assertEqual(
            output.out.strip(),
            "one hundred and fifty point zero"
        )

    def test_cli_with_lang(self):
        """You should be able to specify a language
        """
        output = self.cli.run_cmd(150, '--lang', 'es')
        self.assertEqual(output.return_code, 0)
        self.assertEqual(
            output.out.strip(),
            "ciento cincuenta punto cero"
        )

    def test_cli_with_lang_to(self):
        """You should be able to specify a language
        """
        output = self.cli.run_cmd(150.55, '--lang', 'es', '--to', 'currency')
        self.assertEqual(output.return_code, 0)
        self.assertEqual(
            output.out.strip(),
            "ciento cincuenta euros con cincuenta y cinco centimos"
        )
