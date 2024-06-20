SX=input("Introduce su sexo (H=Hombre, M=Mujer): ")
EM=int(input("Introduce su cantidad de meses: "))
EA=int(input("Introduce su cantidad de años: "))
EG=float(input("Introduce nivel de hemoglobina: "))

#Conversión de años a meses
ED=(EA*12)+(EM)

#Empleamos una doble condicional if para determinar el nivel de hemoglobina en base a la edad, hemoglobina y sexo de los usuarios
if ED >0 and ED <=1:
    if EG >0 and EG <13:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=13 and EG <=26:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >26:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >1 and ED <=6:
    if EG >0 and EG <10:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=10 and EG <=18:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >18:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >6 and ED <=12:
    if EG >0 and EG <11:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=11 and EG <=15:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >15:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >12 and ED <60:
    if EG >0 and EG <11.5:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=11.5 and EG <=15:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >15:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >60 and ED <=120:
    if EG >0 and EG <12.6:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=12.6 and EG <=15.5:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >15.5:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >120 and ED <=180:
    if EG >0 and EG <13:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=13 and EG <=15.5:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >15.5:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >180 and SX == "M":
    if EG >0 and EG <12:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=12 and EG <=16:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >16:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
elif ED >180 and SX == "H":
    if EG >0 and EG <14:
        print("Niveles bajos de hemoglobina,"," Positivo")
    elif EG >=14 and EG <=18:
        print("Niveles normales de hemoglobina,"," Normal")
    elif EG >18:
        print("Niveles altos de hemoglobina,"," Negativo")
    else:
        print("No puedes tener niveles negativos de hemoglobina")
else:
    print("Introdujo un sexo no valido")   