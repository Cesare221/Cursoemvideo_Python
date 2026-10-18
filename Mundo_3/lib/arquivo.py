from pathlib import Path


def arquivoExiste(nome):
    return Path(nome).is_file()


def criarArquivo(nome):
    Path(nome).touch(exist_ok=True)


def lerArquivo(nome):
    caminho = Path(nome)
    cabecalho('PESSOAS CADASTRADAS')
    with caminho.open(encoding='utf-8') as arquivo:
        for registro in arquivo:
            pessoa, idade = registro.rstrip('\n').rsplit(';', 1)
            print(f'{pessoa:<30}{idade:>3} anos')


def cadastrar(arq, nome='desconhecido', idade=0):
    with Path(arq).open('a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade}\n')


def cabecalho(txt):
    print('-' * 42)
    print(txt.center(42))
    print('-' * 42)
