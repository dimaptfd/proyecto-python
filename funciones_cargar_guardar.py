import json
nombre_archivo = 'usuarios.json'
def validar_documento(documento_numero, datos):
    return documento_numero not in datos.get("ingresados", {})

def registrar_usuario(nombre, documento_numero, datos):
    if not validar_documento(documento_numero, datos):
        return False
    nuevo_usuario = {"nombre": nombre}
    datos["ingresados"][documento_numero] = nuevo_usuario
    guardar(datos)
    return True
        
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






def mostrar_rutas(ruta):
    with open(ruta) as contenido:
        datos_rutas = json.load(contenido)

        for categoria, datos_categoria in datos_rutas.items():
            print(f"** {categoria.upper()} **")
            for ruta, datos_ruta in datos_categoria.items():
                print(f"  {ruta}:")
                print(f"    Trainer: {datos_ruta['trainer']}")
                print(f"    Campers: {', '.join(datos_ruta['campers'])}")
                print(f"    Horario: {datos_ruta['horario']}")
                print(f"    Salón: {datos_ruta['salon']}")
                print(f"    Ruta: {datos_ruta['ruta']}")
                print()
            print()



def guardar_trainers(nuevos_datos):
    nombre_archivo = 'rutas.json'
    with open(nombre_archivo, "w") as archivo:
        json.dump(nuevos_datos ,archivo, indent=4)


def mostrar_informacion(ruta):
    try:
        with open(ruta) as contenido:
            datos_usuario = json.load(contenido)
            
            for usuario, datos in datos_usuario["ingresados"].items():
                print("***************************************************")
                print(f"Información del usuario {usuario}:")
                
                print(f"  Nombres: {datos['nombres']}")
                print(f"  Apellidos: {datos['apellidos']}")
                print(f"  Dirección: {datos['direccion']}")
                print(f"  Número de teléfono: {datos['num_tel']}")
                print(f"  Estado: {datos['estados']}")
                print()
                print("***************************************************")
                
                
    except FileNotFoundError:
        print("El archivo '{}' no fue encontrado.".format(ruta))