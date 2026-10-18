# Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# A) Quantidade de notas
# B) A maior nota
# C) A menor nota
# D) A média da turma
# E) A situação (opcional)
def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas) / len(notas)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 1.5, 9.9, sit=True)
print(resp)
help(notas)