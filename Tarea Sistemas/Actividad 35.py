#Definición de la superclase Personaje
class Personaje:
    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Salud: {self.salud}")
    
    def atacar(self):
        print(f"{self.nombre} realiza un ataque básico.")

#Definición de la subclase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, nivel, salud, fuerza):
        super().__init__(nombre, nivel, salud)
        self.fuerza = fuerza
    
    def atacar(self):
        print(f"{self.nombre} golpea con su espada con fuerza {self.fuerza}.")

# Definición de la subclase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, nivel, salud, poder_magico):
        super().__init__(nombre, nivel, salud)
        self.poder_magico = poder_magico
    
    def atacar(self):
        print(f"{self.nombre} lanza un hechizo poderoso con magia {self.poder_magico}.")

#Definición de la subclase Tanque que hereda de Personaje
class Tanque(Personaje):
    def __init__(self, nombre, nivel, salud, resistencia):
        super().__init__(nombre, nivel, salud)
        self.resistencia = resistencia
    
    def defender(self):
        print(f"{self.nombre} bloquea el daño con una alta resistencia de {self.resistencia}.")

#Instanciación de objetos de las subclases
guerrero = Guerrero("Aragorn", 10, 100, 20)
mago = Mago("Gandalf", 12, 80, 30)
tanque = Tanque("Hulk", 15, 150, 50)

#Mostrar información y realizar acciones de los personajes
print("--- Guerrero ---")
guerrero.mostrar_informacion()
guerrero.atacar()

print("\n--- Mago ---")
mago.mostrar_informacion()
mago.atacar()

print("\n--- Tanque ---")
tanque.mostrar_informacion()
tanque.defender()

#Utilice un tutorial de referencia para la creación de clases