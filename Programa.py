import subprocess

def muestraASCII():
    for i in range(256):
        print(f'{i}\t{chr(i)}')

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    muestraASCII()
