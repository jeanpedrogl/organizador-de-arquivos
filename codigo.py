import re
import os
import shutil
import sys


def organizar(path):
    # muda o diretório para a pasta downloads
    os.chdir(path)

    # compila o regex para encontrar o nome do arquivo e isolá-lo junto com a extenção
    regex_find = re.compile(r'^(.*\.(\w+))$')

    # lista todos os arquivos + pastas
    arquivos = os.listdir()

    # isola os arquivos
    todos = []
    for arquivo in arquivos:
        encontrado = regex_find.search(arquivo)
        try:
            todos.append(encontrado.groups())
        except AttributeError:
            pass

    # isola todas as extenções únicas
    extencoes = []
    for cada in todos:
        if cada[1] not in extencoes:
            extencoes.append(cada[1])

    # cria as pastas individuais para cada extencao
    for extencao in extencoes:
        try:
            os.mkdir(extencao)
        except FileExistsError:
            print('Pasta ja existe')
        else:
            print(f'Pasta {extencao} criada')

    # move os arquivos para suas respectivas pastas
    for item, extencao in todos:
        shutil.move(item, extencao)
        print(f'Item {item} movido para a pasta {extencao}')
    print('\n\nDiretório organizado.\n')


if __name__ == '__main__':
    argumentos = sys.argv
    if len(argumentos) == 2:
        print(f'Organizando caminho {argumentos[1]}.')
        try:
            organizar(argumentos[1])
        except FileNotFoundError:
            print(f'O caminho "{argumentos[1]}" não foi encontrado.')
