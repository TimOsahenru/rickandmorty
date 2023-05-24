import unittest
from main import Rick, Morty



class TestRick(unittest.TestCase):
    def test_universe_number(self):
        rick = Rick(1)
        self.assertEqual(rick.universe, 1)



class TestMorty(unittest.TestCase):
    def test_universe_number(self):
        morty = Morty(2)
        self.assertEqual(morty.universe, 2)



if __name__ == "__main__":
    unittest.main()