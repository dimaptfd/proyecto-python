








def pedir_datos():
    print("**********************************************************************")
    print("para realizar la inscripcion, llene el siguiente formulario\n(tome en cuenta que su edad debe ser mayor o igual de 17 y menor que 30 años):  ")
    edad = int(input("edad: "))
    if edad >= 18 and edad < 30:
        documento = int(input("documento: "))
        nombres = str(input("nombres: ")).title()
        apellidos = str(input("apellidos: ")).title()
        direccion = input("direccion: ")
        num_tel = int(input("numero de celular / telefono: "))
        
    elif edad == 17:
        documento = int(input("documento: "))
        nombres = str(input("nombres: ")).title()
        apellidos = str(input("apellidos: ")).title()
        direccion = int(input("direccion: "))
        num_tel = int(input("numero de celular / telefono: "))
        
        print("al ser menor de edad, estamos obligados a pedir los datos de algun acudiente: ")
        acudiente_nombre = str(input("acudiente; nombres y apellidos: ")).title()
        acudiente_= str(input("acudiente; nombres y apellidos: ")).title()
        acudiente = str(input("acudiente; nombres y apellidos: ")).title()
        num_tel = int(input("numero / telefono, del acudiente: "))
    else: 
        print("lo sentimos, estas fuera del rango de edad para la inscripcion")
        

    

        





  
    
    
        