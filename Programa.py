import subprocess
import Clases.ClaseRectangulo

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    for base in range(-1, 2):
        for altura in range(-1, 2):
            print(f'base={base}, altura={altura}')
            C = Clases.ClaseRectangulo.Rectangulo(base, altura)
            print('C')
            print(C)
    input('Presiona Enter para continuar...\n\n')
    subprocess.run('cls', shell=True)

    for base in range(-1, 2):
        for altura in range(-1, 2):
            print(f'base={base}, altura={altura}')
            C.modificaTuEstado(base, altura)
            print('C')
            print(C)
    input('Presiona Enter para continuar...\n\n')
    subprocess.run('cls', shell=True)

    for base in range(-1, 2):
        for altura in range(-1, 2):
            print(f'base={base}, altura={altura}')
            C.base = base
            C.altura = altura
            print('C')
            print(C)
    print()
