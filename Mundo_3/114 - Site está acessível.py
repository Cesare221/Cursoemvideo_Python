# Seu programa vai ter que acessar a página https://www.pudim.com.br e verificar se ela está acessível
# no momento. O programa deverá informar se o site está acessível ou não
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
    # Se você quiser ver o HTML da página:
    # print(site.read())
except urllib.error.URLError:
    print('O site PUDIM não está acessível no momento.')
else:
    print('Consegui acessar o site PUDIM agora mesmo!')