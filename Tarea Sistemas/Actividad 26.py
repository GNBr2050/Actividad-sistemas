#Comprobamos si el número es primo o no con una función
def es_primo(número):
    if número <= 1:
        return False
    for comprobar in range(2, int(numero ** 0.5) + 1):
        if numero % comprobar == 0:
            return False
    return True

#Llamamos a la función para ejecutar el input
numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(numero,"es un número primo")
else:
    print(numero,"no es un número primo")