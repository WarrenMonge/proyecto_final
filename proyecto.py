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
    opc = input("Iniciar | Registrarse: ")
    if opc == "Iniciar":
        ingreso()
    elif opc ==  "Registrarse":
        register()
    else:
        print("Ingrese una de las 2 opciones!!")
        menu()

menu()


