CC=int(input("Introduce la cantidad de computadoras a comprar "))

#Definimos las viariables
P1=5000
D1=0.9
D2=0.8
D3=0.6

#Aplicamos variables if y elif para gestionar el precio según la cantidad. Adicionalmente agregamos la variable else en caso de un valor negativo 
if CC <5 and CC >0:
    Total1=(CC*(P1*D1))
    print("El monto a pagar es de $",Total1,"por",CC,"computadoras,","se le aplico un descuento del %10")
elif CC >=5 and CC <10:
    Total2=(CC*(P1*D2))
    print("El monto a pagar es de $",Total2,"por",CC,"computadoras,","se le aplico un descuento del %20")
elif CC >=10:
    Total3=(CC*(P1*D3))
    print("El monto a pagar es de $",Total3,"por",CC,"computadoras,","se le aplico un descuento del %40")
else:
    print("Introdujo un valor no válido")