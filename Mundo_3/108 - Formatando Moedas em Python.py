# Arquivo: Ex108/desafio108.py
# Aprimore o pacote moeda que fizemos no desafio 107, adicionando uma função chamada moeda()
# que mostra um valor como uma moeda
from Ex107.moeda import moeda

p = float(input('Digite um valor: R$'))
print(f'A metade de {p} é {moeda(p/2)}')
print(f'O dobro de {p} é {moeda(p*2)}')