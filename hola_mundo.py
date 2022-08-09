
#Tarea 1
from cmath import phase


print("Hola, mundo")

#Tarea 2
name = "Ana"
print("Hola,", name)
print("Hola, " + name)
print(f"¡Hola {name}!")

#Tarea 3
name = 42
print(f"Hola {42}!")
print("Hola", name,"!")
# print("Hola" + name + "!")
print("Hola " + str(name) + "!")    #BONUS NINJA

#Tarea 4
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}".format(fave_food1,fave_food2))
print(f"Amo comer {fave_food1} y {fave_food2}")

#BONUS NINJA: JUGAR CON MÉTODOS DE STRINGS
phrase = "me encanta comer hamburguesa y malteada"
test = phrase.capitalize()
print(test)

mayus = phrase.upper()
print(mayus)

divided = "no.me.gusta.la zanahoria"
apart = divided.split(".")
print(apart)

friends = ["ross","monica","chandler", "joey", "phoebe"]
united = ", ".join(friends)
print(united)
office = ("jim", "pam", "michael","dwigth")
friends.extend(office)
print(friends)   #ojo, aca no debo poner la variable que cree (si es que la creo), solo el elemento a la que añadi algo

meet = "I know Andy"
other = meet.replace("Andy", "Erin")
print(other)
