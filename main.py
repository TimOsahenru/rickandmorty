class Rick():
    def __init__(self, universe):
        self.universe = universe
        self.morty = False
        self.pickle = None
        
        
    def assign_morty(self, morty):
        self.morty = morty
        morty.is_assigned = True
        
        
        
class Morty():
    def __init__(self, universe):
        self.universe = universe
        self.is_assigned = False
        
        
        
class Citadel():
    def __init__(self):
        self.residents = []
        
        
        
    def get_all_residents(self):
        return self.residents
    
    
    def add_residents(self, resident):
        self.residents.append(resident)
        
        
        
    def pickle_rick_with_morty(self):
        for resident in self.residents:
            if isinstance(resident, Rick):
                if resident.morty: resident.pickle = True