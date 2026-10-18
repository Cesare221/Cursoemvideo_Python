# A confederação Brasileira de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade
from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')