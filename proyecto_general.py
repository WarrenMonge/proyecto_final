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
price_ad = []
price_car = []

sedes_horarios = {
    1: {"nombre": "San José", "horario": "24 horas, los 7 días de la semana"},
    2: {"nombre": "Alajuela", "horario": "24 horas, los 7 días de la semana"},
    3: {"nombre": "Guanacaste", "horario": "Abren a las 4 am, cierran a las 11 pm"},   # Diccionario que contiene la información sobre las sedes y los horarios en los que operan
    4: {"nombre": "Limón", "horario": "Abren a las 6 am, cierran a las 10 pm"},
    5: {"nombre": "Puntarenas", "horario": "Abren a las 5 am, cierran a las 10 pm"},
    6: {"nombre": "Pérez Zeledón", "horario": "Abren a las 7 am, cierran a las 10 pm"}
}


# DATOS COLOCADOS ACA SOLAMENTE SON PRUEBAS
def visualizar_carros():
    # Proyecto final
    # Vizualizar vehiculos
    marca1 = "toyota"          # Las marcas y modelos son como ejemplo
    marca2 = "nissan"
    marca3 = "hyundai"

    # Marca 1
    modelo_t1 = "yaris"
    modelo_tc1 = 1
    modelo_t2 = "corolla"
    modelo_tc2 = 0
    modelo_t3 = "tacoma"
    modelo_tc3 = 0

    # Marca 2
    modelo_n1 = "kicks"
    modelo_nc1 = 0
    modelo_n2 = "murano"
    modelo_nc2 = 0
    modelo_n3 = "rogue"
    modelo_nc3 = 0

    # Marca 3
    modelo_h1 = "santaFe"
    modelo_hc1 = 0
    modelo_h2 = "tucson"
    modelo_hc2 = 0
    modelo_h3 = "venue"
    modelo_hc3 = 0

    marca = input("Ingrese la marca del vehiculo que desea ver:")

    if marca == marca1:
        print("Disponibilidad de", marca1)
        print(marca1, modelo_t1, modelo_tc1)
        print(marca1, modelo_t2, modelo_tc2)      # en inventario deberia ir cantidad de marcas y cantidad de cada tipo de modelo o se podria establecer una cantidad de modelos en variables
        print(marca1, modelo_t3, modelo_tc3)
    
    elif marca == marca2:
        print("Disponibilidad de", marca2)
        print(marca2, modelo_n1, modelo_nc1)
        print(marca2, modelo_n2, modelo_nc2)
        print(marca2, modelo_n3, modelo_nc3)
    
    elif marca == marca3:
        print("Disponibilidad de", marca3)
        print(marca3, modelo_h1, modelo_hc1)
        print(marca3, modelo_h2, modelo_hc2)
        print(marca3, modelo_h3, modelo_hc3)

    selec_marca = input("Digite el nombre de la marca que desea retirar:")
    if selec_marca == "toyota":
        selec_model = input("Ingrese el nombre del modelo que desea retirar:")
        if selec_model == modelo_t1 and modelo_tc1 == 0:
            print("Disculpe el modelo", modelo_t1, "no está disponible")
        elif selec_model == modelo_t1 and modelo_tc1 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_tc1 -= 1
            print("reservo,", marca1, selec_model)
        elif selec_model == modelo_t2 and modelo_tc2 == 0:
            print("Disculpe el modelo", modelo_t2, "no está disponible")
        elif selec_model == modelo_t2 and modelo_tc2 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_tc2 -= 1
            print("reservó,", marca1, selec_model)
        elif selec_model == modelo_t3 and modelo_tc3 == 0:
            print("Disculpe el modelo", modelo_t3, "no está disponible")
        elif selec_model == modelo_t3 and modelo_tc3 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_tc3 -= 1
            print("reservó,", marca1, selec_model)
        
    elif selec_marca == "nissan":
        selec_model = input("Ingrese el nombre del modelo que desea retirar:")
        if selec_model == modelo_n1 and modelo_nc1 == 0:
            print("Disculpe el modelo", modelo_n1, "no está disponible")
        elif selec_model == modelo_n1 and modelo_nc1 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_nc1 -= 1
            print("reservó,", marca2, selec_model)
        elif selec_model == modelo_n2 and modelo_nc2 == 0:
            print("Disculpe el modelo", modelo_n2, "no está disponible")
        elif selec_model == modelo_n2 and modelo_nc2 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_nc2 -= 1
            print("reservó,", marca2, selec_model)
        elif selec_model == modelo_n3 and modelo_nc3 == 0:
            print("Disculpe el modelo", modelo_n3, "no está disponible")
        elif selec_model == modelo_n3 and modelo_nc3 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_nc3 -= 1
            print("reservó,", marca2, selec_model)
        
    elif selec_marca == "hyundai":
        selec_model = input("Ingrese el nombre del modelo que desea retirar:")
        if selec_model == modelo_h1 and modelo_hc1 == 0:
            print("Disculpe el modelo", modelo_h1, "no está disponible")
        elif selec_model == modelo_h1 and modelo_hc1 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_hc1 -= 1
            print("reservó,", marca3, selec_model)
        elif selec_model == modelo_h2 and modelo_hc2 == 0:
            print("Disculpe el modelo", modelo_h2, "no está disponible")
        elif selec_model == modelo_h2 and modelo_hc2 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_hc2 -= 1
            print("reservó,", marca3, selec_model)
        elif selec_model == modelo_h3 and modelo_hc3 == 0:
            print("Disculpe el modelo", modelo_h3, "no está disponible")
        elif selec_model == modelo_h3 and modelo_hc3 > 0:
            print("El modelo está disponible")
            model_reserva = selec_model
            modelo_hc3 -= 1
            print("reservó,", marca3, selec_model)

#Vizualizar vehiculos y realizar reservas.
def realizar_reserva():
    qq
    marca1=str("toyota")          #Las marcas y modelos son como ejemplo
    marca2=str("nissan")
    marca3=str("hyundai")

    # Diccionario de marcas y modelos
    marcas_modelos = {
        "toyota": {
            "yaris": 2,
            "corolla": 2,
            "tacoma": 0
        },
        "nissan": {
            "kicks": 0,
            "murano": 2,
            "rogue": 0
        },
        "hyundai": {
            "santaFe": 0,
            "tucson": 2,
            "venue": 0
        }
    }
            

    def imprimir_disponibilidad(marca):
        if marca in marcas_modelos:
            print(f"Disponibilidad de {marca}:")
            modelos = marcas_modelos[marca]
            for modelo, cantidad in modelos.items():
                print(f"{marca}, {modelo}: {cantidad} unidades disponibles")
        else:
            print("Marca no encontrada.")

    def verificar_disponibilidad(marcas_modelos, marca_seleccionada, modelo_seleccionado):
        if marca_seleccionada in marcas_modelos:
            modelos = marcas_modelos[marca_seleccionada]
            if modelo_seleccionado in modelos:
                cantidad_disponible = modelos[modelo_seleccionado]
                if cantidad_disponible > 0:
                    print(f"El modelo {modelo_seleccionado} está disponible.")
                    return True
                else:
                    print(f"Disculpe, el modelo {modelo_seleccionado} no está disponible.")
            else:
                print(f"Disculpe, el modelo {modelo_seleccionado} no está disponible para la marca {marca_seleccionada}.")
        else:
            print("Marca no encontrada  .")
        return False

    
    sedes_horarios = {
        1: {
            "nombre": "San José",
            "horario": {
                "lunes": {"apertura": "00:00", "cierre": "23:59"},
                "martes": {"apertura": "00:00", "cierre": "23:59"},
                "miércoles": {"apertura": "00:00", "cierre": "23:59"},
                "jueves": {"apertura": "00:00", "cierre": "23:59"},
                "viernes": {"apertura": "00:00", "cierre": "23:59"},
                "sábado": {"apertura": "00:00", "cierre": "23:59"},
                "domingo": {"apertura": "00:00", "cierre": "23:59"}
            }
        },
        2: {
            "nombre": "Alajuela",
            "horario": {
                "lunes": {"apertura": "00:00", "cierre": "23:59"},
                "martes": {"apertura": "00:00", "cierre": "23:59"},
                "miércoles": {"apertura": "00:00", "cierre": "23:59"},
                "jueves": {"apertura": "00:00", "cierre": "23:59"},
                "viernes": {"apertura": "00:00", "cierre": "23:59"},
                "sábado": {"apertura": "00:00", "cierre": "23:59"},
                "domingo": {"apertura": "00:00", "cierre": "23:59"}
            }
        },
        3: {
            "nombre": "Guanacaste",
            "horario": {
                "lunes": {"apertura": "04:00", "cierre": "23:00"},
                "martes": {"apertura": "04:00", "cierre": "23:00"},
                "miércoles": {"apertura": "04:00", "cierre": "23:00"},
                "jueves": {"apertura": "04:00", "cierre": "23:00"},
                "viernes": {"apertura": "04:00", "cierre": "23:00"},
                "sábado": {"apertura": "04:00", "cierre": "23:00"},
                "domingo": {"apertura": "04:00", "cierre": "23:00"}
            }
        },
        4: {
            "nombre": "Limón",
            "horario": {
                "lunes": {"apertura": "06:00", "cierre": "22:00"},
                "martes": {"apertura": "06:00", "cierre": "22:00"},
                "miércoles": {"apertura": "06:00", "cierre": "22:00"},
                "jueves": {"apertura": "06:00", "cierre": "22:00"},
                "viernes": {"apertura": "06:00", "cierre": "22:00"},
                "sábado": {"apertura": "06:00", "cierre": "22:00"},
                "domingo": {"apertura": "06:00", "cierre": "22:00"}
            }
        },
        5: {
            "nombre": "Puntarenas",
            "horario": {
                "lunes": {"apertura": "05:00", "cierre": "22:00"},
                "martes": {"apertura": "05:00", "cierre": "22:00"},
                "miércoles": {"apertura": "05:00", "cierre": "22:00"},
                "jueves": {"apertura": "05:00", "cierre": "22:00"},
                "viernes": {"apertura": "05:00", "cierre": "22:00"},
                "sábado": {"apertura": "05:00", "cierre": "22:00"},
                "domingo": {"apertura": "05:00", "cierre": "22:00"}
            }
        },
        6: {
            "nombre": "Pérez Zeledón",
            "horario": {
                "lunes": {"apertura": "07:00", "cierre": "22:00"},
                "martes": {"apertura": "07:00", "cierre": "22:00"},
                "miércoles": {"apertura": "07:00", "cierre": "22:00"},
                "jueves": {"apertura": "07:00", "cierre": "22:00"},
                "viernes": {"apertura": "07:00", "cierre": "22:00"},
                "sábado": {"apertura": "07:00", "cierre": "22:00"},
                "domingo": {"apertura": "07:00", "cierre": "22:00"}
            }
        }
    }

    def verificar_horario(horario, sede, sedes_horarios):
        horario_sede = sedes_horarios[sede]["horario"]
        dia = horario["día"]
        hora = horario["hora"]
    
        if dia.lower() in horario_sede:
            apertura = horario_sede[dia.lower()]["apertura"]
            cierre = horario_sede[dia.lower()]["cierre"]
            if apertura <= hora <= cierre:
                return True, None
            else:
                return False, f"Disculpe, la hora especificada de {horario['tipo']} no es permitida en la sede de {sedes_horarios[sede]['nombre']}. El horario de {dia.capitalize()} es de {apertura} a {cierre}."
        else:
            return False, f"Disculpe, la sede de {sedes_horarios[sede]['nombre']} no está abierta el {dia.capitalize()}."

    def mostrar_menu_horario(marcas_modelos, sedes_horarios):
        print("Seleccione la marca y modelo de vehículo que desea rentar:")
        for marca, modelos in marcas_modelos.items():
            print(f"{marca}: {', '.join(modelos.keys())}")

        marca_seleccionada = input("Ingrese la marca del vehículo: ")
        if marca_seleccionada in marcas_modelos:
            modelo_seleccionado = input("Ingrese el modelo de vehículo que desea rentar: ")
            if modelo_seleccionado in marcas_modelos[marca_seleccionada]:
                print(f"Ha seleccionado {marca_seleccionada} {modelo_seleccionado}.")

        print("1 - San José, horario 24 horas, los 7 días de la semana")
        print("2 - Alajuela, horario 24 horas, los 7 días de la semana")
        print("3 - Guanacaste, horario:Abren a las 4 am, cierran a las 11 pm")
        print("4 - Limón, horario:Abren a las 6 am, cierran a las 10 pm")
        print("5 - Puntarenas, horario: Abren a las 5 am, cierran a las 10 pm")
        print("6 - Pérez Zeledón, horario: Abren a las 7 am, cierran a las 10 pm")
        sede_seleccionada = int(input("Ingrese el número de la sede: "))
        print("Por favor, seleccione el día y la hora para el retiro y entrega del vehículo:")
        dia_retiro = input("Día de retiro: ").lower()
        hora_retiro = input("Hora de retiro (HH:MM): ")
        dia_entrega = input("Día de entrega: ").lower()
        hora_entrega = input("Hora de entrega (HH:MM): ")

        retiro_valido, retiro_error = verificar_horario({"día": dia_retiro, "hora": hora_retiro, "tipo": "retiro"}, sede_seleccionada, sedes_horarios)
        entrega_valida, entrega_error = verificar_horario({"día": dia_entrega, "hora": hora_entrega, "tipo": "entrega"}, sede_seleccionada, sedes_horarios)

        if not retiro_valido:
            print(retiro_error)
            return
        elif not entrega_valida:
            print(entrega_error)
            return
        else:
            print("Horarios de retiro y entrega válidos. Proceda con la reserva.")
    
    mostrar_menu_horario(marcas_modelos, sedes_horarios)

    marca_seleccionada = input("Ingrese la marca del vehículo: ")
    imprimir_disponibilidad(marca_seleccionada)
    marca_seleccionada = input("Ingrese la marca del vehículo: ")
    modelo_seleccionado = input("Ingrese el modelo del vehículo: ")
    if verificar_disponibilidad(marcas_modelos, marca_seleccionada, modelo_seleccionado):
        marcas_modelos[marca_seleccionada][modelo_seleccionado] -= 1
        print("Reserva realizada con éxito.")
    else:
        print("No se pudo realizar la reserva.")
  
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

def inv_user():
    menu_opciones_invitado()

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
                        print("Iniciaste sesion correctamente")
                        print("Bienvenido, ", user)
                        while True:
                            print("""
Que te gustaria hacer?             

    (1) Visualizar carros
    (2) Gestion de inventario
    (3) Crear reservacion
    (4) Realizar reserva
    (5) Cambiar de Sede
    (6) Salir
                            """)
                            menu_login = int(input("Ingrese su opcion: "))
                            if menu_login == 1:
                                visualizar_carros()
                            elif menu_login ==2:
                                gestion_inventario()
                            elif menu_login ==3:
                                reservacion()
                            elif menu_login == 4:
                                realizar_reserva()
                            elif menu_login == 5:
                                sede_actual = cambiar_sede(sede_actual)                               
                            elif menu_login == 6:
                                print("Muchas gracias, por elegirnos")
                                break
                    else:
                        print("Usuario o contrase;a incorrecto!!")
                except:
                    print("Contrasena incorrecta del usuario")
            else:
                print("El usuario o contrasena no existe!!")
        except:
            print("El usuario o contrasena no existe!!!")
    else:
        print("Ingrese su datos!!")


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
            inv_user()
        elif opc ==  "4":
            print("Muchas gracias, por elegirnos")
            break            
        else:
            print("Ingrese una de las 4 opciones!!")

menu()


