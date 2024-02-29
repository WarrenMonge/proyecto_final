#Proyecto final
#vizualizar vehiculos

marca1=str("toyota")
marca2=str("nisan")
marca3=str("hyundai")

modelo_t1=str("yaris")          #para ejemplo
modelo_t1=0
marca = str(input("ingrese la marca que desea ver:"))

if marca == marca1:
  print("disponibilidad de",marca1)
  print(marca1, modelo_t1, cantidad)
  print(marca1, modelo_t2, cantidad)      #en inventario deberia ir cantidad de marcas y cantidad de cada tipo de modelo o se podria establecer una cantidad de modelos en variables
  print(marca1, modelo_t3, cantidad)
  
elif marca == marca2:
   print("disponibilidad de",marca2)
   print(marca2, modelo_n1, cantidad)
   print(marca2, modelo_n2, cantidad)
   print(marca2, modelo_n3, cantidad)
  
elif marca == marca3:
   print("disponibilidad de",marca3)
   print(marca3, modelo_h1, cantidad)
   print(marca3, modelo_h2, cantidad)
   print(marca3, modelo_h3, cantidad)

selec_model=str(inpur("digite el nombre del modelo que desea retirar:"))
if selec_model == 0:
  print("disculpe el modelo", selec_model,"no esta disponible")
elif selec_model >= 1:
  print("modleo disponible")
