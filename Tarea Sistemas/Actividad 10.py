OR=float(input("Introduce el precio orinal $"))
GN=float(input("Introduce el porcentaje de ganancia %"))

Total=(OR*((GN/100)+1))
print("Debe de vender el producto a $","{0:.3f}".format(Total),".Para obtener una ganancia del %", GN)
