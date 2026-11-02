import subprocess
from Clases.ClaseFecha import Fecha

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    F = Fecha()
    print(f'Año bisiesto {F}')
    for mes in range(14):
        for dia in range(33):
            F.modificaTuEstado(dia, mes, 2024)
            print(f'dia={dia}, mes={mes}\t{F}')
        print()
    print()
    subprocess.run('pause', shell=True)
    print()

    print(f'Año NO bisiesto {F}')
    F.modificaTuEstado(1,1,2025)
    for mes in range(14):
        for dia in range(33):
            F.modificaTuEstado(dia, mes, 2025)
            print(f'dia={dia}, mes={mes}\t{F}')
        print()
    print()
