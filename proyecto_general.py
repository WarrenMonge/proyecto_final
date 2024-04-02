#VARIABLES
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
    #DATOS COLOCADOS ACA SOLAMENTE SON PRUEBAS
def visualizar_carros():
    #Proyecto final
#vizualizar vehiculos

    marca1=str("toyota")          #Las marcas y modelos son como ejemplo
    marca2=str("nissan")
    marca3=str("hyundai")

    #Marca 1
    modelo_t1=str("yaris")          
    modelo_tc1=1
    modelo_t2=str("corolla")
    modelo_tc2=0
    modelo_t3=str("tacoma")
    modelo_tc3=0

    #Marca 2
    modelo_n1=str("kicks")
    modelo_nc1=0
    modelo_n2=str("murano")
    modelo_nc2=0
    modelo_n3=str("rogue")
    modelo_nc3=0

    #Marca 3
    modelo_h1=str("santaFe")
    modelo_hc1=0
    modelo_h2=str("tucson")
    modelo_hc2=0
    modelo_h3=str("venue")
    modelo_hc3=0


    marca = str(input("Ingrese la marca del vehiculo que desea ver:"))

    if marca == marca1:
        print("Disponibilidad de",marca1)
        print(marca1, modelo_t1, modelo_tc1)
        print(marca1, modelo_t2, modelo_tc2)      #en inventario deberia ir cantidad de marcas y cantidad de cada tipo de modelo o se podria establecer una cantidad de modelos en variables
        print(marca1, modelo_t3, modelo_tc3)
    
    elif marca == marca2:
        print("Disponibilidad de",marca2)
        print(marca2, modelo_n1, modelo_nc1)
        print(marca2, modelo_n2, modelo_nc2)
        print(marca2, modelo_n3, modelo_nc3)
    
    elif marca == marca3:
        print("Disponibilidad de",marca3)
        print(marca3, modelo_h1, modelo_hc1)
        print(marca3, modelo_h2, modelo_hc2)
        print(marca3, modelo_h3, modelo_hc3)

    selec_marca=str(input("Digite el nombre de la marca que desea retirar:"))
    if selec_marca == "toyota":
        selec_model=str(input("Ingrese el nombre del modelo que desea retirar:"))
    if selec_model==modelo_t1 and modelo_tc1==0:
        print("Disculpe el modelo", modelo_t1,"no está disponible")
    elif selec_model==modelo_t1 and modelo_tc1>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_tc1 -= 1
        print("reservo,",marca1, selec_model)
    elif selec_model==modelo_t2 and modelo_tc2==0:
        print("Disculpe el modelo", modelo_t2,"no está disponible")
    elif selec_model==modelo_t2 and modelo_tc2>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_tc2 -= 1
        print("reservó,",marca1, selec_model)
    elif selec_model==modelo_t3 and modelo_tc3==0:
        print("Disculpe el modelo", modelo_t3,"no está disponible")
    elif selec_model==modelo_t3 and modelo_tc3>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_tc3 -= 1
        print("reservó,",marca1, selec_model)
        
    elif selec_marca == "nissan":
        selec_model=str(input("Ingrese el nombre del modelo que desea retirar:"))
    if selec_model==modelo_n1 and modelo_nc1==0:
        print("Disculpe el modelo", modelo_n1,"no está disponible")
    elif selec_model==modelo_n1 and modelo_nc1>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_nc1 -= 1
        print("reservó,",marca2, selec_model)
    elif selec_model==modelo_n2 and modelo_nc2==0:
        print("Disculpe el modelo", modelo_n2,"no está disponible")
    elif selec_model==modelo_n2 and modelo_nc2>0:
        print("El modelo esta disponible")
        model_reserva=selec_model
        modelo_nc2 -= 1
        print("reservó,",marca2, selec_model)
    elif selec_model==modelo_n3 and modelo_nc3==0:
        print("Disculpe el modelo", modelo_n3,"no está disponible")
    elif selec_model==modelo_n3 and modelo_nc3>0:
        print("El modelo esta disponible")
        model_reserva=selec_model
        modelo_nc3 -= 1
        print("reservó,",marca2, selec_model)
        
    elif selec_marca=="hyundai":
        selec_model=str(input("Ingrese el nombre del modelo que desea retirar:"))
    if selec_model==modelo_h1 and modelo_hc1==0:
        print("Disculpe el modelo", modelo_h1,"no está disponible")
    elif selec_model==modelo_h1 and modelo_hc1>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_hc1 -= 1
        print("reservó,",marca3, selec_model)
    elif selec_model==modelo_h2 and modelo_hc2==0:
        print("Disculpe el modelo", modelo_h2,"no está disponible")
    elif selec_model==modelo_h2 and modelo_hc2>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_hc2 -= 1
        print("reservó,",marca3, selec_model)
    elif selec_model==modelo_h3 and modelo_hc3==0:
        print("Disculpe el modelo", modelo_h3,"no está disponible")
    elif selec_model==modelo_h3 and modelo_hc3>0:
        print("El modelo está disponible")
        model_reserva=selec_model
        modelo_hc3 -= 1
        print("reservó,",marca3, selec_model)


#Creacion de ingreso como usuario registrado

def register():
    db = open("login.txt", "r")
    user = input("Crear usuario: ") 
    password = input("Crear contraseña: ")
    password1 = input("Confirmar contraseña: ")

    u = []
    p = []                                      #Crea diccionarios para el usuario y la contrasena
    for i in db:
        a,b = i.split(",")                     #se recorre todos los datos del documento de texto para
        b = b.strip()                           #Validar los usuarios que estan registrados para que no se logre repetir el user
        u.append(a)                             
        p.append(b)
    data = dict(zip(u,p))                       #{'Wawa': '0201', 'Warren': '2022'} Ejemplo de como se recorre, gracias a los diccionarios

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

    #Evitar objetos duplicados en las listas
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
    (4) Salir
                            """)
                            menu_login = int(input("Ingrese su opcion: "))
                            if menu_login == 1:
                                visualizar_carros()
                            elif menu_login ==2:
                                gestion_inventario()
                            elif menu_login ==3:
                                reservacion()                               
                            elif menu_login == 4:
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
    


def menu(opc = None):
    while True:
        opc = input("""
Bienvenido a Fiderents
                
    (1) Iniciar Sesion
    (2) Registrarte
    (3) Salir                   
                    
Ingrese tu opcion:""")
        if opc == "1":
            ingreso()
        elif opc ==  "2":
            register()
        elif opc ==  "3":
            print("Muchas gracias, por elegirnos")
            break            
        else:
            print("Ingrese una de las 2 opciones!!")
            menu()

menu()

#--------------------------------------------------------------------------------------------



