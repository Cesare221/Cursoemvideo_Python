# Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante à função
# input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')