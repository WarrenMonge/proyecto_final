#Creacion de ingreso como usuario registrado

def register():
    db = open("login.txt", "r")
    user = input("Crear usuario: ")
    password = input("Crear contraseña: ")
    password1 = input("Confirmar contraseña: ")

    u = []
    p = []                                      #Crea diccionarios para el usuario y la contrasena
    for i in db:
        a,b = i.split(", ")                     #se recorre todos los datos del documento de texto para
        b = b.strip()                           #Validar los usuarios que estan registrados para que no se logre repetir el user
        u.append(a)                             
        p.append(b)
    data = dict(zip(u,p))                       #{'Wawa': '0201', 'Warren': '2022'} Ejemplo de como se recorre, gracias a los diccionarios
    print(data)

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

register()

def ingreso():
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if not len(user or password) < 1:
        pass



