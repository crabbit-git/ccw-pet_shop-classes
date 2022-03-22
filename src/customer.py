class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []
    
    def pet_count(self):
        return len(self.pets)
    
    def add_pet(self, pet):
        self.pets.append(pet)
    
    def get_total_value_of_pets(self):
        total_cost = 0
        for pet in self.pets:
            total_cost += pet.price
        return total_cost