Año=int(input("Introduce un año: "))

#Un año es bisiesto si es divisible por 4
def BI(Año):
    return (Año%4 ==0) and (Año%100!=0 or Año%400==0)

#Buscar el siguiente año bisiesto con un bucle
SAño =Año +1
while not BI(SAño):
    SAño += 1

print(f"El año bisiesto mas cercano de",Año,"es",SAño)