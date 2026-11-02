import subprocess

def generoEstadoCivil1(genero, estadoCivil):
    if genero == 'f':
        if estadoCivil == 's':
            return 'soltera'
        elif estadoCivil == 'S':
            return 'Soltera'
        elif estadoCivil == 'c':
            return 'casada'
        elif estadoCivil == 'C':
            return 'Casada'
        elif estadoCivil == 'd':
            return 'divorciada'
        elif estadoCivil == 'D':
            return 'Divorciada'
        elif estadoCivil == 'v':
            return 'viuda'
        elif estadoCivil == 'V':
            return 'Viuda'
        else:
            return 'Estado civil no reconocido, femenino'
    elif genero == 'F':
        if estadoCivil == 's':
            return 'solterA'
        elif estadoCivil == 'S':
            return 'SolterA'
        elif estadoCivil == 'c':
            return 'casadA'
        elif estadoCivil == 'C':
            return 'CasadA'
        elif estadoCivil == 'd':
            return 'divorciadA'
        elif estadoCivil == 'D':
            return 'DivorciadA'
        elif estadoCivil == 'v':
            return 'viudA'
        elif estadoCivil == 'V':
            return 'ViudA'
        else:
            return 'Estado civil no reconocido, FEMENINO'
    elif genero == 'm':
        if estadoCivil == 's':
            return 'soltero'
        elif estadoCivil == 'S':
            return 'Soltero'
        elif estadoCivil == 'c':
            return 'casado'
        elif estadoCivil == 'C':
            return 'Casado'
        elif estadoCivil == 'd':
            return 'divorciado'
        elif estadoCivil == 'D':
            return 'Divorciado'
        elif estadoCivil == 'v':
            return 'viudo'
        elif estadoCivil == 'V':
            return 'Viudo'
        else:
            return 'Estado civil no reconocido, masculino'
    elif genero == 'M':
        if estadoCivil == 's':
            return 'solterO'
        elif estadoCivil == 'S':
            return 'SolterO'
        elif estadoCivil == 'c':
            return 'casadO'
        elif estadoCivil == 'C':
            return 'CasadO'
        elif estadoCivil == 'd':
            return 'divorciadO'
        elif estadoCivil == 'D':
            return 'DivorciadO'
        elif estadoCivil == 'v':
            return 'viudO'
        elif estadoCivil == 'V':
            return 'ViudO'
        else:
            return 'Estado civil no reconocido, MASCULINO'
    else:
        if estadoCivil == 's':
            return 'soltero, Género no reconocido'
        elif estadoCivil == 'S':
            return 'Soltero, Género no reconocido'
        elif estadoCivil == 'c':
            return 'casado, Género no reconocido'
        elif estadoCivil == 'C':
            return 'Casado, Género no reconocido'
        elif estadoCivil == 'd':
            return 'divorciado, Género no reconocido'
        elif estadoCivil == 'D':
            return 'Divorciado, Género no reconocido'
        elif estadoCivil == 'v':
            return 'viudo, Género no reconocido'
        elif estadoCivil == 'V':
            return 'Viudo, Género no reconocido'
        else:
            return 'Estado civil no reconocido, Género no reconocido'

def generoEstadoCivil2(genero, estadoCivil):
    if genero == 'f' or genero == 'F':
        if estadoCivil == 's' or estadoCivil == 'S':
            return 'Soltera'
        elif estadoCivil == 'c' or estadoCivil == 'C':
            return 'Casada'
        elif estadoCivil == 'd' or estadoCivil == 'D':
            return 'Divorciada'
        elif estadoCivil == 'v' or estadoCivil == 'V':
            return 'Viuda'
        else:
            return 'Estado civil no reconocido, Femenino'
    elif genero == 'm' or genero == 'M':
        if estadoCivil == 's' or estadoCivil == 'S':
            return 'Soltero'
        elif estadoCivil == 'c' or estadoCivil == 'C':
            return 'Casado'
        elif estadoCivil == 'd' or estadoCivil == 'D':
            return 'Divorciado'
        elif estadoCivil == 'v' or estadoCivil == 'V':
            return 'Viudo'
        else:
            return 'Estado civil no reconocido, Masculino'
    else:
        if estadoCivil == 's' or estadoCivil == 'S':
            return 'Soltero, Género no reconocido'
        elif estadoCivil == 'c' or estadoCivil == 'C':
            return 'Casado, Género no reconocido'
        elif estadoCivil == 'd' or estadoCivil == 'D':
            return 'Divorciado, Género no reconocido'
        elif estadoCivil == 'v' or estadoCivil == 'V':
            return 'Viudo, Género no reconocido'
        else:
            return 'Estado civil no reconocido, Género no reconocido'

def generoEstadoCivil3(genero, estadoCivil):
    if (genero == 'f' or genero == 'F') and (estadoCivil == 's' or estadoCivil == 'S'):
        return 'Soltera'
    elif (genero == 'f' or genero == 'F') and (estadoCivil == 'c' or estadoCivil == 'C'):
        return 'Casada'
    elif (genero == 'f' or genero == 'F') and (estadoCivil == 'd' or estadoCivil == 'D'):
        return 'Divorciada'
    elif (genero == 'f' or genero == 'F') and (estadoCivil == 'v' or estadoCivil == 'V'):
        return 'Viuda'
    elif (genero == 'f' or genero == 'F'):
        return 'Estado civil no reconocido, Femenino'
    elif (genero == 'm' or genero == 'M') and (estadoCivil == 's' or estadoCivil == 'S'):
        return 'Soltero'
    elif (genero == 'm' or genero == 'M') and (estadoCivil == 'c' or estadoCivil == 'C'):
        return 'Casado'
    elif (genero == 'm' or genero == 'M') and (estadoCivil == 'd' or estadoCivil == 'D'):
        return 'Divorciado'
    elif (genero == 'm' or genero == 'M') and (estadoCivil == 'v' or estadoCivil == 'V'):
        return 'Viudo'
    elif (genero == 'm' or genero == 'M'):
        return 'Estado civil no reconocido, Masculino'
    elif (estadoCivil == 's' or estadoCivil == 'S'):
            return 'Soltero, Género no reconocido'
    elif (estadoCivil == 'c' or estadoCivil == 'C'):
        return 'Casado, Género no reconocido'
    elif (estadoCivil == 'd' or estadoCivil == 'D'):
        return 'Divorciado, Género no reconocido'
    elif (estadoCivil == 'v' or estadoCivil == 'V'):
        return 'Viudo, Género no reconocido'
    else:
        return 'Estado civil no reconocido, Género no reconocido'

def generoEstadoCivil4(genero, estadoCivil):
    match genero:
        case 'f':
            match estadoCivil:
                case 's':
                    return 'soltera'
                case 'S':
                    return 'Soltera'
                case 'c':
                    return 'casada'
                case 'C':
                    return 'Casada'
                case 'd':
                    return 'divorciada'
                case 'D':
                    return 'Divorciada'
                case 'v':
                    return 'viuda'
                case 'V':
                    return 'Viuda'
                case _:
                    return 'Estado civil no reconocido, femenino'
        case 'F':
            match estadoCivil:
                case 's':
                    return 'solterA'
                case 'S':
                    return 'SolterA'
                case 'c':
                    return 'casada'
                case 'C':
                    return 'CasadA'
                case 'd':
                    return 'divorciada'
                case 'D':
                    return 'DivorciadA'
                case 'v':
                    return 'viuda'
                case 'V':
                    return 'ViudA'
                case _:
                    return 'Estado civil no reconocido, FEMENINO'
        case 'm':
            match estadoCivil:
                case 's':
                    return 'soltero'
                case 'S':
                    return 'Soltero'
                case 'c':
                    return 'casado'
                case 'C':
                    return 'Casado'
                case 'd':
                    return 'divorciado'
                case 'D':
                    return 'Divorciado'
                case 'v':
                    return 'viudo'
                case 'V':
                    return 'Viudo'
                case _:
                    return 'Estado civil no reconocido, masculino'
        case 'M':
            match estadoCivil:
                case 's':
                    return 'soltero'
                case 'S':
                    return 'SolterO'
                case 'c':
                    return 'casado'
                case 'C':
                    return 'CasadO'
                case 'd':
                    return 'divorciado'
                case 'D':
                    return 'DivorciadO'
                case 'v':
                    return 'viudo'
                case 'V':
                    return 'ViudO'
                case _:
                    return 'Estado civil no reconocido, MASCULINO'
        case _:
            match estadoCivil:
                case 's':
                    return 'soltero, Género no reconocido'
                case 'S':
                    return 'Soltero, Género no reconocido'
                case 'c':
                    return 'casado, Género no reconocido'
                case 'C':
                    return 'Casado, Género no reconocido'
                case 'd':
                    return 'divorciado, Género no reconocido'
                case 'D':
                    return 'Divorciado, Género no reconocido'
                case 'v':
                    return 'viudo, Género no reconocido'
                case 'V':
                    return 'Viudo, Género no reconocido'
                case _:
                    return 'Estado civil no reconocido, Género no reconocido'

def generoEstadoCivil5(genero, estadoCivil):
    match genero:
        case 'f'|'F':
            match estadoCivil:
                case 's'|'S':
                    return 'Soltera'
                case 'c'|'C':
                    return 'Casada'
                case 'd'|'D':
                    return 'Divorciada'
                case 'v'|'V':
                    return 'Viuda'
                case _:
                    return 'Estado civil no reconocido, Femenino'
        case 'm'|'M':
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
                    return 'Estado civil no reconocido, Masculino'
        case _:
            match estadoCivil:
                case 's'|'S':
                    return 'Soltero, Género no reconocido'
                case 'c'|'C':
                    return 'Casado, Género no reconocido'
                case 'd'|'D':
                    return 'Divorciado, Género no reconocido'
                case 'v'|'V':
                    return 'Viudo, Género no reconocido'
                case _:
                    return 'Estado civil no reconocido, Género no reconocido'

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    g = ['f', 'F', 'm', 'M', 'x']
    eC = ['s', 'S', 'c', 'C', 'd', 'D', 'v', 'V', 'x']

    print('generoEstadoCivil1(género)\n\n')
    contador = 1
    for est in eC:
        for gen in g:
            print(f'{contador}\t{est} con {gen} es {generoEstadoCivil1(gen, est)}')
            contador += 1
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('generoEstadoCivil2(género)\n\n')
    contador = 1
    for est in eC:
        for gen in g:
            print(f'{contador}\t{est} con {gen} es {generoEstadoCivil2(gen, est)}')
            contador += 1
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('generoEstadoCivil3(género)\n\n')
    contador = 1
    for est in eC:
        for gen in g:
            print(f'{contador}\t{est} con {gen} es {generoEstadoCivil3(gen, est)}')
            contador += 1
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('generoEstadoCivil4(género)\n\n')
    contador = 1
    for est in eC:
        for gen in g:
            print(f'{contador}\t{est} con {gen} es {generoEstadoCivil4(gen, est)}')
            contador += 1
    print()
    input('Presiona Enter para continuar...')
    subprocess.run('cls', shell=True)

    print('generoEstadoCivil5(género)\n\n')
    contador = 1
    for est in eC:
        for gen in g:
            print(f'{contador}\t{est} con {gen} es {generoEstadoCivil5(gen, est)}')
            contador += 1
    print()
