

import json

def mostrar_informacion(ruta):
    try:
        with open(ruta) as contenido:
            cursos = json.load(contenido)
            print(cursos)
    except FileNotFoundError:
        print("El archivo '{}' no fue encontrado.".format(ruta))
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON '{}'.".format(ruta))
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == '__main__':
    ruta = 'docentes.json'
    mostrar_informacion(ruta)

    



    
