from os import system

class Fraccion:
    def __init__(self, numerador=0, denominador=1):
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    def __str__(self):
        estado = f'{self.numerador}/'
        estado += f'{self.denominador}'
        return estado
    def del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.numerador = input('Dame mi numerador ')
        self.denominador = input('Dame mi denominador ')

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, Derecho):
        S = Fraccion()
        S.numerador = self.numerador*Derecho.denominador + self.denominador*Derecho.numerador
        S.denominador = self.denominador*Derecho.denominador
        return S

    def __sub__(self, Derecho):
        R = Fraccion()
        R.numerador = self.numerador*Derecho.denominador - self.denominador*Derecho.numerador
        R.denominador = self.denominador*Derecho.denominador
        return R

    def __mul__(self, Derecho):
        M = Fraccion()
        M.numerador = self.numerador*Derecho.numerador
        M.denominador = self.denominador*Derecho.denominador
        return M

    def __truediv__(self, Derecho):
        D = Fraccion()
        D.numerador = self.numerador*Derecho.denominador
        D.denominador = self.denominador*Derecho.numerador
        return D
    
def add(Izquierdo, Derecho):
    S = Fraccion()
    S.numerador = Izquierdo.numerador*Derecho.denominador + Izquierdo.denominador*Derecho.numerador
    S.denominador = Izquierdo.denominador*Derecho.denominador
    return S

def sub(Izquierdo, Derecho):
    S = Fraccion()
    S.numerador = Izquierdo.numerador*Derecho.denominador - Izquierdo.denominador*Derecho.numerador
    S.denominador = Izquierdo.denominador*Derecho.denominador
    return S

def mul(Izquierdo, Derecho):
    M = Fraccion()
    M.numerador = Izquierdo.numerador*Derecho.numerador
    M.denominador = Izquierdo.denominador*Derecho.denominador
    return M

def truediv(Izquierdo, Derecho):
    D = Fraccion()
    D.numerador = Izquierdo.numerador*Derecho.denominador
    D.denominador = Izquierdo.denominador*Derecho.numerador
    return D
