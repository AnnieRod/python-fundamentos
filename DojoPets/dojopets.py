
class Ninja:

    def __init__(self, name, last_name, treats, pet_food, pet):
        self.name = name
        self.lastname = last_name
        self.treats = treats
        self.petfood = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def wash(self): 
        self.pet.noise()
        return self
    
    #incluí los dos siguientes metodos por necesidad
    def pet_data(self):
        self.pet.pet_status()
        return self
    
    def nap_time(self):
        self.pet.sleep()
        return self
