

def validar_contraseña(contra):
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
                        "1 para agregar/eliminar trainers\n"
                        "2 para cambiar informacion de trainer"
                    )
                    print(menu_trainers)
                    submenu = input("Ingrese una opción: ")
                    if submenu == "1":
                        # Implementar agregar/eliminar trainers
                        pass
                    elif submenu == "2":
                        # Implementar cambiar informacion de trainer
                        pass
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion == 2:
                    menu_campers = (
                        "1 para calificar prueba de ingreso\n"
                        "2 cambiar estado campers\n"
                        "3 actualizar informacion"
                    )
                    print(menu_campers)
                    submenu1 = int(input("Ingrese una opción: "))
                    if submenu1 == 1:
                        # Implementar calificar prueba de ingreso
                        docu_buscar = int(input("numero usuario:  "))

                        brr = int(input("ingrese nota del prueva: "))
                        if 59 <= int(brr) <= 100:
                            from funciones_cargar_guardar import buscar_usuario, cambiar_estado
                            user = buscar_usuario(docu_buscar)
                            if user:
                                nuevo_estado = "aprobado"
                                cambiar_estado(user, nuevo_estado)
                                print("Estado cambiado con éxito")
                            else:
                                print("Usuario no encontrado")
                    elif submenu1 == "2":
                        # Implementar cambiar estado campers
                        pass
                    elif submenu1 == "3":
                        # Implementar actualizar informacion
                        pass
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion == 3:
                    menu_rutas = (
                        "1 agregar rutas\n"
                        "2 cambiar de ruta a los grupos"
                    )
                    print(menu_rutas)
                    submenu = input("Ingrese una opción: ")
                    if submenu == "1":
                        # Implementar agregar rutas
                        pass
                    elif submenu == "2":
                        # Implementar cambiar de ruta a los grupos
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