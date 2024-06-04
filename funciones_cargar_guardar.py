import json
nombre_archivo = 'usuarios_delta.json'

def guardar(nuevos_datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(nuevos_datos ,archivo, indent=4)



def cargar():
    try: 
        with open(nombre_archivo, "r") as read:
            datos = json.load(read)
            return datos
    except FileNotFoundError:
        return {"ingresados": { } }

def mostrar_informacion(ruta):
    with open(ruta) as contenido:
        cursos = json.load(contenido)
        print(cursos)



def guardar_ruta(nuevos_datos):
    nombre_archivo = 'rutas.json'
    with open(nombre_archivo, "w") as archivo:
        json.dump(nuevos_datos ,archivo, indent=4)



def cargar_ruta():
    try: 
        with open(nombre_archivo, "r") as read:
            datos = json.load(read)
            return datos
    except FileNotFoundError:
        return {"rutas_grupos": { } }