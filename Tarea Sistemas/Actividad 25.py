PR=float(input("Introduce su promedio: "))
PE=input("Introduce su especialidad (E=Estudiante, P=Profesional): ")
MR=int(input("Introduce la cantidad de materias reprobadas "))

#Definimos los variables descuento y precio de los créditos
D1=0.9
D2=0.80
D3=0.75
P1=180
P2=300

#Empleamos las variantes if, elif y else para definir el descuento y total a pagar según el promedio, especialidad y materias reprobadas
if PR >=19 and PR <=20 and PE =="E" and MR ==0:
    Total1= 55*(P1*D3)
    print("Su total a pagar como estudiante",Total1,"descuento del %25")
elif PR >=18 and PR <19 and PE =="E" and MR ==0:
    Total2= 50*(P1*D1)
    print("Su total a pagar como estudiante",Total2,"descuento del %10")
elif PR >=16 and PR <18 and PE =="E" and MR ==0:
    Total3= 50*(P1)
    print("Su total a pagar como estudiante",Total3)
elif PR >0 and PR <16 and PE =="E" and MR <=3:
    Total4= 45*(P1)
    print("Su total a pagar como estudiante",Total4)
elif PR >0 and PR <16 and PE =="E" and MR >=4:
    Total5= 30*(P1)
    print("Su total a pagar como estudiante",Total5)
elif PR >=18 and PR <=20 and PE =="P" and MR ==0:
    Total6= 55*(P2*D2)
    print("Su total a pagar como estudiante",Total6,"descuento del %20")
elif PR >0 and PR <18 and PE =="P" and MR ==0:
    Total7= 5*(P2)
    print("Su total a pagar como estudiante",Total7)
else:
    print("su valor no es válido")