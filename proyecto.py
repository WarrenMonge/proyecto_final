#Proyecto final

print("Gestion de inventario")

while True:
    print("""
    (1) Agregar vehiculos
    (2) Inhabilite vehiculos
    (3) Salir
    """)
    gest_ans = int(input("Ingrese su opcion: "))
    if gest_ans == 1:
        marca = input ("Ingrese la marca del vehiculo")
        modelo = input("Ingrese el modelo del vehiculo")
        año = input("Ingrese el año del vehiculo")
        cc = input("Ingrese el cilindraje del vehiculo")
        price_ad = input("Ingrese el precio de alquiler por dia")
        price_car = input("Ingrese el precio del vehiculo")

    elif gest_ans == 2:
        print