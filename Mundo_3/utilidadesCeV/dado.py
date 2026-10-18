import math


def leiaDinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
        except ValueError:
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
            continue
        if math.isfinite(valor):
            return valor
        print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')


def leiaInt(msg):
    while True:
        entrada = input(msg).strip()
        try:
            return int(entrada)
        except ValueError:
            print(f'\033[0;31mERRO: "{entrada}" não é um número inteiro válido.\033[m')


def leiaFloat(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
        except ValueError:
            print(f'\033[0;31mERRO: "{entrada}" não é um número real válido.\033[m')
            continue
        if math.isfinite(valor):
            return valor
        print(f'\033[0;31mERRO: "{entrada}" não é um número real válido.\033[m')
