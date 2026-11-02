import subprocess
import Clases.ClaseFraccion

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    F1 = Clases.ClaseFraccion.Fraccion()
    print(f'F1 = {F1}')
    print('F1 = ',end='')
    F1.muestraTuEstado()
    print()

    F2 = Clases.ClaseFraccion.Fraccion(1, 2)
    print(f'F2 = {F2}')
    print('F2 = ',end='')
    F2.muestraTuEstado()
    print()

    F1.pideleAlUsuarioTuEstado()
    print(f'F1 = {F1}')
    print('F1 = ',end='')
    F1.muestraTuEstado()
    print()

    F3 = Clases.ClaseFraccion.Fraccion(5)
    print(f'F3 = {F3}')
    print('F3 = ',end='')
    F3.muestraTuEstado()
    print()

    F3.modificaTuEstado(6, 7)
    print(f'F3 = {F3}')
    print('F3 = ',end='')
    F3.muestraTuEstado()
    print()
