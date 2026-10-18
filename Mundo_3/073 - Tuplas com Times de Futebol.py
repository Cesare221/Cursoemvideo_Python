# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Lista de times do 5 primeiros colocados
# b) Os últimos 4 colocados da tabela
# c) Lista de times em ordem alfabética
# d) Em que posição na tabela está o time da Chapecoense
times = ('Palmeiras', 'Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo',
         'Fluminense', 'Grêmio', 'Athletico-PR', 'Santos', 'Corinthians',
         'Bragantino', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza',
         'Bahia', 'Vasco', 'Chapecoense', 'Goiás', 'Botafogo')
print('-=' * 30)
print('Lista de times do Brasileirão: ', times)
print('-=' * 30)
print('Os 5 primeiros colocados são: ', times[0:5])
print('-=' * 30)
print('Os últimos 4 colocados são: ', times[-4:])
print('-=' * 30)
print('Times em ordem alfabética: ', sorted(times))
print('-=' * 30)
print('O Chapecoense está na {}ª posição'.format(times.index('Chapecoense')+1))