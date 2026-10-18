# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: quantas pessoas têm mais de 18 anos, quantos homens foram cadastrados
# e quantas mulheres têm menos de 20 anos
mai = homens = mulher20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        mai += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if resp == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(mai))
print('Ao todo temos {} homens cadastrados.'.format(homens))
print('E temos {} mulheres com menos de 20 anos.'.format(mulher20))