# Arquivo: Ex109/desafio109.py
# Modifique o pacote moeda (criado nos desafios 107 e 108), adicionando novos parâmetros opcionais
# nas funções aumentar(), diminuir(), dobro() e metade()
from Ex107.moeda import moeda, aumentar, diminuir, dobro, metade

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10% de {moeda(p)}, temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13% de {moeda(p)}, temos {diminuir(p, 13, True)}')