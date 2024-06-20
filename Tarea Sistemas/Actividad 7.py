from datetime import datetime
from dateutil.relativedelta import relativedelta

Año=int(input("Introduce su año de nacimiento: "))
Mes=int(input("Introduce el mes de nacimiento: "))
Día=int(input("Introduce el día de nacimiento: "))

Hoy=datetime.today()
Nacimiento=datetime(Año,Mes,Día)
Resultado = relativedelta(Hoy,Nacimiento)

print("Usted tiene:  ",Resultado.years,"años ",Resultado.months,"meses ",Resultado.days,"días")