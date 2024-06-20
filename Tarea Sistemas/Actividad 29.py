import math

#Emplear un rango del 1 al 30
for valor in range(1, 31):
    if valor % 7==0:
        continue
    
    # Calcular seno, coseno y tangente con la libreria math (solo tres decimales) 
    seno=math.sin(math.radians(valor))
    coseno=math.cos(math.radians(valor))
    tangente=math.tan(math.radians(valor))
    
    print("Número: ",valor)
    print("Seno: ","{:.3f}".format(seno))
    print("Coseno: ","{:.3f}".format(coseno))
    print("Tangente: ","{:.3f}".format(tangente))
    print()