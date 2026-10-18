# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, tangente))