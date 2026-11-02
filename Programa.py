import subprocess
import Clases.ClaseMonomio

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    M1 = Clases.ClaseMonomio.Monomio()
    print(f'M1 = {M1}')
    print('M1 = ',end='')
    M1.muestraTuEstado()
    print()

    M1.pideleAlUsuarioTuEstado()
    print(f'M1 = {M1}')
    print('M1 = ',end='')
    M1.muestraTuEstado()
    print()

    M2 = Clases.ClaseMonomio.Monomio(1, -2)
    print(f'M2 = {M2}')
    print('M2 = ',end='')
    M2.muestraTuEstado()
    print()

    M3 = Clases.ClaseMonomio.Monomio(3)
    print(f'M3 = {M3}')
    print('M3 = ',end='')
    M3.muestraTuEstado()
    print()

    M3.modificaTuEstado(4, -5)
    print(f'M3 = {M3}')
    print('M3 = ',end='')
    M3.muestraTuEstado()
    print()
