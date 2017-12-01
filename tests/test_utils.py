from unittest import TestCase

from num2words.utils import splitbyx


class TestUtils(TestCase):
    def test_splitbyx(self):
        self.assertEqual(list(splitbyx(str(12), 3)), [12])
        self.assertEqual(list(splitbyx(str(1234), 3)), [1, 234])
        self.assertEqual(list(splitbyx(str(12345678900), 3)), [12, 345, 678, 900])
        self.assertEqual(list(splitbyx(str(1000000), 6)), [1, 0])

        self.assertEqual(list(splitbyx(str(12), 3, format_int=False)), ['12'])
        self.assertEqual(list(splitbyx(str(1234), 3, format_int=False))
                         , ['1', '234']
                         )
        self.assertEqual(list(splitbyx(str(12345678900), 3, format_int=False)),
                         ['12', '345', '678', '900']
                         )
        self.assertEqual(list(splitbyx(str(1000000), 6, format_int=False)),
                         ['1', '000000']
                         )
