TC=float(input("Introduce el monto a pagar "))

#Se aplica el interes unicamente cuando el monto es inferior a 500000 (ejemplo2) en la parte del crédito (es lo que entendí del enunciado)
if TC>500000:
    Empre1=(TC*0.55)
    Prest1=(TC*0.3)
    Cred1=(TC*0.15)
    print("El monto a pagar (sin terereses) es de $",Empre1,"por parte de la empresa ",Prest1,"$ por prestamo de un banco y ",Cred1,"$ con un prestamo del fabricante")
    #La empresa paga un %70 y el resto con un credito al fabricante (pagando adicionalmente un %20 de ese crédito)
elif TC<500000:
    Empre2=(TC*0.7)
    Cred2=(1.2*(TC*0.3))
    print("El monto a pagar (con intereses) es de $",Empre2," por parte de la empresa y $",Cred2,"en credito al fabricante")