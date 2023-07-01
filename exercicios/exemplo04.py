print('--- Iniciando o programa ---')
user_option = input('Qual a permissão? \n0 para sem permissão | 1 para com permissão: ')

directory = 'teste\\'
file = 'arquivo03.txt'
path = directory + file

with open(path, 'r', encoding='utf-8') as file_object:
    for line_object in file_object:
        if line_object[0] == user_option:
            print(line_object[4:].rstrip())
