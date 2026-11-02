from math import sqrt, pow

class Complejo:
    ######################################################################################################################################################################################################## 
    # MÉTODOS
    ######################################################################################################################################################################################################## 
    def __init__(self, real=0.0, imaginario=0.0):
        self.__real = real
        self.__imaginario = imaginario
        self.verificaTuEstado()

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, valor):
        self.__real = valor
        self.verificaTuEstado()

    @property
    def imaginario(self):
        return self.__imaginario

    @imaginario.setter
    def imaginario(self, valor):
        self.__imaginario = valor
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        cadena = f'{self.__real}'
        if self.__imaginario<0:
            cadena = cadena + f'{self.__imaginario}'
        else:
            cadena = cadena + f'+{self.__imaginario}'
        cadena = cadena + 'i'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        self.__real = input('Dame mi real ')
        self.__imaginario = input('Dame mi imaginario ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, real, imaginario):
        self.__real = real
        self.__imaginario = imaginario
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__real = float(self.__real)
        except ValueError:
            self.__real = 0.0
        try:
            self.__imaginario = float(self.__imaginario)
        except ValueError:
            self.__imaginario = 0.0

    def __add__(self, Derecho):
        S = Complejo()
        S.real = self.__real+Derecho.real
        S.imaginario = self.__imaginario+Derecho.imaginario
        return S

    def __sub__(self, Derecho):
        R = Complejo()
        R.real = self.__real-Derecho.real
        R.imaginario = self.__imaginario-Derecho.imaginario
        return R

    def __mul__(self, Derecho):
        M = Complejo()
        M.real = self.__real*Derecho.real-self.__imaginario*Derecho.imaginario
        M.imaginario = self.__real*Derecho.imaginario+self.__imaginario*Derecho.real
        return M

    def __truediv__(self, Derecho):
        D = Complejo()
        D.real = (self.__real*Derecho.real+self.__imaginario*Derecho.imaginario) / (Derecho.real**2+Derecho.imaginario**2)
        D.imaginario = (Derecho.real*self.__imaginario-self.__real*Derecho.imaginario) / (Derecho.real**2+Derecho.imaginario**2)
        return D

######################################################################################################################################################################################################## 
# FUNCIONES
########################################################################################################################################################################################################
def add(Izquierdo, Derecho):
    return Izquierdo+Derecho

def sub(Izquierdo, Derecho):
    return Izquierdo-Derecho

def mul(Izquierdo, Derecho):
    return Izquierdo*Derecho

def truediv(Izquierdo, Derecho):
    return Izquierdo/Derecho
