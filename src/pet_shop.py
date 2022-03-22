class PetShop:
    def __init__(self, name, stock, cash):
        self.name = name
        self.stock = stock
        self.total_cash = cash
        self.pets_sold = 0
    
    def total_cash(self):
        return self.total_cash
    
    def stock_count(self):
        return len(self.stock)
    
    def increase_pets_sold(self):
        self.pets_sold += 1
    
    def increase_total_cash(self, transact):
        self.total_cash += transact
    
    def add_pet(self, pet):
        self.stock.append(pet)
    
    def remove_pet(self, pet):
        self.stock.remove(pet)
    
    def find_pet_by_name(self, pet_name):
        for pet in self.stock:
            if pet.name == pet_name:
                return pet