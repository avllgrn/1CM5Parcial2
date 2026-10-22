import math

class Circulo:
    def __init__(self, radio=0.0):
        self.radio = float(radio)
        # print(f'Objeto {self.radio}, construido...')

    def __del__(self):
        # print(f'Objeto {self.radio}, destruido...')
        pass

    def __str__(self):
        cadena = ''
        cadena = cadena + f'Radio: {self.radio}\n'
        cadena = cadena + f'Diametro: {self.dameTuDiametro()}\n'
        cadena = cadena + f'Area: {self.dameTuArea()}\n'
        cadena = cadena + f'Perimetro: {self.dameTuPerimetro()}\n'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        self.radio = float(input('Dame mi radio '))

    def muestraTuEstado(self):
        print(self)

    def dameTuDiametro(self):
        return self.radio*2

    def dameTuArea(self):
        return math.pi * self.radio**2

    def dameTuPerimetro(self):
        return 2.* math.pi * self.radio

