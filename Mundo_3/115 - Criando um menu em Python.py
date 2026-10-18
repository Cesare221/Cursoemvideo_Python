from lib import arquivo, interface


ARQUIVO_DADOS = 'cursoemvideo.txt'


def main():
    if not arquivo.arquivoExiste(ARQUIVO_DADOS):
        arquivo.criarArquivo(ARQUIVO_DADOS)

    while True:
        resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
        if resposta == 1:
            arquivo.lerArquivo(ARQUIVO_DADOS)
        elif resposta == 2:
            interface.cabecalho('NOVO CADASTRO')
            nome = input('Nome: ').strip()
            idade = interface.leiaInt('Idade: ')
            arquivo.cadastrar(ARQUIVO_DADOS, nome, idade)
        elif resposta == 3:
            interface.cabecalho('Saindo do sistema... Até logo!')
            break
        else:
            print('\033[0;31mERRO: opção inválida.\033[m')


if __name__ == '__main__':
    main()
