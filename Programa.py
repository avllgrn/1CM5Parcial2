import subprocess

def estadoCivil1(estadoCivil):
    if estadoCivil == 's':
        return 'soltero'
    elif estadoCivil == 'S':
        return 'soltero'.upper()
    elif estadoCivil == 'c':
        return 'casado'
    elif estadoCivil == 'C':
        return 'casado'.upper()
    elif estadoCivil == 'd':
        return 'divorciado'
    elif estadoCivil == 'D':
        return 'divorciado'.upper()
    elif estadoCivil == 'v':
        return 'viudo'
    elif estadoCivil == 'V':
        return 'viudo'.upper()
    else:
        return 'Estado civil no reconocido...'

def estadoCivil2(estadoCivil):
    if estadoCivil == 's' or estadoCivil == 'S':
        return 'soltero'.capitalize()
    elif estadoCivil == 'c' or estadoCivil == 'C':
        return 'casado'.capitalize()
    elif estadoCivil == 'd' or estadoCivil == 'D':
        return 'divorciado'.capitalize()
    elif estadoCivil == 'v' or estadoCivil == 'V':
        return 'viudo'.capitalize()
    else:
        return 'Estado civil no reconocido...'

def estadoCivil3(estadoCivil):
    match estadoCivil:
        case 's':
            return 'soltero'
        case 'S':
            return 'soltero'.upper()
        case 'c':
            return 'casado'
        case 'C':
            return 'casado'.upper()
        case 'd':
            return 'divorciado'
        case 'D':
            return 'divorciado'.upper()
        case 'v':
            return 'viudo'
        case 'V':
            return 'viudo'.upper()
        case _:
            return 'Estado civil no reconocido...'

def estadoCivil4(estadoCivil):
    match estadoCivil:
        case 's'|'S':
            return 'soltero'.capitalize()
        case 'c'|'C':
            return 'casado'.capitalize()
        case 'd'|'D':
            return 'divorciado'.capitalize()
        case 'v'|'V':
            return 'viudo'.capitalize()
        case _:
            return 'Estado civil no reconocido...'

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    print('estadoCivil1(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil1(estadoCivil) )
    print()
    input('Presiona Enter para continuar...')

    print('estadoCivil2(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil2(estadoCivil) )
    print()
    input('Presiona Enter para continuar...')

    print('estadoCivil3(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil3(estadoCivil) )
    print()
    input('Presiona Enter para continuar...')

    print('estadoCivil4(género)\n\n')
    for estadoCivil in ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V','x']:
        print( estadoCivil, 'es', estadoCivil4(estadoCivil) )
    print()
