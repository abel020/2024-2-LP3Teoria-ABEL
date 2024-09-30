import gestion_archivos as ga
def error():
    print("A ocurrido un error")

def crear():
    nombre = input("Digite el nombre del archivo txt a crear: ")
    contenido = input("Digite el contenido del archivo txt a crear: ")
    ga.crear_archivo(nombre, contenido)
    print("Archivo creado exitosamente")

def eliminar():
    nombre = input("Digite el nombre del archivo txt a eliminar: ")
    ga.eliminar_archivo(nombre)
    print("Archivo eliminado exitosamente")

def agregar():
    nombre = input("Digite el nombre del archivo txt al que se agregará contenido: ")
    contenido = input("Digite el contenido a agregar al archivo: ")
    ga.agregar_contenido_archivo(nombre, contenido)
    print("Contenido agregado exitosamente")

def listar():
    nombre = input("Digite el nombre del archivo txt a leer: ")
    try:
        print(ga.leer_archivo(nombre))
    except FileNotFoundError:
        print("Archivo no encontrado")

def salir():
    print("Saliendo...")
    exit()

def menu():
    print("Menu")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido de archivo")
    print("5. Salir")
    try:
        opcion = int(input("\nDigite la opción deseada: "))
        if opcion == 1:
            crear()
            menu()
        elif opcion == 2:
            eliminar()
            menu()
        elif opcion == 3:
            agregar()
            menu()
        elif opcion == 4:
            listar()
            menu()
        elif opcion == 5:
            salir()
    except ValueError:
        print("Debe ingresar un número")
        error()

menu()
