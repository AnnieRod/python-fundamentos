
#Cuenta regresiva

def countDown(num):          #decian que solo un numero asi que pense que no podia usar lo de inicio-fin-intervalo
    countList = []
    for i in range(num+1):
        countList.append(num)
        num-=1
    return countList

x = countDown(10)
print(x)  

#2. Imprimir y devolver

def impDel (lista):
    print(lista[0])
    return lista[1]

print(impDel([1,2]))

#3. Primero mas longitud

def moreLength(lista):
    return lista[0]+(len(lista))

print(moreLength([1,2,3,4,5]))

#4. Valores mayores que el segundo

def moreThanSecond(nums):
    newList = []
    countNum = 0
    if (len(nums) > 2):
        for i in range(len(nums)):  
            if (nums[i] > nums[1]):
                newList.append(nums[i])
                countNum+=1
        print(countNum)
        return newList
    else:
        return False

print(moreThanSecond([5,2,3,2,1,4]))
print(moreThanSecond([3]))

#me daba mal porque agregaba el i en vez del num[i]
#prints me ayudaron a ver que la indentacion de return y print count estaban adentro de if y por eso no sacaban el total

#5. Esa longitud, ese valor 

def doubleFun(length, values):
    newList = []
    for i in range(length):
        newList.append(values)
    return newList

print(doubleFun(4,7))
print(doubleFun(6,2))



