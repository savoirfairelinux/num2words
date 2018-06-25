#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import unittest

import delegator


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
    """test the command line app"""
    def setUp(self):
        self.cli = CliCaller()

    def test_cli_help(self):
        """num2words without arguments should exit with status 1
        and show docopt's default short usage message
        """
        output = self.cli.run_cmd()
        self.assertEqual(output.return_code, 1)
        self.assertTrue(output.err.startswith('Usage:'))

    def test_cli_default_lang(self):
        """default to english
        """
        output = self.cli.run_cmd(150)
        self.assertEqual(output.return_code, 0)
        self.assertEqual(output.out.strip(),
                         "one hundred and fifty point zero")

    def test_cli_with_lang(self):
        """you should be able to specify a language
        """
        output = self.cli.run_cmd(150, '--lang', 'es')
        self.assertEqual(output.return_code, 0)
        self.assertEqual(output.out.strip(),
                         "ciento cincuenta punto cero")
