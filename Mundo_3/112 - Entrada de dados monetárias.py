# Arquivo: Ex112/desafio112.py
# Aprimore o pacote utilidadesCeV adicionando ao módulo dado uma função chamada leiaDinheiro()
# que seja capaz de validar um valor monetário
from utilidadesCeV.moeda import resumo
from utilidadesCeV.dado import leiaDinheiro

p = leiaDinheiro('Digite o preço: R$')
resumo(p, 35, 20)