# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e cada dicionário em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com as mulheres
# D) Uma lista com as pessoas com idade acima da média
pessoas = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}; ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')