class Rick():
    def __init__(self, universe):
        self.universe = universe
        
        
        
class Morty():
    def __init__(self, universe):
        self.universe = universe
        
        
        
class Citadel():
    def __init__(self):
        self.residents = []
        
        
        
    def get_all_residents(self):
        return self.residents
    
    
    def add_residents(self, resident):
        self.residents.append(resident)
    