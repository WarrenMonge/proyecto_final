# VARIABLES
marcas = ["toyota", "nissan", "subaru","toyota","ford"]
marca_unique = []
modelos = ["yaris","altima","wrx","supra","fiesta"]
modelo_unique = []
years = ["2012","2008","2010","1990","2005"]
year_unique = []
cc = ["1500cc","2500cc","2400cc","3000cc","2000cc"]
cc_unique = []
state = ["Disponible","Disponible","Disponible","Disponible","Disponible"]
price_ad = [500,800,1000,2000,800]
price_car = [5000,8000,15000,50000,10000]

sedes_horarios = {
    1: {"nombre": "San José", "horario": "24 horas, los 7 días de la semana"},
    2: {"nombre": "Alajuela", "horario": "24 horas, los 7 días de la semana"},
    3: {"nombre": "Guanacaste", "horario": "Abren a las 4 am, cierran a las 11 pm"},   # Diccionario que contiene la información sobre las sedes y los horarios en los que operan
    4: {"nombre": "Limón", "horario": "Abren a las 6 am, cierran a las 10 pm"},
    5: {"nombre": "Puntarenas", "horario": "Abren a las 5 am, cierran a las 10 pm"},
    6: {"nombre": "Pérez Zeledón", "horario": "Abren a las 7 am, cierran a las 10 pm"}
}

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
    for marca in marcas:
        if marca not in marca_unique:
            marca_unique.append(marca)  
    print("Ingrese la marca del vehículo: ")
    for i in range(len(marca_unique)):
        print(i ,"-", marca_unique[i])
    marca_seleccionada = int(input())
    if marcas[marca_seleccionada] in marcas_modelos:
        imprimir_disponibilidad(marcas[marca_seleccionada])
        modelo_seleccionado = input("Ingrese el modelo del vehículo: ").lower()
        if verificar_disponibilidad(marcas[marca_seleccionada], modelo_seleccionado):
            datos_cliente = {}
            datos_cliente["Nombre"] = input("Ingrese su nombre: ")
            datos_cliente["Teléfono"] = input("Ingrese su número de teléfono: ")
            guardar_reserva(marcas[marca_seleccionada], modelo_seleccionado, datos_cliente)
        else:
            print("No se pudo realizar la reserva.")
    else:
        print("No disponibilidad.")

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

def visualizar_carros():
    # Vizualizar vehiculos
    for marca in marcas:
        if marca not in marca_unique:
            marca_unique.append(marca)     
    print("Indique la marca del vehiculo que quiera visualizar:")  
    for i in range(len(marca_unique)):
        print(i ,"-", marca_unique[i]) 
    marca_search = int(input())
    print()
    for x in range(len(modelos)):
        if marca_unique[marca_search] == marcas[x]:
            print(x ,"-", modelos[x],",", years[x],",",cc[x],",",state[x])

#Ingreso como invitado

def menu_opciones_invitado():
    
    print("Iniciaste sesion correctamente como invitado")
    print("Bienvenido Usuario invitado" )
    while True:
        print("""
Que te gustaria hacer?             

    (1) Visualizar carros
    (2) Salir
                            """)
        menu_login = int(input("Ingrese su opcion: "))
        if menu_login == 1:
            visualizar_carros()
        elif menu_login ==2:
            print("Muchas gracias, por elegirnos")
        break            

# Creacion de ingreso como usuario registrado
def register():
    db = open("login.txt", "r")
    user = input("Crear usuario: ") 
    password = input("Crear contraseña: ")
    password1 = input("Confirmar contraseña: ")

    u = []
    p = []                                      # Crea diccionarios para el usuario y la contrasena
    for i in db:
        a,b = i.split(",")                     # se recorre todos los datos del documento de texto para
        b = b.strip()                           # Validar los usuarios que estan registrados para que no se logre repetir el user
        u.append(a)                             
        p.append(b)
    data = dict(zip(u,p))                       # {'Wawa': '0201', 'Warren': '2022'} Ejemplo de como se recorre, gracias a los diccionarios

    if password != password1:
        print("La contraseñas no son iguales!!")
        register()
    elif user in u:
        print("El usuario ya existe!!")
        register()  

    else:
        db = open("login.txt", "a")
        db.write(user + ", " + password + "\n")
        print("Se registro con exito!!")

def gestion_inventario():
    print("Gestion de inventario")

    # Evitar objetos duplicados en las listas
    for marca in marcas:
        if marca not in marca_unique:
            marca_unique.append(marca)     

    while True:
        print("""
    (1) Agregar vehiculos
    (2) Inhabilite vehiculos
    (3) Estado de vehiculos
    (4) Salir
        """)
        gest_ans = int(input("Ingrese su opcion: "))
        if gest_ans == 1:
            marcas.append(input ("Ingrese la marca del vehiculo: "))
            modelos.append(input("Ingrese el modelo del vehiculo: "))
            years.append(input("Ingrese el año del vehiculo: "))
            cc.append(input("Ingrese el cilindraje del vehiculo: "))
            price_ad.append(input("Ingrese el precio de alquiler por dia: "))
            price_car.append(input("Ingrese el precio del vehiculo: "))
            state.append("Disponible")

        elif gest_ans == 2:
            print("Indique la marca del vehiculo que quiera inhabilitar:")  
            for i in range(len(marca_unique)):
                print(i ,"-", marca_unique[i]) 
            marca_search = int(input())
            print("Cual auto desea inhabilitar:")
            for x in range(len(modelos)):
                if marca_unique[marca_search] == marcas[x]:
                    print(x ,"-", modelos[x],",", years[x],",",cc[x])
            car_search = int(input())
            state[car_search] = "Inhabilitado"
        elif gest_ans == 3:
            for y in range(len(modelos)):
                print(y ,"-",marcas[y],",", modelos[y],",", years[y],",",cc[y],",",state[y])
        elif gest_ans == 4:
            break
        else:
            print("Coloca una opcion valida")

def reservacion():
    print("Reservacion de Autos")
    while True:
        print("""
    (1) Reservar vehiculo
    (2) Salir
        """)

def ingreso():
    db = open("login.txt", "r")
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if not len(user or password) < 1:
        u = []
        p = []                                      
        for i in db:
            a,b = i.split(",")                     
            b = b.strip()                           
            u.append(a)                             
            p.append(b)
        data = dict(zip(u,p))

        try:
            if data[user]:
                try:
                    if password == data[user]:
                        print(f"Ingresaste corectamente {user}")
                        main_menu()
                    else:
                        print("Usuario o contrasena incorrecto!!")
                except KeyError:
                    print("Contrasena incorrecta del usuario")
        except KeyError:
            print("El usuario o contrasena no existe!!")
    else:
        print("Ingrese sus datos!!")

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
        opc = input("""
Bienvenido a Fiderents
                
    (1) Iniciar Sesion
    (2) Registrarte
    (3) Ingreso invitado
    (4) Salir                   
                    
Ingrese tu opcion:""")
        if opc == "1":
            ingreso()
        elif opc ==  "2":
            register()
        elif opc == "3":
            menu_opciones_invitado()
        elif opc ==  "4":
            print("Muchas gracias, por elegirnos")
            break            
        else:
            print("Ingrese una de las 4 opciones!!")

def main_menu():
    while True:
        print("""
    (1) Visualizar vehiculos
    (2) Realizar reserva
    (3) Entrega de vehiculo
    (4) Gestion de inventario
    (5) Cambiar de sede
    (6) Salir
        """)
        ans = int(input("Ingrese su opcion: "))
        if ans == 1:
            visualizar_carros()
        elif ans == 2:
            hacer_reserva()
        elif ans == 3:
            print("Entrega realizada correctamente")
        elif ans == 4:
            gestion_inventario()
        elif ans == 5:
            print("Seleccione la sede a la que desea cambiar:")
            for key, value in sedes_horarios.items():
                print(f"{key}. {value['nombre']} - Horario: {value['horario']}")
            sede_seleccionada = int(input("Ingrese el número correspondiente a la sede deseada: "))
            print(f"Usted ha seleccionado cambiar a la sede {sedes_horarios[sede_seleccionada]['nombre']}.")
        elif ans == 6:
            break
        else:
            print("Coloca una opcion valida")

if __name__ == "__main__":
    menu()


