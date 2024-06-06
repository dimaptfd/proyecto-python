import practicas as hola

def pedir_datos():
    rhlm = hola.cargar()
    usuarios = {}
    print("**********************************************************************")
    print("para realizar la inscripcion, llene el siguiente formulario\n(tome en cuenta que su edad debe ser mayor o igual de 17 y menor que 30 años):  ")
    edad = int(input("edad: "))
    
    if edad >= 17 and edad < 30:  
        usuarios["nombres"] = str(input("nombres: ")).title()
        usuarios["apellidos"] = str(input("apellidos: ")).title()
        docu = int(input("documento: "))
        nombre = usuarios["nombres"] + " " + usuarios["apellidos"]
        if hola.registrar_usuario(nombre, docu, rhlm):
            print("El usuario ya existe...")
            return
        
        
        usuarios["direccion"] = input("direccion: ")
        usuarios["num_tel"] = int(input("numero de celular / telefono: "))
        
        if edad == 17:
            print("al ser menor de edad, estamos obligados a pedir los datos de algun acudiente: ")
            usuarios["acudiente_nombre"] = str(input("acudiente; nombres y apellidos: ")).title()
            usuarios["acudiente documento"] = int(input("acudiente; documento: "))
            usuarios["parentesco acudiente"] = str(input("parentesco: "))
            usuarios["num_tel acudiente"] = int(input("numero / telefono, del acudiente: "))
        
        usuarios["estados"] ="en proceso de inscripcion"      
        rhlm["ingresados"][docu] = usuarios
        hola.guardar(rhlm)
        print("Datos guardados correctamente.")
    else: 
        print("lo sentimos, estas fuera del rango de edad para la inscripcion")
        import menu_pricipal
        return menu_pricipal         
