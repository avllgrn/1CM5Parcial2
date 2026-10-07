import subprocess
import random

def esNumérico(caracter):
    x = ord(caracter)
    return 48<=x and x<=57

def esMayúscula(caracter):
    x = ord(caracter)
    return 65<=x and x<=90

def esMinúscula(caracter):
    x = ord(caracter)
    return 97<=x and x<=122

def esLetra(caracter):
    x = ord(caracter)
    return (65<=x and x<=90) or (97<=x and x<=122)

def esCaracterEspecial(caracter):
    x = ord(caracter)
    return not (48<=x and x<=57) and not (65<=x and x<=90) or (97<=x and x<=122)

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    for i in range(10):
        caracter = chr(random.randrange(33, 127))
        if esNumérico(caracter):
            print(f'{caracter} ES numérico')
        else:
            print(f'{caracter} NO es numérico')

        if esMayúscula(caracter):
            print(f'{caracter} ES mayúscula')
        else:
            print(f'{caracter} NO es mayúscula')

        if esMinúscula(caracter):
            print(f'{caracter} ES minúscula')
        else:
            print(f'{caracter} NO es minúscula')

        if esLetra(caracter):
            print(f'{caracter} ES letra')
        else:
            print(f'{caracter} NO es letra')

        if esCaracterEspecial(caracter):
            print(f'{caracter} ES caracter especial')
        else:
            print(f'{caracter} NO es caracter especial')
        print()
