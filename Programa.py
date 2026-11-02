import subprocess

def genero1(genero):
    if genero == 'f':
        return 'femenino'
    elif genero == 'F':
        return 'femenino'.upper()
    elif genero == 'm':
        return 'masculino'
    elif genero == 'M':
        return 'masculino'.upper()
    else:
        return 'Género no reconocido...'

def genero2(genero):
    if genero == 'f' or genero == 'F':
        return 'femenino'.capitalize()
    elif genero == 'm' or genero == 'M':
        return 'masculino'.capitalize()
    else:
        return 'Género no reconocido...'

def genero3(genero):
    match genero:
        case 'f':
            return 'femenino'
        case 'F':
            return 'femenino'.upper()
        case 'm':
            return 'masculino'
        case 'M':
            return 'masculino'.upper()
        case _:
            return 'Género no reconocido...'

def genero4(genero):
    match genero:
        case 'f'|'F':
            return 'femenino'.capitalize()
        case 'm'|'M':
            return 'masculino'.capitalize()
        case _:
            return 'Género no reconocido...'

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    print('genero1(genero)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', genero1(genero) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('genero2(genero)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', genero2(genero) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('genero3(genero)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', genero3(genero) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('genero4(genero)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', genero4(genero) )
    print()
