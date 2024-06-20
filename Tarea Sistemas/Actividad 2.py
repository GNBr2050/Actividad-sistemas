Inversión=float(input("Introduce su inversión"))
Rendimiento=int(input("Introduce su porcentaje de rendimiento"))
Tiempo=int(input("Introduce la cantidad de meses"))

Ganancia=(((Tiempo*Rendimiento)*Inversión)/100)
Total=(Ganancia+Inversión)

print("Inversión ", Inversión)
print("Ganancia de ", Ganancia)
print("Total ", Total)