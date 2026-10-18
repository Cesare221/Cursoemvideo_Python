# Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Está na hora de se alistar no serviço militar, IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))