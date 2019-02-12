from unittest import TestCase

from num2words import num2words


class Num2WordsKNTest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(42, lang='hi'), "ನಲವತ್ತ್ ಎರಡು")
        self.assertEqual(num2words(893, lang="hi"), "ಎಂಟು ನೂರು ತೊಂಬತ್ತ ಮೂರು")
        self.assertEqual(num2words(1729, lang="hi"), "ಒಂದು ಸಾವಿರ ಏಳು ನೂರು ಇಪ್ಪತ್ತ್ಒಂಬತ್ತು")

    def test_ordinals(self):
        self.assertEqual(num2words(2, lang='hi'), "ಎರಡನೇ")
        self.assertEqual(num2words(5, lang='hi'), "ಐದನೇ")
        self.assertEqual(num2words(16, lang='hi'), "ಹದಿನಾರನೇ")