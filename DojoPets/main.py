from dojopets import Ninja
from pets import Cat, Pet

#Creación de instancias
mimo = Pet("Duck", "carrots",20,20,"quack quack")
annie = Ninja("Annie","Rod","cookies", "grains",mimo) #se puede definir aqui dentro la mascota?

annie.walk().feed().wash().nap_time().pet_data()

#Instancia con mascota de class hija (ejemplo de herencia y polimorfismo) 
enzo = Cat(type="Enzo", snacks="tuna", energy=60, health=60, sound="meeeow")
carpe = Ninja("Carpe","Diem","peanuts", "cat-chow", enzo)  

carpe.walk().feed().wash().nap_time().pet_data()
