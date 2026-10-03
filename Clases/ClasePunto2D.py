import subprocess 

class Punto2D:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y
        self.verificaPunto2D()
        # print(f'Objeto {self} construido')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.verificaPunto2D()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.verificaPunto2D()

    def __del__(self):
        pass
        # print(f'Objeto {self} destruido')

    def __str__(self):
        return f'({self._x}, {self._y})'

    def verificaPunto2D(self):
        try:
            self._x = float(self._x)
        except:
            raise TypeError('x DEBE ser numérica...')
        finally:
            try:
                self._y = float(self._y)
            except:
                raise TypeError('y DEBE ser numérica...')

    def pideleAlUsuarioTuEstado(self):
        self._x = input('Ingresa x ')
        self._y = input('Ingresa y ')
        self.verificaPunto2D()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, x, y):
        self._x = x
        self._y = y
        self.verificaPunto2D()

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self._x},{self._y}')

    def cargaTuEstado(self, ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self._x = float(datos[0])
        self._y = float(datos[1])

if __name__ == '__main__':
    subprocess.run('cls', shell=True)
