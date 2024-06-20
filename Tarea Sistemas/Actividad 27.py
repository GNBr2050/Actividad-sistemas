#Solicitar al usuario un input de los dos números
N1=int(input("Introduce el primer número: "))
N2=int(input("Introduce el segundo número: "))

#Verificar si el primer número es menor que el segundo
if N1 >N2:
    N1,N2= N2,N1

#Calcular la suma de los valores dentro del rango
suma=0
for valor in range(N1,N2+1):
    suma +=valor
print("La suma de todos los valores entre",N1,"y",N2,"es",suma)