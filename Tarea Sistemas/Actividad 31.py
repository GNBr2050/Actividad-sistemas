class NumeroRomano:
    def __init__(self, numero):
        self.numero = numero

    def a_romano(self):
        #Mapear los valores enteros a sus equivalentes en números romanos
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        resultado = ''
        numero = self.numero
        
        #Iterar sobre los valores y construir el número romano
        for valor, romano in valores:
            while numero >= valor:
                resultado += romano
                numero -= valor
        
        return resultado

#Ejemplo de uso
numero = int(input("Introduce un número entero: "))
convertidor = NumeroRomano(numero)
numero_romano = convertidor.a_romano()
print(f"El número {numero} en números romanos es: {numero_romano}")