from unittest import TestCase

from num2words import num2words


class Num2WordsKNTest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(42, lang="kn"), "ನಲವತ್ತ್ ಎರಡು")
        self.assertEqual(num2words(893, lang="kn"), "ಎಂಟು ನೂರು ತೊಂಬತ್ತ ಮೂರು")
        self.assertEqual(
            num2words(1729, lang="kn"), "ಒಂದು ಸಾವಿರ ಏಳು ನೂರು ಇಪ್ಪತ್ತ್ಒಂಬತ್ತು"
        )

    def test_ordinals(self):
        self.assertEqual(num2words(2, lang="kn"), "ಎರಡನೇ")
        self.assertEqual(num2words(5, lang="kn"), "ಐದನೇ")
        self.assertEqual(num2words(16, lang="kn"), "ಹದಿನಾರನೇ")
