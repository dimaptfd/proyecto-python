

from funciones_cargar_guardar import cargar_y_guardar


def pedir_datos():
    
    usuarios = {}
    print("**********************************************************************")
    print("para realizar la inscripcion, llene el siguiente formulario\n(tome en cuenta que su edad debe ser mayor o igual de 17 y menor que 30 años):  ")
    edad = int(input("edad: "))
    if edad >= 18 and edad < 30:  
        
        usuarios["nombres"] = str(input("nombres: ")).title()
        usuarios["apellidos"] = str(input("apellidos: ")).title()
        docu = usuarios["documento"] = int(input("documento: "))
        usuarios["direccion"] = input("direccion: ")
        usuarios["num_tel"] = int(input("numero de celular / telefono: "))
        estados ="en proceso de inscripcion"      
        usuarios["estado":estados] 
        campers = {docu:usuarios}
        cargar_y_guardar(campers)
    elif edad == 17:
        
        usuarios["nombres"] = str(input("nombres: ")).title()
        usuarios["apellidos"] = str(input("apellidos: ")).title()
        usuarios["direccion"] = input("direccion: ")
        usuarios["num_tel"] = int(input("numero de celular / telefono: "))
        docu = usuarios["documento"] = int(input("documento: "))
        print("al ser menor de edad, estamos obligados a pedir los datos de algun acudiente: ")
        usuarios["acudiente_nombre"] = str(input("acudiente; nombres y apellidos: ")).title()
        usuarios["acudiente documento"] = int(input("acudiente; documento: "))
        usuarios["parentesco acudiente"] = str(input("parentesco: "))
        usuarios["num_tel acudiente"] = int(input("numero / telefono, del acudiente: "))
        estados ="en proceso de inscripcion"      
        usuarios["estado":estados] 
        campers = {docu:usuarios}
        cargar_y_guardar(campers)
        
    else: 
        print("lo sentimos, estas fuera del rango de edad para la inscripcion")
            
