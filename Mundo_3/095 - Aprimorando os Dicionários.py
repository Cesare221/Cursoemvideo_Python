# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador
temp = dict()
principal = list()
gols = list()
while True:
    temp.clear()
    temp['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'   Quantas partidas {temp["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'      Quantos gols na partida {c}? ')))
    temp['gols'] = gols[:]
    temp['total'] = sum(gols)
    principal.append(temp.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in principal[0].keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(principal):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(principal):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {principal[busca]["nome"]}:')
        for i, g in enumerate(principal[busca]['gols']):
            print(f'      No jogo {i}, fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')