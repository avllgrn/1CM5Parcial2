import subprocess
import Clases.ClaseFraccion

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    F = Clases.ClaseFraccion.Fraccion(1,-2)
    print('F')
    print(F)
    print()

    print('(Ingresa un denominador negativo)')
    print('F')
    F.pideleAlUsuarioTuEstado()
    print('F')
    print(F)
    print()

    print('F.modificaTuEstado(5, -6)')
    F.modificaTuEstado(5, -6)
    print('F')
    print(F)
    print()

    print('F.numerador = 7')
    print('F.denominador = -8')
    F.numerador = 7
    F.denominador = -8
    print('F')
    print(F)
    print()

    F2 = Clases.ClaseFraccion.Fraccion(-1,-2)
    print('F2')
    print(F2)
    print()

    print('(Ingresa un numerador negativo)')
    print('(Ingresa un denominador negativo)')
    print('F2')
    F2.pideleAlUsuarioTuEstado()
    print('F2')
    print(F2)
    print()

    print('F2.modificaTuEstado(-5, -6)')
    F2.modificaTuEstado(-5, -6)
    print('F2')
    print(F2)
    print()

    print('F2.numerador = -7')
    print('F2.denominador = -8')
    F2.numerador = -7
    F2.denominador = -8
    print('F2')
    print(F2)
    print()

    print('F2.denominador = 0')
    F2.denominador = 0
    print('F2')
    print(F2)
    print()
