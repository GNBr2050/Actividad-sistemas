IN=float(input("Introduce su inversión $"))
ME=float(input("Introduce la cantidad de meses:"))
#Rendimiento fijo a %3

IT=ME*0.03
GN1=IN*(1+IT)
if GN1 > 7000:
    print("Su inversión supero $7000 y ahora es $",GN1)
else:
    print("Su inversión crecio hasta $",GN1)