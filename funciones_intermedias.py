#1. Actualiza valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)  #punto 1:   [[5, 2, 3], [15, 8, 9]]

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)  #punto 2: [{'first_name': 'Michael', 'last_name': 'Bryant'}, {'first_name': 'John', 'last_name': 'Rosales'}]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes) #punto 3: {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Andrés', 'Ronaldo', 'Rooney']}

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z) #punto 4: [{'x': 10, 'y': 30}]

#2. Iterar a través de una lista de diccionarios

def iterateDictionary(some_list):
        for playerDic in some_list:
            for nameF,nameL in playerDic.items():
                print(f"{nameF} - {nameL}", end = " ") #python por defecto pone un salto de linea, con el end space se lo quito
            print(" ")


estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(estudiantes)

#3. Obtener valores de una lista de diccionarios

def iterateDictionary2 (key_name, some_list):
    for playName in some_list:        #"para un diccionario en una lista: "
        print(playName[key_name])

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#OTRA SOLUCION PARA ESTE:
# def iterateDictionary2 (key_name, some_list):
#     for i in range(len(some_list)):
#             print(some_list[i][key_name])

#4. Iterar a través de un diccionario con valores de lista

def printInfo(some_dict):
    for keyName in some_dict:
        print(len(some_dict[keyName]), keyName)
        for i in range(len(some_dict[keyName])):
            print(some_dict[keyName][i])
        print("-"*15)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)








