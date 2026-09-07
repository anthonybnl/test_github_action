import unittest
import mon_module

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(mon_module.addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(mon_module.soustraction(5, 3), 2)