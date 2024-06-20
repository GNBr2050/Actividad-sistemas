FI=float(input("Introduce cantidad de horas: "))

if FI>40:
    EX=FI-40
    Total=((40*16)+(EX*18))
    print("Su salario es de $",Total,"por un total de",FI,"horas")
    print(EX)
else:
    print("Su salario es de $",(FI*16),",no se aplican horas extras")