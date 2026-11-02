import subprocess
from Clases.ClaseHora import Hora

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    F = Hora()
    for hora in range(-7, 34, 10):
        for minuto in range(-1, 80, 20):
            for segundo in range(-1, 80, 20):
                F.modificaTuEstado(hora, minuto, segundo)
                print(f'hora={hora}, minuto={minuto}, segundo={segundo}\t{F}')
            print()
        print('\n')
