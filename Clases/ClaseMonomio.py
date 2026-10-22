from os import system

class Monomio:
    def __init__(self, coeficiente=0.0, exponente=1):
        self.coeficiente = int(coeficiente)
        self.exponente = int(exponente)

    def __del__(self):
        pass

    def __str__(self) -> str:
        return f'{self.coeficiente}x^{self.exponente}'

    def muestraTuEstado(self):
        print(self)

    def pideleAlUsuarioTuEstado(self):
        self.coeficiente = float(input('Dame mi coeficiente '))
        self.exponente = float(input('Dame mi exponente '))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, coeficiente, exponente):
        self.coeficiente = int(coeficiente)
        self.exponente = int(exponente)
