import json

def cargar_y_guardar(nuevos_datos, nombre_archivo='usuarios_delta.json'):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []
        users = { } 
        datos[0] = users


    datos.append(nuevos_datos)

    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

    return datos

    
def buscar_usuario(docu_buscar, archivo='usuarios.json'):
    try:
        with open(archivo, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        return None
    for user in datos:
        if user.get("docu") == docu_buscar:
            return user
    return None

def cambiar_estado(user, nuevo_estado, archivo='usuarios.json'):
    if user:
        user["estado"] = nuevo_estado
        with open(archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        return True
    return False