  #Codigo general
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
    3: {"nombre": "Guanacaste", "horario": "Abren a las 4 am, cierran a las 11 pm"},   #dicciionario con sus respectivas sedes, para la funcion cambiar de sede 
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
    modelo_nc2 = 2
    modelo_n3 = "rogue"
    modelo_nc3 = 0

    # Marca 3
    modelo_h1 = "santaFe"
    modelo_hc1 = 0
    modelo_h2 = "tucson"
    modelo_hc2 = 2
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


def gestion_inventario():
    print("Gestion de inventario")

    # Evitar objetos duplicados en las listas
    for marca in marcas:
        if marca not in marca_unique:
            marca_unique.append(marca)     

    while True:
        print("""
    (1) Agregar vehiculos
    (2) Inhabilitar vehiculo
    (3) Estado de vehiculos
    (4) Cambiar de sede
    (5) Salir
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
            print("Indique el carro que desea inhabilitar:")  
            for i in range(len(marcas)):
                print(i ,"-", marcas[i], modelos[i], years[i], cc[i], state[i])  #funcion de inabilithar vehiculo, esto para que los usuarios puedan inabilitarlo si asi lo desean 
            car_index = int(input())
            state[car_index] = "Inhabilitado"
            print("El carro ha sido inhabilitado correctamente.")
        elif gest_ans == 3:
            for i in range(len(marcas)):
                print(i ,"-",marcas[i],",", modelos[i],",", years[i],",",cc[i],",",state[i])
        elif gest_ans == 4:
            print("Seleccione la sede a la que desea cambiar:")
            for key, value in sedes_horarios.items():
                print(f"{key}. {value['nombre']} - Horario: {value['horario']}")
            sede_seleccionada = int(input("Ingrese el número correspondiente a la sede deseada: "))
            print(f"Usted ha seleccionado cambiar a la sede {sedes_horarios[sede_seleccionada]['nombre']}.")  #funcion cambiar sede activa
        elif gest_ans == 5:
            break
        else:
            print("Coloca una opcion valida")


def main_menu():
    while True:
        print("""
    (1) Visualizar inventario
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
            print("Reserva realizada correctamente")
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
    main_menu()



