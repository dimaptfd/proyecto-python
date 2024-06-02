import json

def cargar_y_guardar(nuevos_datos, nombre_archivo='datos.json'):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    datos.append(nuevos_datos)

    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
print("felicitaciones, se ha inscrito satisfactoriamente!!")