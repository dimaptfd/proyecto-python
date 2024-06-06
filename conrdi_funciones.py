from funciones_cargar_guardar import guardar, cargar



def validar_contraseña(contra):
    contraseña_correcta = "yosoyelcordi"
    if contra == contraseña_correcta:
        print("Contraseña correcta...")
        while True:
            menu = (
                "1 trainers\n"
                "2 usuarios/campers\n"
                "3 rutas\n"
                "4 salir"
            )
            print("**********************************************************************")
            print(menu)
            opcion = input("Ingrese una opción: ")
            try:
                opcion = int(opcion)
                if opcion == 1:
                    menu_trainers = (
                        "1 para agregar trainers\n"
                        "2 para cambiar informacion de trainer"
                    )
                    print("**********************************************************************")
                    print(menu_trainers)
                    submenu = input("Ingrese una opción: ")
                    if submenu == "1":
                        from trainer_funciones import agregar_trainer
                        agregar_trainer()
                    elif submenu == "2":
                        pass
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion == 2:
                   
                    from camper_opc_cordi import usuarios_campers
                    usuarios_campers()
                elif opcion == 3:
                    from rutas_opc_cordi import rutas_cordi
                    rutas_cordi()
          
            finally: 
                
                break
    else:
        print("contrase incorrecta...")
             