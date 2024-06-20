PU=float(input("Introduce el monto de su compra $"))

#La cantidad a introducer es libre, se aplica un descuento si el monto es superior a 1000, en caso contrario no se aplica un descuento
if PU >1000:
        TO=PU*0.8
        print("Se monto a pagar es de $",TO," con un descuento del %20")
else:
      print("Su monto a pagar es de $",PU)