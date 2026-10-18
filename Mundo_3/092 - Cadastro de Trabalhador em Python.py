# Crie um programa que leia Nome, Ano de Nascimento e Carteira de Trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o Ano de Contratação
# e o Salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')