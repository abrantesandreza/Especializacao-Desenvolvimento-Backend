print('Vamos ler cada linha do livro...\n')

file_one = 'contos_dos_irmaos_grimm.txt'
file_two = 'o_principe_maquiavel.txt'
# books = file_one + file_two

with open(file_one, 'r', encoding='utf-8') as first_file_object, \
        open(file_two, 'r', encoding='utf-8') as second_file_object:
    count_line_first_book = 0
    for file_line in first_file_object:
        print(file_line.rstrip())
        count_line_first_book += 1
    count_line_second_book = 0
    for file_line in second_file_object:
        print(file_line.rstrip())
        count_line_second_book += 1
    print(f'Contagem primeiro livro: {count_line_first_book}')
    print(f'Contagem segundo livro: {count_line_second_book}')


#with open(file_one, 'r', encoding='utf-8') as first_file_object, \
#        open(file_two, 'r', encoding='utf-8') as second_file_object:
#    count_line_first_book = 0
#    for file_line in first_file_object:
#        count_line_first_book += 1
#   print(f'Contagem primeiro livro: {count_line_first_book}')

#    count_line_second_book = 0
#    for file_line in second_file_object:
#        count_line_second_book += 1
#    print(f'Contagem segundo livro: {count_line_second_book}')
