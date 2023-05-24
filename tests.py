import unittest
from main import Rick, Morty, Citadel



class TestRick(unittest.TestCase):
    def test_universe_number(self):
        rick = Rick(1)
        self.assertEqual(rick.universe, 1)
        
        
    def test_has_morty(self):
        rick = Rick(1)
        self.assertFalse(rick.morty)
        
        
    def test_has_pickle(self):
        rick = Rick(2)
        self.assertEqual(rick.pickle, None)
        
        
    def test_morty_can_be_assigned(self):
        rick = Rick(1)
        morty = Morty(2)
        rick.assign_morty(morty)
        self.assertEqual(rick.morty, morty)



class TestMorty(unittest.TestCase):
    def test_universe_number(self):
        morty = Morty(2)
        self.assertEqual(morty.universe, 2)
        
        
    def test_morty_is_assigned(self):
        morty = Morty(2)
        self.assertFalse(morty.is_assigned)
        
        
        
    
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
        
        
    def test_pickle_rick_with_morty(self):
        citadel = Citadel()
        rick = Rick(1)
        morty = Morty(2)
        rick.assign_morty(morty)
        
        citadel.add_residents(rick)
        citadel.add_residents(morty)
        
        citadel.pickle_rick_with_morty()
        residents = citadel.get_all_residents()
        self.assertTrue(residents[0].pickle)
        


if __name__ == "__main__":
    unittest.main()