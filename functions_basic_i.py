#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# predicción: 5     

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# predicción: error no definió variable de triangle a concatenar

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# predicción: 5      #como ya retornó no entra al siguiente return

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# predicción: 5     #como ya retorno no ejecuta mas 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# predicción: 5,None            #sin retornar y no almacenar no devuleve un valor, sino none


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# predicción: 3  5  8               (mal, como no retorna no debe poder sumar el resultado de las dos funciones)

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#predicción: "25"                  #al ser strings se juntan, pero no adicionan aritmética

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#predicción: 100 10 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#predicción:  7 14 21 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#predicción: 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#predicción: 500 300 500 300 500             (mal, se me pasó que si no se llama la funcion no imprime lo que esta dentro hasta que se le llame)

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#predicción: 500 500 300 500                #aunque se retorne b, la siguiente imprime 500 porque toma la variable del scope global

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#predicción: 500 500 300 300                #al almacenarlo como b ahora si se vuelve 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#predicción: 1 3 2              #se pueden llamar funciones antes de definirlas sin problema

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#predicción: 1 3 5 10        #a tricky one, hay que tener cuidado de diferenciar los print de los return