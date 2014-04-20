import unittest
from py2chainmap import ChainMap


class Py2ChainMapTestCase(unittest.TestCase):
    def test_init(self):
        ChainMap()

    def test_read_string(self):
        cm = ChainMap({'zebra': 'black', 'snake': 'red'})
        self.assertEqual(cm['zebra'], 'black')

suite = unittest.TestLoader().loadTestsFromTestCase(Py2ChainMapTestCase)

