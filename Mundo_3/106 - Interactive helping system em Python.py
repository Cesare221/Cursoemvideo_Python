# Vamos criar nosso próprio manual de Python? Seu programa terá que simular o funcionamento do comando help(),
# usado diretamente no shell do Python. O usuário vai digitar um comando e o manual vai mostrar como se usa
# esse tipo de comando
from time import sleep


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print('\033[33m', end='')
    help(com)
    print('\033[m')
    sleep(2)


def título(msg, cor=0):
    cores = {0: '\033[m',
             1: '\033[30;41m',
             2: '\033[30;42m',
             3: '\033[30;43m',
             4: '\033[30;44m',
             5: '\033[30;45m',
             6: '\033[30;46m',
             7: '\033[30;47m'}
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print('\033[m', end='')


# Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        título('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)