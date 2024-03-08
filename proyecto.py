#Proyecto final

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
