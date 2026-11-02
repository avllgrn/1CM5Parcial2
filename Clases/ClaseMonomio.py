from os import system

class Monomio:
    ######################################################################################################################################################################################################## 
    # MÉTODOS
    ######################################################################################################################################################################################################## 
    def __init__(self, coeficiente=0.0, exponente=1.0):
        self.__coeficiente = coeficiente
        self.__exponente = exponente
        self.verificaTuEstado()

    @property
    def coeficiente(self):
        return self.__coeficiente

    @coeficiente.setter
    def coeficiente(self, valor):
        self.__coeficiente = valor
        self.verificaTuEstado()

    @property
    def exponente(self):
        return self.__exponente

    @exponente.setter
    def exponente(self, valor):
        self.__exponente = valor
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self) -> str:
        return f'{self.__coeficiente}x^{self.__exponente}'

    def muestraTuEstado(self):
        print(self)

    def pideleAlUsuarioTuEstado(self):
        self.__coeficiente = input('Dame mi coeficiente ')
        self.__exponente = input('Dame mi exponente ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, coeficiente, exponente):
        self.__coeficiente = coeficiente
        self.__exponente = exponente
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__coeficiente = float(self.__coeficiente)
        except ValueError:
            self.__coeficiente = 0.0
        try:
            self.__exponente = float(self.__exponente)
        except ValueError:
            self.__exponente = 1.0

        if self.__coeficiente == 0 and self.__exponente==0:
            print('Error! Monomio indeterminado...')
            self.__coeficiente = 0.0
            self.__exponente = 1.0

    def __add__(self, Derecho):
        S = Monomio()
        if self.__exponente==Derecho.exponente:
            S.coeficiente=self.__coeficiente+Derecho.coeficiente
            S.exponente = self.__exponente
        return S

    def __sub__(self, Derecho):
        R = Monomio()
        if self.__exponente==Derecho.exponente:
            R.coeficiente=self.__coeficiente-Derecho.coeficiente
            R.exponente = self.__exponente
        return R

    def __mul__(self, Derecho):
        M = Monomio()
        M.coeficiente = self.__coeficiente*Derecho.coeficiente
        M.exponente = self.__exponente+Derecho.exponente
        return M

    def __truediv__(self, Derecho):
        D = Monomio()
        if Derecho.coeficiente!=0:
            D.coeficiente = self.__coeficiente/Derecho.coeficiente
            D.exponente = self.__exponente-Derecho.exponente
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
