




while True:

    menu_inicio=  (
            "1 ingresar\n"
            "2 para registrar"
            
    )

    menu_ingreso = (
                        "1 camper\n"
                        "2 trainer\n"
                        "3 cordinador"
                    )
    print(menu_inicio)
    menu1 = int(input("="))
    if menu1 == 1:
        print(menu_ingreso)
        menu_ingreso1 = int(input("= "))
        if menu_ingreso1 == 1:
            print("welcome!!")
        elif menu_ingreso1 == 2:
            user = str(input("ingrese su nombre de usario: "))
            contraseña = str(input("ingrese su contraseña: ")).lower()
            from funciones_traines import validacion_contraseña_trainer
            hee = validacion_contraseña_trainer
            hee(contraseña)
        elif menu_ingreso1 == 3:
            import conrdi_funciones 
            contra = input("bienvenido cordinador, porfavor ingrese su contraseña: ")
            hh = conrdi_funciones.validar_contraseña
            hh(contra)
           

    elif menu1 == 2:
        print("*******************************************************")
        import funciones_registro
        funciones_registro.pedir_datos()
        print("registro")
    else:
        print("opcion invalida, Porfavor ingrese una opcion: ")
        print(menu_inicio)
        menu1 =int(input("= "))
        break




