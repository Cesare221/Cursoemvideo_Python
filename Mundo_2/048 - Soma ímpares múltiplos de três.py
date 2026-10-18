# Faça um programa que calcule a soma entre todos os números que são múltiplos de 3
# e que se encontram no intervalo entre 1 e 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} valores solicitados é {}'.format(cont, soma))
