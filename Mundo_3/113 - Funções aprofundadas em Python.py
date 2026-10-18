# Arquivo: Ex113/desafio113.py
# Refaça o DESAFIO 104 criando uma função chamada leiaInt() que vai funcionar de forma semelhante à função input()
# Crie também uma função chamada leiaFloat()
from utilidadesCeV.dado import leiaInt, leiaFloat

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')