

import funciones_registro


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

        break
    elif menu1 == 2:
        funciones_registro.pedir_datos()
        print("registro")
    else:
        print("opcion invalida, Porfavor ingrese una opcion: ")
        print(menu_inicio)
        menu1 =int(input("= "))
        break




