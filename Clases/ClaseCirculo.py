import math

class Circulo:
    ######################################################################################################################################################################################################## 
    # MÉTODOS
    ######################################################################################################################################################################################################## 
    def __init__(self, radio=0.0):
        self.__radio = radio
        self.verificaTuEstado()
        # print(f'Objeto {self.__radio}, construido...')

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, r):
        self.__radio = r
        self.verificaTuEstado()

    def __del__(self):
        # print(f'Objeto {self.__radio}, destruido...')
        pass

    def __str__(self):
        cadena = ''
        cadena = cadena + f'Radio: {self.__radio}\n'
        cadena = cadena + f'Diametro: {self.dameTuDiametro()}\n'
        cadena = cadena + f'Area: {self.dameTuArea()}\n'
        cadena = cadena + f'Perimetro: {self.dameTuPerimetro()}\n'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        self.__radio = input('Dame mi radio ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, valor):
        self.radio = valor
        self.verificaTuEstado()

    def dameTuDiametro(self):
        return self.__radio*2

    def dameTuArea(self):
        return math.pi * self.__radio**2

    def dameTuPerimetro(self):
        return 2.* math.pi * self.__radio

    def verificaTuEstado(self):
        try:
            self.__radio = float(self.__radio)
        except:
            self.__radio = 0.0

        if self.__radio<0:
            self.__radio = 0.0
