# Arquivo: Ex110/desafio110.py
# Refaça o pacote moeda, colocando agora uma função chamada resumo(), que vai mostrar vários dados
# sobre um valor monetário
from Ex107 import moeda

p = float(input('Digite um preço: R$'))
moeda.resumo(p, 35, 30)