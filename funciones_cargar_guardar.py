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
        return{"ingresados": { }}



    
# def buscar_usuario(docu_buscar, archivo='usuarios.json'):
#    try:
#        with open(archivo, 'r') as archivo:
#            datos = json.load(archivo)
#    except FileNotFoundError:
#        return None
#    for user in datos:
#        if user.get("docu") == docu_buscar:
#            return user
#    return None
#
# def cambiar_estado(user, nuevo_estado, archivo='usuarios.json'):
#    if user:
#        user["estado"] = nuevo_estado
#        with open(archivo, 'w') as archivo:
#            json.dump(datos, archivo, indent=4)
#        return True
#    return False