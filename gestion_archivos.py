def crear_archivo(nombre,contenido):
    archivo = open(nombre+".txt","wt")
    archivo.write(contenido)
    archivo.close()

def eliminar_archivo(nombre):
    import os
    os.remove(nombre+".txt")

def agregar_contenido_archivo(nombre,contenido):
    archivo = open(nombre+".txt","at")
    archivo.write("\n"+contenido)
    archivo.close()

def leer_archivo(nombre):
    noticia = open(nombre+".txt", 'rt', encoding='utf-8')
    datos_noticia = noticia.read()
    print (datos_noticia)





