#Proyecto final
#vizualizar vehiculos

marca1=str("toyota")          #Las marcas y modelos son como ejemplo
marca2=str("nissan")
marca3=str("hyundai")

#Marca 1
modelo_t1=str("yaris")          
modelo_tc1=0
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


marca = str(input("ingrese la marca que desea ver:"))

if marca == marca1:
  print("disponibilidad de",marca1)
  print(marca1, modelo_t1, modelo_tc1)
  print(marca1, modelo_t2, modelo_tc2)      #en inventario deberia ir cantidad de marcas y cantidad de cada tipo de modelo o se podria establecer una cantidad de modelos en variables
  print(marca1, modelo_t3, modelo_tc3)
  
elif marca == marca2:
   print("disponibilidad de",marca2)
   print(marca2, modelo_n1, modelo_nc1)
   print(marca2, modelo_n2, modelo_nc2)
   print(marca2, modelo_n3, modelo_nc3)
  
elif marca == marca3:
   print("disponibilidad de",marca3)
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
    

  
    
  

