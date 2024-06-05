from funciones_cargar_guardar import guardar, cargar

def validar_contraseña(contra):
    yuca = cargar
    contraseña_correcta = "yosoyelcordi"
    if contra == contraseña_correcta:
        print("Contraseña correcta...")
        while True:
            print("**********************************************")
            menu = (
                "1 trainers\n"
                "2 campers\n"
                "3 rutas\n"
                "4 salir"
            )
            print(menu)
            opcion = input("Ingrese una opción: ")
            try:
                opcion = int(opcion)
                if opcion == 1:
                    menu_trainers = (
                        "1 para agregar trainers\n"
                        "2 para cambiar informacion de trainer"
                    )
                    print(menu_trainers)
                    submenu = input("Ingrese una opción: ")
                    if submenu == "1":
                        from funciones_traines import agragar_trainer
                    elif submenu == "2":
                        
                        pass
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion == 2:
                    menu_campers = (
                        "1 para calificar prueba de ingreso: \n"
                        "2 cambiar estado campers: \n"
                        "3 ver campers: "
                    )
                    print(menu_campers)
                    submenu1 = int(input("Ingrese una opción: "))
                    if submenu1 == 1:
                        
                        docu_buscar = int(input("numero usuario:  "))
                        if str(docu_buscar) in yuca ["ingresados"]: 
                            nota1 = int(input("ingrese nota del prueba 1: "))
                            nota2 = int(input("ingrese nota del prueba 2: "))
                            nota = (nota1 + nota2)/2
                            nota_final = int(nota)/2 
                            if 59 <= int(nota_final) and int(nota_final) <= 100:
                                yuca["ingresados"][str(docu_buscar)]["estados"] = "aprobado"
                               
                                guardar(yuca)
                                print("Estado cambiado con éxito")
                            else:
                                yuca["ingresados"][str(docu_buscar)]["estados"] = "reprobado"
                                guardar(yuca)
                        else:
                            print("Usuario no encontrado")
                    elif submenu1 == 2:
                       
                        pass
                    elif submenu1 == 3:
                        import json
                        from funciones_cargar_guardar import mostrar_informacion 
                        
                        ruta = 'usuarios_delta.json'
                        mostrar_informacion(ruta)
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion == 3:
                    menu_rutas = (
                        "1 agregar rutas\n"
                        "2 cambiar de ruta a los grupos"
                    )
                    print(menu_rutas)
                    submenu = input("Ingrese una opción: ")
                    if submenu == 1:
                       import funciones_cargar_guardar as hola 
                       bb = hola.cargar_ruta(rutas)
                       rutas ={ }
                       rutas["ruta"] = input("nombre ruta")
                       print("favor asignar grupo a la ruta")
                       grupos = (
                           "aa1\n",
                           "bb2\n",
                           "cc3\n"
                       )
                       print (grupos)
                       ruta["grupo asignado: "] = input(">> ")
                       hola.guardar_ruta(bb)
                    elif submenu == "2":
                        
                        pass
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion == 4:
                    print("Saliendo...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número. Intente nuevamente.")
    else:
        print("Contraseña incorrecta. Intente nuevamente.") 