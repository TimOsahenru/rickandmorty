import unittest
from main import Rick, Morty, Citadel



class TestRick(unittest.TestCase):
    def test_universe_number(self):
        rick = Rick(1)
        self.assertEqual(rick.universe, 1)



class TestMorty(unittest.TestCase):
    def test_universe_number(self):
        morty = Morty(2)
        self.assertEqual(morty.universe, 2)
        
        
        
    
class TestCitadel(unittest.TestCase):
    def test_has_residents(self):
        citadel = Citadel()
        self.assertEqual(citadel.residents, [])
        
        
    def test_get_all_residents(self):
        citadel = Citadel()
        self.assertEqual(citadel.get_all_residents(), [])
        
        
    def test_add_residents(self):
        citadel = Citadel()
        rick = Rick(1)
        morty = Morty(2)
        
        citadel.add_residents(rick)
        citadel.add_residents(morty)
        
        residents = citadel.get_all_residents()
        self.assertEqual(residents[0], rick)
        self.assertEqual(residents[1], morty)
        


if __name__ == "__main__":
    unittest.main()