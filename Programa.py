import subprocess
import Clases.ClaseMonomio

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    M1 = Clases.ClaseMonomio.Monomio(0, 0)
    print('M1')
    print(M1)
    print()

    M2 = Clases.ClaseMonomio.Monomio()
    print('(Ingresa un coeficiente cero)')
    print('(Ingresa un exponente cero)')
    print('M2')
    M2.pideleAlUsuarioTuEstado()

    M3 = Clases.ClaseMonomio.Monomio()
    print('M3')
    print(M3)
    print()
    print('M3.coeficiente = 0')
    M3.coeficiente = 0

    M4 = Clases.ClaseMonomio.Monomio(2,3)
    print('M4')
    print(M4)
    print('M4.coeficiente = 0')
    print('M4.exponente = 0')
    M4.coeficiente = 0
    M4.exponente = 0
    print('M4')
    print(M4)
    print()
