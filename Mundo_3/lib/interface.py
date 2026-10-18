def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for indice, item in enumerate(lista, start=1):
        print(f'{indice} - {item}')
    print(linha())
    return leiaInt('Sua opção: ')
