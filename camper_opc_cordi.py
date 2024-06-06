from funciones_cargar_guardar import cargar, guardar
def usuarios_campers():
        menu_campers = (
                            "1 para calificar prueba de ingreso: \n"
                            "2 cambiar estado campers: \n"
                            "3 ver campers: \n "
                            "oprima cualquier numero para salir..."
                        )
        while True:
            print("**********************************************************************")
            print(menu_campers)
            submenu1 = int(input("Ingrese una opción: "))
            if submenu1 == 1:
                yuca = cargar()
                docu_buscar = int(input("numero usuario:  "))
                print("**********************************************************")
                if str(docu_buscar) in yuca["ingresados"]: 
                    nota1 = int(input("ingrese nota del prueba 1: "))
                    nota2 = int(input("ingrese nota del prueba 2: "))
                    nota = (nota1 + nota2)/2
                    if 59 <= int(nota) and int(nota) <= 100:
                        
                        yuca["inscritos"][str(docu_buscar)]["estados"] = "aprobado"
                        guardar(yuca)
                        if ["inscritos"][str(docu_buscar)]["estados"] == "aprobado":
                            yuca["aprobados"][str(docu_buscar)]["riesgo"] = False
                            guardar(yuca)
                                       
                            print("**************************************************")
                            print("Estado cambiado con éxito")
                    else:
                        yuca["ingresados"][str(docu_buscar)]["estados"] = "reprobado"
                        guardar(yuca)
                else:
                    print("Usuario no encontrado")
            elif submenu1 == 2:
                pass
            elif submenu1 == 3:
                print("**********************************************************************")
                from funciones_cargar_guardar import mostrar_informacion
                ruta = 'usuarios.json'
                mostrar_informacion(ruta)
            else:
                break
                

        
                    