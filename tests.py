import unittest
from main import Rick


class TestRick(unittest.TestCase):
    
    def test_universe_number(self):
        rick = Rick(1)
        self.assertEqual(rick.universe, 1)


if __name__ == "__main__":
    unittest.main()