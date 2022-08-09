
import Bopred as Red

#AQUI EMPIEZA EL PROGRAMA PRINCIPAL, llama funcion de bienvenida y toma de datos

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Bienvenide ", nombre, ". Estas navegando en MediaBop")

#Vemos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    print("Leyendo datos de user", nombre, "desde archivo")
    (nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos, estado, muro) = Red.leer_usuario(nombre)
#EL USUARIO NO EXISTE
else:
    print()
    edad= Red.obtener_edad()
    (metros, centimetros) = Red.obtener_estatura()
    (genero, pronombre) = Red.obtener_genpro()
    (ciudad, pais) = Red.obtener_ciupa()
    celular = Red.obtener_celular()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

    #INICIA PROGRAMA TRAS CONOCER DATOS DE USUARIO
print("Super. Ya tenemos la info necesaria para crear tu perfil.")
Red.mostrar_perfil(nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos)
Red.mostrar_mensaje(nombre, estado)

#INICIA MENU Y OPCIONES
opcion = 1
while opcion != 0:
    #muestras el menu y le das el valor a la variable opcion
    opcion = Red.opcion_menu()
    #OPCION 1: PUBLICA MENSAJE
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, amigos, estado, muro)
    #OPCION 2: MANDAR MENSAJE A UN GRUPO
    elif opcion == 2:
        estado = Red.mostrar_muro(muro)

    #OPCION 3: PUBLICA DATOS PERFIL
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos)
    #OPCION 4: ACTUALIZAR DATOS DEL PERFIL
    elif opcion == 4:
        edad = Red.obtener_edad()
        (metros, centimetros) = Red.obtener_estatura()
        (genero, pronombre) = Red.obtener_genpro()
        (ciudad, pais) = Red.obtener_ciupa()
        celular = Red.obtener_celular()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos)
    elif opcion == 5:
        nombre = Red.obtener_nombre()
        print("Bienvenide ", nombre, ". Estas navegando en MediaBop")
        if Red.existe_archivo(nombre+".user"):
            print("Leyendo datos de user", nombre, "desde archivo")
            (nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, num_amigos,
             estado) = Red.leer_usuario(nombre)
        else:
            print("Lo sentimos, no puede cambiar por un user no existente")

    elif opcion == 0:
        print("Vas de salida en MediaBop... Guardando perfil en ", nombre+".user")
        Red.escribir_usuario(nombre, edad, metros, centimetros, genero, pronombre, ciudad, pais, celular, amigos, estado, muro)
        print("Archivo", nombre+".user","guardado")
print("¡Gracias por estar en MediaBop! Ten un buen día :) ")
