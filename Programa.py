import subprocess
import Clases.ClaseComplejo

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    C1 = Clases.ClaseComplejo.Complejo()
    print(f'C1 = {C1}')
    print('C1 = ',end='')
    C1.muestraTuEstado()
    print()

    C1.pideleAlUsuarioTuEstado()
    print(f'C1 = {C1}')
    print('C1 = ',end='')
    C1.muestraTuEstado()
    print()

    C2 = Clases.ClaseComplejo.Complejo(1, -2)
    print(f'C2 = {C2}')
    print('C2 = ',end='')
    C2.muestraTuEstado()
    print()

    C3 = Clases.ClaseComplejo.Complejo(3)
    print(f'C3 = {C3}')
    print('C3 = ',end='')
    C3.muestraTuEstado()
    print()

    C3.modificaTuEstado(4, -5)
    print(f'C3 = {C3}')
    print('C3 = ',end='')
    C3.muestraTuEstado()
    print()
