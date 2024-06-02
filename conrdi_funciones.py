while True:
  menu = (
    "1 trainers\n"
    "2 campers\n"
    "3 rutas"
    
  )
  print(menu)
  menu = int(input("= "))
  
  menu_trainers = (
    "1 para agregar/eliminar trainers\n"
    "2 para cambiar informacion de trainer"

  )
  menu_campers = (
    "1 para calificar prueba de ingreso\n"
    "2 cambiar estado campers\n"
    "3 actualizar informacion"
  )
  menu_rutas = (
    "1 agregar rutas\n"
    "2 cambiar de ruta a los grupos"
  )
  if menu == 1: 
    print(menu_trainers)
  elif menu == 2:
    print(menu_campers)
  elif menu == 3:
    print(menu_rutas)