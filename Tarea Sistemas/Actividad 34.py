class Auto:
    def __init__(self, marca, modelo, año, color, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kilometraje = kilometraje
        self.motor_encendido = False
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Kilometraje: {self.kilometraje} km")
    
    def arrancar_motor(self):
        if not self.motor_encendido:
            self.motor_encendido = True
            print("El motor ha sido arrancado.")
        else:
            print("El motor ya está encendido.")
    
    def apagar_motor(self):
        if self.motor_encendido:
            self.motor_encendido = False
            print("El motor ha sido apagado.")
        else:
            print("El motor ya está apagado.")
    
    def actualizar_kilometraje(self, km):
        if km >= self.kilometraje:
            self.kilometraje = km
            print(f"El kilometraje ha sido actualizado a {self.kilometraje} km.")
        else:
            print("No se puede reducir el kilometraje.")

#Instanciar un objeto de la clase Auto
mi_auto = Auto("Toyota", "Corolla", 2018, "Rojo", 50000)

#Mostrar la información del auto
mi_auto.mostrar_informacion()

#Arrancar el motor del auto
mi_auto.arrancar_motor()

#Actualizar el kilometraje del auto
mi_auto.actualizar_kilometraje(55000)

#Apagar el motor del auto
mi_auto.apagar_motor()