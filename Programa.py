import subprocess
import Clases.ClasePunto2D

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    A = Clases.ClasePunto2D.Punto2D(1, -2)
    B = Clases.ClasePunto2D.Punto2D(-3, 4)

    C = Clases.ClasePunto2D.add(A, B)
    E = A+B
    G = A.__add__(B)
    D = Clases.ClasePunto2D.sub(A, B)
    F = A-B
    H = A.__sub__(B)

    print(f'{A} + {B} = {C}')
    print(f'{A} - {B} = {D}')
    print()
    print(f'{A} + {B} = {E}')
    print(f'{A} - {B} = {F}')
    print()
    print(f'{A} + {B} = {G}')
    print(f'{A} - {B} = {H}')
    print()
