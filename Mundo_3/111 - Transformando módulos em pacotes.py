# Organize as funções monetárias no pacote utilidadesCeV.
from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite um preço: R$')
moeda.resumo(p, 80, 35)
