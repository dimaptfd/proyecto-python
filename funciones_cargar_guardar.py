import json
nombre_archivo = 'usuarios_delta.json'
def cargar():
    try: 
        with open(nombre_archivo, "r") as read:
            datos = json.load(read)
            return datos
    except FileNotFoundError:
        return {"ingresados": { } }
    
def guardar(nuevos_datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(nuevos_datos ,archivo, indent=4)






def guardar_trainers(nuevos_datos):
    nombre_archivo = 'rutas.json'
    with open(nombre_archivo, "w") as archivo:
        json.dump(nuevos_datos ,archivo, indent=4)


def mostrar_informacion(ruta):
    try:
        with open(ruta) as contenido:
            datos_usuario = json.load(contenido)
            
            for usuario, datos in datos_usuario["ingresados"].items():
                print(f"Información del usuario {usuario}:")
                
                print(f"  Nombres: {datos['nombres']}")
                print(f"  Apellidos: {datos['apellidos']}")
                print(f"  Dirección: {datos['direccion']}")
                print(f"  Número de teléfono: {datos['num_tel']}")
                print(f"  Estado: {datos['estados']}")
                print()
                
    except FileNotFoundError:
        print("El archivo '{}' no fue encontrado.".format(ruta))