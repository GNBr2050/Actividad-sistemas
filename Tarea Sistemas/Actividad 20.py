CLL=int(input("Introduce la cantidad de llantas a contar "))

#Definimos el precio de las llantas
P1=400
P2=350

#Aplicamos variables if para gestionar el precio según la cantidad
if CLL <5:
    Total1=(CLL*P1)
    print("El monto a pagar es de $",Total1,"por",CLL,"llantas")
elif CLL >=5:
    Total2=(CLL*P2)
    print("El monto a pagar es de $",Total2,"por",CLL,"llantas")