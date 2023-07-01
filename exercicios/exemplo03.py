# with open('teste.txt', 'r', encoding='utf-8') as file_object:
#     conteudo = file_object
#     print(conteudo)

path = 'teste.txt'

with open(path, 'r', encoding='utf-8') as file_object:
    for file_line in file_object:
        if 'Ir' in file_line:
            print(f'Tipo: {type(file_line)} | {file_line.rstrip()}')
