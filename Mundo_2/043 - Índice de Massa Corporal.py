# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é a sua altura? (m) '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')