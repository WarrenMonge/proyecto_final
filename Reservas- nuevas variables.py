
marcas = ["toyota", "nissan", "subaru", "toyota", "ford"]
marca_unique = []
modelos = ["yaris", "altima", "wrx", "supra", "fiesta"]
modelo_unique = []
years = ["2012", "2008", "2010", "1990", "2005"]
year_unique = []
cc = ["1500cc", "2500cc", "2400cc", "3000cc", "2000cc"]
cc_unique = []
state = ["Disponible", "Disponible", "Disponible", "Disponible", "Disponible"]
price_ad = [500, 800, 1000, 2000, 800]
price_car = [5000, 8000, 15000, 50000, 10000]

marcas_modelos = {}
for marca, modelo, year, cc, estado, precio_adicional, precio_auto in zip(marcas, modelos, years, cc, state, price_ad, price_car):
    if marca not in marcas_modelos:
        marcas_modelos[marca] = []
        marca_unique.append(marca)
    marcas_modelos[marca].append({"modelo": modelo, "year": year, "cc": cc, "estado": estado, "precio_adicional": precio_adicional, "precio_auto": precio_auto})
    if modelo not in modelo_unique:
        modelo_unique.append(modelo)
    if year not in year_unique:
        year_unique.append(year)
    if cc not in cc_unique:
        cc_unique.append(cc)

sedes_horarios = {
    1: {"nombre": "San José", "horario": {"lunes": {"apertura": "00:00", "cierre": "23:59"}, "martes": {"apertura": "00:00", "cierre": "23:59"}, "miércoles": {"apertura": "00:00", "cierre": "23:59"}, "jueves": {"apertura": "00:00", "cierre": "23:59"}, "viernes": {"apertura": "00:00", "cierre": "23:59"}, "sábado": {"apertura": "00:00", "cierre": "23:59"}, "domingo": {"apertura": "00:00", "cierre": "23:59"}}},
    2: {"nombre": "Alajuela", "horario": {"lunes": {"apertura": "00:00", "cierre": "23:59"}, "martes": {"apertura": "00:00", "cierre": "23:59"}, "miércoles": {"apertura": "00:00", "cierre": "23:59"}, "jueves": {"apertura": "00:00", "cierre": "23:59"}, "viernes": {"apertura": "00:00", "cierre": "23:59"}, "sábado": {"apertura": "00:00", "cierre": "23:59"}, "domingo": {"apertura": "00:00", "cierre": "23:59"}}},
    3: {"nombre": "Guanacaste", "horario": {"lunes": {"apertura": "04:00", "cierre": "23:00"}, "martes": {"apertura": "04:00", "cierre": "23:00"}, "miércoles": {"apertura": "04:00", "cierre": "23:00"}, "jueves": {"apertura": "04:00", "cierre": "23:00"}, "viernes": {"apertura": "04:00", "cierre": "23:00"}, "sábado": {"apertura": "04:00", "cierre": "23:00"}, "domingo": {"apertura": "04:00", "cierre": "23:00"}}},
    4: {"nombre": "Limón", "horario": {"lunes": {"apertura": "06:00", "cierre": "22:00"}, "martes": {"apertura": "06:00", "cierre": "22:00"}, "miércoles": {"apertura": "06:00", "cierre": "22:00"}, "jueves": {"apertura": "06:00", "cierre": "22:00"}, "viernes": {"apertura": "06:00", "cierre": "22:00"}, "sábado": {"apertura": "06:00", "cierre": "22:00"}, "domingo": {"apertura": "06:00", "cierre": "22:00"}}},
    5: {"nombre": "Puntarenas", "horario": {"lunes": {"apertura": "05:00", "cierre": "22:00"}, "martes": {"apertura": "05:00", "cierre": "22:00"}, "miércoles": {"apertura": "05:00", "cierre": "22:00"}, "jueves": {"apertura": "05:00", "cierre": "22:00"}, "viernes": {"apertura": "05:00", "cierre": "22:00"}, "sábado": {"apertura": "05:00", "cierre": "22:00"}, "domingo": {"apertura": "05:00", "cierre": "22:00"}}},
    6: {"nombre": "Pérez Zeledón", "horario": {"lunes": {"apertura": "07:00", "cierre": "22:00"}, "martes": {"apertura": "07:00", "cierre": "22:00"}, "miércoles": {"apertura": "07:00", "cierre": "22:00"}, "jueves": {"apertura": "07:00", "cierre": "22:00"}, "viernes": {"apertura": "07:00", "cierre": "22:00"}, "sábado": {"apertura": "07:00", "cierre": "22:00"}, "domingo": {"apertura": "07:00", "cierre": "22:00"}}}
}

def imprimir_disponibilidad(marca):
    if marca in marcas_modelos:
        print(f"Disponibilidad de {marca}:")
        modelos = marcas_modelos[marca]
        for modelo_info in modelos:
            modelo = modelo_info["modelo"]
            estado = modelo_info["estado"]
            print(f"{marca}, {modelo}: Estado - {estado}")
    else:
        print("Marca no encontrada.")

def verificar_disponibilidad(marca_seleccionada, modelo_seleccionado):
    if marca_seleccionada in marcas_modelos:
        modelos = marcas_modelos[marca_seleccionada]
        for modelo_info in modelos:
            if modelo_info["modelo"] == modelo_seleccionado:
                estado = modelo_info["estado"]
                if estado == "Disponible":
                    print(f"El modelo {modelo_seleccionado} de la marca {marca_seleccionada} está disponible.")
                    return True
                else:
                    print(f"Disculpe, el modelo {modelo_seleccionado} de la marca {marca_seleccionada} no está disponible.")
                    return False
        print(f"Disculpe, el modelo {modelo_seleccionado} no está disponible para la marca {marca_seleccionada}.")
    else:
        print("Marca no encontrada.")
    return False

def verificar_horario(horario, sede_seleccionada):
    if sede_seleccionada in sedes_horarios:
        horario_sede = sedes_horarios[sede_seleccionada]["horario"]
        dia = horario["dia"]
        hora = horario["hora"]

        if dia.lower() in horario_sede:
            apertura = horario_sede[dia.lower()]["apertura"]
            cierre = horario_sede[dia.lower()]["cierre"]
            if apertura <= hora <= cierre:
                return True, None
            else:
                return False, f"Disculpe, la hora especificada de {horario['tipo']} no es permitida en la sede de {sedes_horarios[sede_seleccionada]['nombre']}. El horario de {dia.capitalize()} es de {apertura} a {cierre}."
        else:
            return False, f"Disculpe, la sede de {sedes_horarios[sede_seleccionada]['nombre']} no está abierta el {dia.capitalize()}."
    else:
        return False, "Sede no encontrada."

def guardar_reserva(marca_seleccionada, modelo_seleccionado, datos_cliente):
    with open("reservas.txt", "a") as archivo:
        archivo.write(f"Marca: {marca_seleccionada}, Modelo: {modelo_seleccionado}\n")
        archivo.write("Datos del cliente:\n")
        for key, value in datos_cliente.items():
            archivo.write(f"{key}: {value}\n")
        archivo.write("\n")

def visualizar_reservas():
    try:
        with open("reservas.txt", "r") as archivo:
            reservas = archivo.read()
            print("Reservas realizadas:\n")
            print(reservas)
    except FileNotFoundError:
        print("No hay reservas realizadas.")

def hacer_reserva():
    marca_seleccionada = input("Ingrese la marca del vehículo: ").lower()
    if marca_seleccionada in marcas_modelos:
        imprimir_disponibilidad(marca_seleccionada)
        modelo_seleccionado = input("Ingrese el modelo del vehículo: ").lower()
        if verificar_disponibilidad(marca_seleccionada, modelo_seleccionado):
            datos_cliente = {}
            datos_cliente["Nombre"] = input("Ingrese su nombre: ")
            datos_cliente["Teléfono"] = input("Ingrese su número de teléfono: ")
            guardar_reserva(marca_seleccionada, modelo_seleccionado, datos_cliente)
        else:
            print("No se pudo realizar la reserva.")
    else:
        print("Marca no encontrada.")

def mostrar_menu_horario():
    print("Seleccione la marca y modelo de vehículo que desea rentar:")
    for marca, modelos in marcas_modelos.items():
        print(f"{marca}: {', '.join([modelo_info['modelo'] for modelo_info in modelos])}")

    marca_seleccionada = input("Ingrese la marca del vehículo: ").lower()
    if marca_seleccionada in marcas_modelos:
        modelo_seleccionado = input("Ingrese el modelo de vehículo que desea rentar: ").lower()
        if modelo_seleccionado in [modelo_info['modelo'] for modelo_info in marcas_modelos[marca_seleccionada]]:
            print(f"Ha seleccionado {marca_seleccionada} {modelo_seleccionado}.")

    print("1 - San José, horario 24 horas, los 7 días de la semana")
    print("2 - Alajuela, horario 24 horas, los 7 días de la semana")
    print("3 - Guanacaste, horario: Abren a las 4 am, cierran a las 11 pm")
    print("4 - Limón, horario: Abren a las 6 am, cierran a las 10 pm")
    print("5 - Puntarenas, horario: Abren a las 5 am, cierran a las 10 pm")
    print("6 - Pérez Zeledón, horario: Abren a las 7 am, cierran a las 10 pm")
    sede_seleccionada = int(input("Ingrese el número de la sede: "))
    print("Por favor, seleccione el día y la hora para el retiro y entrega del vehículo:")
    dia_retiro = input("Día de retiro: ").lower()
    hora_retiro = input("Hora de retiro (HH:MM): ")
    dia_entrega = input("Día de entrega: ").lower()
    hora_entrega = input("Hora de entrega (HH:MM): ")

    retiro_valido, retiro_error = verificar_horario({"dia": dia_retiro, "hora": hora_retiro, "tipo": "retiro"}, sede_seleccionada)
    entrega_valida, entrega_error = verificar_horario({"dia": dia_entrega, "hora": hora_entrega, "tipo": "entrega"}, sede_seleccionada)

    if not retiro_valido:
        print(retiro_error)
        return
    elif not entrega_valida:
        print(entrega_error)
        return
    else:
        print("Horarios de retiro y entrega válidos. Proceda con la reserva.")

def menu_principal():
    while True:
        print("\n----- MENÚ PRINCIPAL -----")
        print("1. Hacer una reserva")
        print("2. Mostrar disponibilidad de vehículos")
        print("3. Ver reservas realizadas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hacer_reserva()
        elif opcion == "2":
            mostrar_menu_horario()
        elif opcion == "3":
            visualizar_reservas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu_principal()
