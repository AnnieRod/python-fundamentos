class Pet: 

    def __init__(self, type, snacks, energy, health, sound):
        self.type = type
        self.snacks = snacks
        self.energy = energy
        self.health = health
        self.sound = sound
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play (self):
        self.health+= 5
        return self
    
    def noise(self):
        print(f"Your {self.type} goes {self.sound}!")
        return self

    def pet_status(self):
        print(f"{self.type}'s current health: {self.health} - energy: {self.energy}.")


#BONUS SENSEI: Creación de categoría hija Cat
class Cat(Pet):
    def __init__(self, type, snacks, energy, health, sound):
        super().__init__(type, snacks, energy, health, sound)

    def eat(self):
        super().eat()
        return self
    
    def pet_status(self):
        super().pet_status()
        return self
    
    # intento de polimorfismo en sleep, noise y play
    def sleep(self):       
        self.energy += 55
        print("I sleep more than 16 hours a day!")
        return self

    def noise(self): 
        print(f"Your cat {self.type} goes meow!") 
        return self
    
    def play (self):
        self.health+= 15
        print("I'll bite you if you touch my belly")
        return self

#Ejecuta solo aqui pero no al importar 
if __name__ == "__main__":
    enzo = Cat(type="calico", snacks="tuna", energy=60, health=60, sound="meeeow")
    enzo.sleep().noise().play()
