# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
print('-=' * 15)
print('Digite 999 para parar')
print('-=' * 15)
n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))