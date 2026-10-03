import subprocess 

class Fraccion:
    def __init__(self, numerador=0, denominador=1):
        self._numerador = numerador
        self._denominador = denominador
        self.verificaFraccion()
        # print(f'Objeto {self} construido')

    @property
    def numerador(self):
        return self._numerador

    @numerador.setter
    def numerador(self, numerador):
        self._numerador = numerador
        self.verificaFraccion()

    @property
    def denominador(self):
        return self._denominador

    @denominador.setter
    def denominador(self, denominador):
        self._denominador = denominador
        self.verificaFraccion()

    def __del__(self):
        pass
        # print(f'Objeto {self} destruido')

    def __str__(self):
        return f'{self._numerador}/{self._denominador}'

    def verificaFraccion(self):
        try:
            self._numerador = int(self._numerador)
        except:
            raise TypeError('numerador DEBE ser entero')
        finally:
            try:
                self._denominador = int(self._denominador)
            except:
                raise TypeError('denominador DEBE ser entero')
            else:
                if self._denominador < 0:
                    self._numerador *= -1
                    self._denominador *= -1

            if self._denominador == 0:
                raise ZeroDivisionError

    def pideleAlUsuarioTuEstado(self):
        self._numerador = input('Ingresa numerador ')
        self._denominador = input('Ingresa denominador ')
        self.verificaFraccion()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, numerador, denominador):
        self._numerador = numerador
        self._denominador = denominador
        self.verificaFraccion()

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self._numerador},{self._denominador}')

    def cargaTuEstado(self, ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self._numerador = int(datos[0])
        self._denominador = int(datos[1])

if __name__ == '__main__':
    subprocess.run('cls', shell=True)
