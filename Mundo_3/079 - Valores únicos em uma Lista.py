# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o valor já exista, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Adicionado...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
