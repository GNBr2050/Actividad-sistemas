E1=float(input("Parcial 1 "))
E2=float(input("Parcial 2 "))
E3=float(input("Parcial 3 "))
E4=float(input("Parcial 4 "))
EC1=float(input("Continua 1 "))
EC2=float(input("Continua 2 "))
EC3=float(input("Continua 3 "))
EC4=float(input("Continua 4 "))
EC5=float(input("Continua 5 "))
EC6=float(input("Continua 6 "))

#Se tiene en cuenta un total de 5 calificaciones (4 del parcial y 1 de las continuas), luego se promedia

E=((E1)+(E2*2)+(E3*2)+(E4*3))
EC=(((EC1)+(EC2)+(EC3)+(EC4)+(EC5)+(EC6))/6)

print("Su calificación final fue: ",((E+EC)/9))