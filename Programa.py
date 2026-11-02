import subprocess
import Clases.ClaseCirculo

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    C = Clases.ClaseCirculo.Circulo(-1)
    print('C')
    print(C)

    print('(Ingresa un radio negativo)')
    print('C')
    C.pideleAlUsuarioTuEstado()
    print('C')
    print(C)
    print()

    print('C.modificaTuEstado(-1)')
    C.modificaTuEstado(-1)
    print('C')
    print(C)
    print()

    print('C.radio = -1')
    C.radio = -1
    print('C')
    print(C)
    print()
