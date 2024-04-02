#CAMBIO DE SEDE 
sedes_horarios = {
    1: {"nombre": "San José", "horario": "24 horas, los 7 días de la semana"},
    2: {"nombre": "Alajuela", "horario": "24 horas, los 7 días de la semana"},
    3: {"nombre": "Guanacaste", "horario": "Abren a las 4 am, cierran a las 11 pm"},   # Diccionario que contiene la información sobre las sedes y los horarios en los que operan
    4: {"nombre": "Limón", "horario": "Abren a las 6 am, cierran a las 10 pm"},
    5: {"nombre": "Puntarenas", "horario": "Abren a las 5 am, cierran a las 10 pm"},
    6: {"nombre": "Pérez Zeledón", "horario": "Abren a las 7 am, cierran a las 10 pm"}
}

def cambiar_sede(sede_actual):   # Llama a la función cambiar_sede para cambiar la sede actual, la cual se basa en la informacion del diccionario para poder ejecutar dicha sede.
    print("Sedes disponibles:")
    for num, sede_info in sedes_horarios.items():
        print(f"{num}. {sede_info['nombre']}")

    num_sede = int(input("Ingrese el número de la nueva sede: "))

    if num_sede in sedes_horarios:
        nueva_sede = sedes_horarios[num_sede]["nombre"]
        print(f"Sede cambiada a {nueva_sede} correctamente.")
        return nueva_sede
    else:
        print("El número de sede ingresado no es válido.")
        return sede_actual

def menu():
    sede_actual = "San José"  #funcion para saber en cual sede se encuentran esto con el fin de hacer que el usuario tenga mas visulacion de la informacion 
    while True:
        opc = input
        print(sede_actual)

menu()  # Llama a la función menu para iniciar la ejecución del programa
