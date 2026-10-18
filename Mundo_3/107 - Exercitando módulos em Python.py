# Arquivo: Ex107/desafio107.py
# Baixe a documentação do Python e procure o pacote chamado "random".
# Você vai descobrir como gerar valores aleatórios e pode criar um pequeno pacote de funções úteis.
from Ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')