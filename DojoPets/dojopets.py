
from pets import Pet, Cat

class Ninja:

    def __init__(self, name, last_name, treats, pet_food, pet_info):
        self.name = name
        self.lastname = last_name
        self.treats = treats
        self.petfood = pet_food
        self.pet = Pet(type=pet_info["type"], snacks=pet_info["snacks"], energy=pet_info["energy"], health= pet_info["health"],sound=pet_info["sound"]) 

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

#Creación de instancias
mimo = {"type": "duck","snacks": "carrots", "energy": 50, "health": 50, "sound": "quack quack"}
annie = Ninja("Annie","Rod","cookies", "grains",mimo) #se puede definir aqui dentro la mascota?

annie.walk().feed().wash().nap_time().pet_data()

#Instancia con mascota de class hija (ejemplo de herencia y polimorfismo) -AUN NO FUNCIONA!!!, no incluye al gato como mascota ni se apoya en el diccionario para crearlo
enzo = Cat(type="calico", snacks="tuna", energy=60, health=60, sound="meeeow")
carpe = Ninja("Carpe","Diem","peanuts", "cat-chow", enzo)  

carpe.walk().feed().wash().nap_time().pet_data()