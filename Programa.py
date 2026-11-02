import subprocess
import Clases.ClaseComplejo

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    C1 = Clases.ClaseComplejo.Complejo()
    C2 = Clases.ClaseComplejo.Complejo(7, 8)
    C3 = Clases.ClaseComplejo.Complejo(9)

    print(f'C1 = {C1}')
    print(f'C2 = {C2}')
    print(f'C3 = {C3}')
    print()

    C1.modificaTuEstado(5, 6)
    print(f'C1 = ', end='')
    C1.muestraTuEstado()
    print()

    print('C1')
    C1.pideleAlUsuarioTuEstado()
    print('C2')
    C2.pideleAlUsuarioTuEstado()
    print()

    C4 = C1+C2
    C5 = C1-C2
    C6 = C1*C2
    C7 = C1/C2

    print(f'C1+C2 = {C4}')
    print(f'C1-C2 = {C5}')
    print(f'C1*C2 = {C6}')
    print(f'C1/C2 = {C7}')
