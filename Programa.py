import subprocess

def género1(género):
    if género == 'f':
        return 'femenino'
    elif género == 'F':
        return 'FEMENINO'
    elif género == 'm':
        return 'masculino'
    elif género == 'M':
        return 'MASCULINO'
    else:
        return 'Genero no reconocido...'

def género2(género):
    if género == 'f' or género == 'F':
        return 'Femenino'
    elif género == 'm' or género == 'M':
        return 'Masculino'
    else:
        return 'Genero no reconocido...'

def género3(género):
    match género:
        case 'f':
            return 'femenino'
        case 'F':
            return 'FEMENINO'
        case 'm':
            return 'masculino'
        case 'M':
            return 'MASCULINO'
        case _:
            return 'Genero no reconocido...'

def género4(género):
    match género:
        case 'f'|'F':
            return 'Femenino'
        case 'm'|'M':
            return 'Masculino'
        case _:
            return 'Genero no reconocido...'

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    print('género1(género)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', género1(genero) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('género2(género)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', género2(genero) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('género3(género)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', género3(genero) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('género4(género)\n\n')
    for genero in ['f', 'F', 'm', 'M', 'x']:
        print( genero, 'es', género4(genero) )
    print()
