import os

def mostrar_bienvenida():
    print("¡Hola! Estás navegando en...")
    print("""
 __  __            _  _         ____                
|  \/  |  ___   __| |(_)  __ _ | __ )   ___   _ __  
| |\/| | / _ \ / _` || | / _` ||  _ \  / _ \ | '_ \ 
| |  | ||  __/| (_| || || (_| || |_) || (_) || |_) |
|_|  |_| \___| \__,_||_| \__,_||____/  \___/ | .__/ 
                                             |_|    
""")

def obtener_nombre():
    nombre = input("Vamos a conocerte mejor ¿Cómo te llamas?")
    return nombre

def obtener_edad():
    nac = int(input("Para crear tu perfil, cuéntanos en qué año naciste."))
    return 2022-nac-1

def obtener_estatura():
    estatura = float(input("¿Cuál es tu estatura en metros?"))
    metros = int(estatura)
    centimetros = int((estatura - metros)*100)
    return metros,centimetros

def obtener_genpro():
    genero = input(" Un poco más y queda listo tu perfil. ¿Cuál es el género con el que te identificas? ")
    pronombre = input("Nos aseguramos de respetar la diversidad. Cuentános qué pronombres prefieres que usen contigo ")
    return genero, pronombre

def obtener_ciupa():
    ciudad = input("Queremos saber de qué parte del mundo te conectas. ¿En que ciudad naciste? ")
    pais = input("Una ciudad muy bonita dicen, ¿En que país te ubicas? ")
    return ciudad, pais

def obtener_celular():
    celular = str(input("Para verificar tu cuenta, déjanos tu número de celular "))
    return celular

def obtener_lista_amigos():
    linea = input("Genial. Para terminar, escribe una lista con los nombres de tus amigos, separados por una ','. ")
    amigos = linea.split(",")
    return amigos

def mostrar_perfil(nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos):
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("Nombre: ", nombre)
    print("Edad: ", edad, "años")
    print("Estatura:", metros, "metros y", centimetros, "centimetros")
    print("Género: ", genero)
    print("Tus pronombres: ",pronombre)
    print("Lugar de orígen: ", ciudad,"-", pais)
    print("Teléfono movil: ", celular)
    print("Amigos: ", len(amigos))
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

def opcion_menu():
    print("¿Qué quieres hacer hoy?")
    print("  1. Escribir un mood publico")
    print("  2. Mostrar mi muro")
    print("  3. Revisar los datos de tu cuenta")
    print("  4. Actualizar tu información de perfil")
    print("  5. Iniciar sesión con otro user")
    print("  0. Salir de Mediabop")
    opcion = int(input("Ingresa el numero de la opción que deseas: "))
    while opcion < 0 or opcion > 5:
        print("Ups, no entendí tu elección, intenta nuevamente")
        opcion = int(input("Por favor, selecciona una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Cuéntale a tus amigos qué estas pensando...")
    return mensaje

def mostrar_mensaje(origen, mensaje):
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print(origen+"ha publicado un mood:", mensaje)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

def mostrar_muro(muro):
    print("_-_-_-_-_-_-MURO("+str(len(muro))+"mensajes)-_-_-_-_-_-_-_-_")
    for mensaje in muro:
        print(mensaje)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

def publicar_mensaje(origen, amigos, mensaje, muro):
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print(origen, "dice: ", mensaje)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    muro.apend(mensaje)
    for amigo in amigos:
        if existe_archivo(amigo+":user"):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user", "r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    metros = int(estatura)
    centimetros = int((estatura - metros) * 100)
    genero = archivo_usuario.readline().rstrip()
    pronombre = archivo_usuario.readline().rstrip()
    ciudad = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    celular = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()

    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    archivo_usuario.close()

    return (nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos, estado, muro)

def escribir_usuario(nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, num_amigos, estado):
    archivo_usuario = open(nombre + ".user", "w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(metros + centimetros / 100)+"\n")
    archivo_usuario.write(genero+"\n")
    archivo_usuario.write(pronombre+"\n")
    archivo_usuario.write(ciudad+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(celular+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")    #algo pasa con las variable amigo y muro
    archivo_usuario.write(estado+"\n")
    for mensaje in muro:                                #algo pasa con el prgrama se cierra al cambiar de usuario o 
        archivo_usuario.write(mensaje+"\n")
    archivo_usuario.close()



