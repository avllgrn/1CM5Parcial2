import subprocess
import Clases.ClaseMonomio

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    M1 = Clases.ClaseMonomio.Monomio()
    M2 = Clases.ClaseMonomio.Monomio(7, 8)
    M3 = Clases.ClaseMonomio.Monomio(9)

    print(f'M1 = {M1}')
    print(f'M2 = {M2}')
    print(f'M3 = {M3}')
    print()

    M1.modificaTuEstado(5, 6)
    print(f'M1 = ', end='')
    M1.muestraTuEstado()
    print()

    print('M1')
    M1.pideleAlUsuarioTuEstado()
    print('M2')
    M2.pideleAlUsuarioTuEstado()
    print()

    M4 = M1+M2
    M5 = M1-M2
    M6 = M1*M2
    M7 = M1/M2

    print(f'M1+M2 = {M4}')
    print(f'M1-M2 = {M5}')
    print(f'M1*M2 = {M6}')
    print(f'M1/M2 = {M7}')
