import subprocess
import Clases.ClaseFraccion

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    F1 = Clases.ClaseFraccion.Fraccion()
    F2 = Clases.ClaseFraccion.Fraccion(7, 8)
    F3 = Clases.ClaseFraccion.Fraccion(9)

    print(f'F1 = {F1}')
    print(f'F2 = {F2}')
    print(f'F3 = {F3}')
    print()

    F1.modificaTuEstado(5, 6)
    print(f'F1 = ', end='')
    F1.muestraTuEstado()
    print()

    print('F1')

    F1.pideleAlUsuarioTuEstado()
    print('F2')
    F2.pideleAlUsuarioTuEstado()
    print()

    F4 = F1+F2
    F5 = F1-F2
    F6 = F1*F2

    print(f'F1+F2 = {F4}')
    print(f'F1-F2 = {F5}')
    print(f'F1*F2 = {F6}')

    F7 = F1/F2
    print(f'F1/F2 = {F7}')
