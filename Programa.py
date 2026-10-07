import subprocess

def estadoCivil1(estadoCivil):
    if estadoCivil == 's':
        return 'soltero'
    elif estadoCivil == 'S':
        return 'SOLTERO'
    elif estadoCivil == 'c':
        return 'casado'
    elif estadoCivil == 'C':
        return 'CASADO'
    elif estadoCivil == 'd':
        return 'divorciado'
    elif estadoCivil == 'D':
        return 'DIVORCIADO'
    elif estadoCivil == 'v':
        return 'viudo'
    elif estadoCivil == 'V':
        return 'VIUDO'
    else:
        return 'Estado Civil no reconocido...'

def estadoCivil2(estadoCivil):
    if estadoCivil == 's' or estadoCivil == 'S':
        return 'Soltero'
    elif estadoCivil == 'c' or estadoCivil == 'C':
        return 'Casado'
    elif estadoCivil == 'd' or estadoCivil == 'D':
        return 'Divorciado'
    elif estadoCivil == 'v' or estadoCivil == 'V':
        return 'Viudo'
    else:
        return 'Estado Civil no reconocido...'

def estadoCivil3(estadoCivil):
    match estadoCivil:
        case 's':
            return 'soltero'
        case 'S':
            return 'SOLTERO'
        case'c':
            return 'casado'
        case 'C':
            return 'CASADO'
        case 'd':
            return 'divorciado'
        case 'D':
            return 'DIVORCIADO'
        case 'v':
            return 'viudo'
        case 'V':
            return 'VIUDO'
        case _:
            return 'Estado Civil no reconocido...'

def estadoCivil4(estadoCivil):
    match estadoCivil:
        case 's'|'S':
            return 'Soltero'
        case 'c'|'C':
            return 'Casado'
        case 'd'|'D':
            return 'Divorciado'
        case 'v'|'V':
            return 'Viudo'
        case _:
            return 'Estado Civil no reconocido...'

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    print('estadoCivil1(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil1(estadoCivil) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('estadoCivil2(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil2(estadoCivil) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('estadoCivil3(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil3(estadoCivil) )
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('estadoCivil4(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil4(estadoCivil) )
    print()
