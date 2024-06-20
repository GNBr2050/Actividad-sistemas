KM=float(input("Introduce los kilos de manzana "))
PM=float(input("Introduce el precio de cada kilo "))

#Definimos los porcentajes de descuento
D1=0.9
D2=0.85
D3=0.8

#Empleamos las variantes if, elif y else para definir el descuento según la cantidad
if KM >0 and KM <=2 and PM>0:
    Total1=(KM*PM)
    print("El monto a pagar es de $",Total1,"por",KM,"kilogramos de manzana,","no se aplico un descuento")
elif KM >2 and KM <=5:
    Total2=(KM*(PM*D1))
    print("El monto a pagar es de $",Total2,"por",KM,"kilogramos de manzana,","se aplico un descuento del %10")
elif KM >5 and KM <=10:
    Total3=(KM*(PM*D2))
    print("El monto a pagar es de $",Total3,"por",KM,"kilogramos de manzana,","se aplico un descuento del %15")
elif KM >10:
    Total4=(KM*(PM*D3))
    print("El monto a pagar es de $",Total4,"por",KM,"kilogramos de manzana,","se aplico un descuento del %20")
else:
    print("Introdujo un valor no válido")