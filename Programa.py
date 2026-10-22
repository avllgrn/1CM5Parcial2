import subprocess
import Clases.ClaseCirculo

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    C = Clases.ClaseCirculo.Circulo()
    print('C')
    print(C)

    C2 = Clases.ClaseCirculo.Circulo(-1)
    print('C2')
    C2.muestraTuEstado()

    print(f'C.dameTuDiametro() -> {C.dameTuDiametro()}')
    print(f'C.dameTuArea() -> {C.dameTuArea()}')
    print(f'C.dameTuPerimetro() -> {C.dameTuPerimetro()}')
    print()
    input('Presiona Enter para continuar...\n\n\n')
    subprocess.run('cls', shell=True)

    print('(Ingresa un radio positivo)')
    print('C')
    C.pideleAlUsuarioTuEstado()
    print()

    print('C')
    print(C)
    print(f'C.dameTuDiametro() -> {C.dameTuDiametro()}')
    print(f'C.dameTuArea() -> {C.dameTuArea()}')
    print(f'C.dameTuPerimetro() -> {C.dameTuPerimetro()}')
    print()
    input('Presiona Enter para continuar...\n\n\n')
    subprocess.run('cls', shell=True)

    print('(Ingresa un radio negativo)')
    print('C')
    C.pideleAlUsuarioTuEstado()
    print()

    print('C')
    print(C)
    print(f'C.dameTuDiametro() -> {C.dameTuDiametro()}')
    print(f'C.dameTuArea() -> {C.dameTuArea()}')
    print(f'C.dameTuPerimetro() -> {C.dameTuPerimetro()}')
    print()
    input('Presiona Enter para continuar...\n\n\n')
    subprocess.run('cls', shell=True)

    print('(Si intenta modificarse el radio con un valor negativo)')
    print('C')
    C.modificaTuEstado(-1)
    print()

    print('C')
    print(C)
    print(f'C.dameTuDiametro() -> {C.dameTuDiametro()}')
    print(f'C.dameTuArea() -> {C.dameTuArea()}')
    print(f'C.dameTuPerimetro() -> {C.dameTuPerimetro()}')
    print()
