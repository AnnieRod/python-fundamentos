#Basico: imprime numeros de 0 a 150
for i in range(151): 
    print(i)

#Multiplos de 5: imprime multiplos de 5 entre 5 y 1000
for i in range(5,1000,5):
    print(i)

#Contar al estilo dojo: imprime enteros de 1 a 100. Si es divisible por 5 imprime Coding, si es divisible por 10 Coding Dojo
for i in range(1,101):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 == 0):
        print("Coding")
    else: 
        print(i)

#Whoa, es un "gran idiota": Agregar enteros IMPARES del 0 a 500000 e imprime suma final
sumAll= 0
for i in range (500000):
    if (i % 2 != 0):
        sumAll += i

print(sumAll)

#Cuenta regresiva de a 4: Imprime positivos desde 2018 de 4 en 4 hacia abajo
for i in range(2018, 0,-4):
    print(i)

#Contador flexible: Imprime enteros de mult, dentro del rango de las dos variables. 
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,(highNum+1)):
    if (i % mult == 0):
        print(i)

