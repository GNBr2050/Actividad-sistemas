class Estudiante:
    def __init__(self, nombre, apellido, numero_identificacion, carrera, ano_ingreso):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_identificacion = numero_identificacion
        self.carrera = carrera
        self.ano_ingreso = ano_ingreso
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"ID: {self.numero_identificacion}")
        print(f"Carrera: {self.carrera}")
        print(f"Año de ingreso: {self.ano_ingreso}")
    
    def calcular_ano_actual(self):
        from datetime import datetime
        ano_actual = datetime.now().year
        return ano_actual - self.ano_ingreso

#Instanciar un objeto de la clase Estudiante
mi_carnet = Estudiante("Juan", "Pérez", "123456789", "Ingeniería Informática", 2020)

#Mostrar la información del estudiante
mi_carnet.mostrar_informacion()

#Calcular y mostrar el año actual en la universidad
anos_en_la_universidad = mi_carnet.calcular_ano_actual()
print(f"Años en la universidad: {anos_en_la_universidad}")