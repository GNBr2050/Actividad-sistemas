Sueldo=float(input("Introduce su salario "))
Aumento=float(input("Introduce el porcentaje de su aumento "))

Total=(Sueldo*(((Aumento/100)+1)))
print("Su salario es de","{0:.2f}".format(Total))

