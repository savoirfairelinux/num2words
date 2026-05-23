# -*- coding: utf-8 -*-
"""Demo script for manually testing every supported num2words language."""

from __future__ import unicode_literals

import argparse
import os
import sys

# Ensure the demo loads the local source tree when run from tests/.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from num2words import CONVERTER_CLASSES, num2words

SAMPLE_CARDINALS = [0, 1, 5, 11, 21, 103, 1000000, 1234567, 3.14]
SAMPLE_ORDINALS = [1, 2, 11, 21, 101]
SAMPLE_YEARS = [1999, 2024]
SAMPLE_CURRENCY = 1.23
CURRENCY_CODE = 'USD'


def format_result(value, converter, lang, to, **kwargs):
    try:
        return num2words(value, lang=lang, to=to, **kwargs)
    except Exception as exc:
        return "<error: {}>".format(exc)


def demo_language(lang):
    print('=' * 72)
    print('Language:', lang)
    print('-' * 72)

    print('cardinal examples:')
    for value in SAMPLE_CARDINALS:
        text = format_result(value, num2words, lang, 'cardinal')
        print('  {:>10} -> {}'.format(value, text))

    print('\nordinal examples:')
    for value in SAMPLE_ORDINALS:
        text = format_result(value, num2words, lang, 'ordinal')
        print('  {:>10} -> {}'.format(value, text))

    print('\nyear examples:')
    for value in SAMPLE_YEARS:
        text = format_result(value, num2words, lang, 'year')
        print('  {:>10} -> {}'.format(value, text))

    print('\ncurrency example:')
    currency_text = format_result(SAMPLE_CURRENCY, num2words, lang, 'currency', currency=CURRENCY_CODE)
    print('  {:>10} {} -> {}'.format(SAMPLE_CURRENCY, CURRENCY_CODE, currency_text))


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Manual demo for num2words languages.')
    parser.add_argument('-l', '--lang', help='Language code to test (default: all languages)')
    parser.add_argument('-a', '--all', action='store_true', help='Test all supported languages')
    parser.add_argument('-q', '--quiet', action='store_true', help='Only print language names and success/failure statuses')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    languages = sorted(CONVERTER_CLASSES.keys())

    if args.lang:
        langs_to_test = [args.lang]
    elif args.all:
        langs_to_test = languages
    else:
        langs_to_test = languages

    if args.quiet:
        for lang in langs_to_test:
            try:
                _ = format_result(1, num2words, lang, 'cardinal')
                print('OK -', lang)
            except Exception as exc:
                print('FAIL -', lang, exc)
        return 0

    for lang in langs_to_test:
        demo_language(lang)

    return 0


if __name__ == '__main__':
    sys.exit(main())
