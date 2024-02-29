#Creacion de ingreso como usuario registrado

def register():
    db = open("login.txt", "r")
    user = input("Crear usuario: ")
    password = input("Crear contraseña: ")
    password1 = input("Confirmar contraseña: ")

    if password != password1:
        print("La contraseñas no son iguales!!")
        register()
    elif user  in db:
        print("El usuario ya existe!!")
        register()  

    else:
        db = open("login.txt", "a")
        db.write(user + ", " + password + "\n")
        print("Se registro con exito!!")
        
register()



