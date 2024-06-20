DO=float(input("Introduce la cantidad de minutos de sueño de sueño: "))
JU=float(input("Introduce la cantidad de minutos de juego: "))

#Un día igual a 1440 minutos
TO=(DO*1.08)+(JU*1.66)
#Un Kilogramo de peso equivale a 7700 calorías
CO=TO/7700
print("Usted consumio",TO,"calorias que equivale a","{0:.2}".format(CO),"kilogramos de peso")