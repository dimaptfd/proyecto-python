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
        return {"ingresados": { }}

def eliminar_users(datos):
    with open(nombre_archivo, "w") as archivo:
        json.pop(datos ,archivo, indent=4)




    
