

#import json
#
#def mostrar_informacion(ruta):
#    try:
#        with open(ruta) as contenido:
#            cursos = json.load(contenido)
#            print(cursos)
#    except FileNotFoundError:
#        print("El archivo '{}' no fue encontrado.".format(ruta))
#    except json.JSONDecodeError:
#        print("Error al decodificar el archivo JSON '{}'.".format(ruta))
#    except Exception as e:
#        print("Ocurrió un error inesperado:", e)
#
#if __name__ == '__main__':
#    ruta = 'docentes.json'
#    mostrar_informacion(ruta)






    
#import json
#
#def mostrar_informacion(ruta):
#    try:
#        with open(ruta) as contenido:
#            datos_usuario = json.load(contenido)
#            
#            for usuario, datos in datos_usuario.items():
#                print(f"Información del usuario {usuario}:")
##                
##                for clave, valor in datos.items():
##                    print(f"{clave}: {valor}")
##                print()
##                
##    except FileNotFoundError:
##        print("El archivo '{}' no fue encontrado.".format(ruta))
##
##if __name__ == "__main__":
##    datos_users = 'u2.json'
##    mostrar_informacion(datos_users)
##
 #   
#
#
#ef validar_contraseña(contra):
 #   contraseña_correcta = "yosoyelcordi"
 #   if contra == contraseña_correcta:
 #       print("Contraseña correcta...")
 #       while True:
 #           menu = (
 #               "1 trainers\n"
 #               "2 campers\n"
 #               "3 rutas\n"
 #               "4 salir"
 #           )
 #           print("**********************************************************************")
 #           print(menu)
 #           opcion = input("Ingrese una opción: ")
 #           try:
 #               opcion = int(opcion)
 #               if opcion == 1:
 #                   menu_trainers = (
 #                       "1 para agregar trainers\n"
 #                       "2 para cambiar informacion de trainer"
 #                   )
 #                   print("**********************************************************************")
 #                   print(menu_trainers)
 #                   submenu = input("Ingrese una opción: ")
 #                   if submenu == "1":
 #                       from funciones_traines import agregar_trainer
 #                       agregar_trainer()
 #                   elif submenu == "2":
 #                       pass
 #                   else:
 #                       print("Opción inválida. Intente nuevamente.")
 #               elif opcion == 2:
 #                   menu_campers = (
 #                       "1 para calificar prueba de ingreso: \n"
 #                       "2 cambiar estado campers: \n"
 #                       "3 ver campers: "
 #                   )
 #                   print("**********************************************************************")
 #                   print(menu_campers)
 #                   submenu1 = int(input("Ingrese una opción: "))
 #                   if submenu1 == 1:
 #                       yuca = cargar()
 #                       docu_buscar = int(input("numero usuario:  "))
 #                       if str(docu_buscar) in yuca["ingresados"]: 
 #                           nota1 = int(input("ingrese nota del prueba 1: "))
 #                           nota2 = int(input("ingrese nota del prueba 2: "))
 #                           nota = (nota1 + nota2)/2
 #                           nota_final = int(nota)/2 
 #                           if 59 <= int(nota_final) and int(nota_final) <= 100:
 #                               yuca["ingresados"][str(docu_buscar)]["estados"] = "aprobado"
 #                               guardar(yuca)
 #                               print("**********************************************************************")
 #                               print("Estado cambiado con éxito")
 #                           else:
 #                               yuca["ingresados"][str(docu_buscar)]["estados"] = "reprobado"
 #                               guardar(yuca)
 #                       else:
 #                           print("Usuario no encontrado")
 #                   elif submenu1 == 2:
 #                       pass
 #                   elif submenu1 == 3:
 #                       from funciones_cargar_guardar import mostrar_informacion
 #                       ruta = 'usuarios_delta.json'
 #                       mostrar_informacion(ruta)
 #                   else:
 #                       print("Opción inválida. Intente nuevamente.")
 #               elif opcion == 3:
 #                   menu_rutas = (
 #                       "1 agregar rutas\n"
 #                       "2 cambiar de ruta a los grupos"
 #                   )
 #                   print("**********************************************************************")
 #                   print(menu_rutas)
 #                   submenu = input("Ingrese una opción: ")
 #                   if submenu == "1":
 #                       import funciones_cargar_guardar as hola 
 #                       bb = hola.cargar_ruta()
 #                       rutas ={ }
 #                       rutas["ruta"] = input("nombre ruta")
 #                       print("favor asignar grupo a la ruta")
 #                       grupos = (
 #                           "aa1\n",
 #                           "bb2\n",
 #                           "cc3"
 #                       )
 #           finally: 
 #               
 #               pass
 #                                   
import funciones_cargar_guardar as hola

def añadagrupo():
    rhlm = hola.cargar
    documento = int(input("Digite el documento"))
    if str(documento) in ["ingresados"]:
        ruta = (
            "java\n",
            "Netcore\n",
            "Nodejs"
        )
        opc1 = int(input("Digite la ruta en la que lo quiere pasar"))
        if opc1 == 1:
            rhlm["java"]["campers"].append(documento)
            hola.guardar(rhlm)
        if opc1 == 2:
            rhlm["Netcore"]["campers"].append(documento)
            hola.guardar(rhlm)
        if opc1 == 3:
            rhlm["Nodejs"]["campers"].append(documento)
            hola.guardar(rhlm)

