

 

def rutas_cordi():
        while True:
               try:
                    menu_rutas = (
                        "1 ver rutas\n"
                        "2 subir campers a rutas\n"
                        "3 subir triners a rutas\n"
                        "oprima cualquier otro numero para volver al anterior menu....."
                    )
                    print("**********************************************************************")
                    print(menu_rutas)
                    submenu = input("Ingrese una opción: ")
                    if submenu == "1":
                     from funciones_cargar_guardar import mostrar_rutas
                     ruta= "rutas.json"
                     mostrar_rutas(ruta)
                    elif submenu == 2:
                        from practicas import cargar
                        datos = cargar
                        numero = int(input("ingrese documento usuario"))
                        if numero not in datos.get("ingresados", {}):
                            from funciones_cargar_guardar import mostrar_rutas
                            rutas = str(input("seleccione una ruta: "))
                            salon = str(input("seleccione un salon:"))
                        else:
                            print("usuario no existe...")
               except:
                   pass

                   