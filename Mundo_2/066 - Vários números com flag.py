# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('A soma dos {} valores foi {}.'.format(cont, soma))