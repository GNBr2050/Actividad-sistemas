TP=int(input("Introduce la cantidad de camisas "))
TC=int(input("Introduce el monto de la compra "))

#Definimos las variables a descontar
Desc1= 0.05
Desc2= 0.20

#Empleamos las condicionales if para evaluar la cantidad de camisas
if TP<3:
    Total1= TC*(1-(Desc1*TP))
    print("Su total a pagar es de $",Total1)
elif TP>=3:
    Total2= TC*(1-(Desc2))
    print("Su total a pagar es de $",Total2)