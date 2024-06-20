class RomanoAEntero:
    def __init__(self, romano):
        self.romano = romano

    def a_entero(self):
        #Mapear los símbolos romanos a sus valores enteros
        valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        
        numero = 0
        anterior = 0
        
        # Iterar sobre los caracteres del número romano de derecha a izquierda
        for simbolo in reversed(self.romano):
            valor = valores[simbolo]
            if valor >= anterior:
                numero += valor
            else:
                numero -= valor
            anterior = valor
        
        return numero

#Ejemplo de uso
romano = input("Introduce un número romano: ")
convertidor = RomanoAEntero(romano)
numero_entero = convertidor.a_entero()
print(f"El número romano {romano} convertido a entero es: {numero_entero}")