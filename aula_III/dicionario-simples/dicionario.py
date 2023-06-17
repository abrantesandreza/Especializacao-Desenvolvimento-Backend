# Definição de um dicionário
professor = {
    'nome': 'Messias',
    'idade': 36
}

aluno = {
    'nome': 'Andreza',
    'idade': 27
}

#print(professor['nome'])
#print(professor['idade'])
#print(aluno['nome'])
#print(aluno['idade'])

professores = {
    'Messias': {
        'idade': 36,
        'disciplinas': ['Introdução', 'Java']},
    'Wuldson': {
        'idade': 53,
        'disciplinas': ['BD I', 'BD II']}
}

print(f'O professor Messias tem {professores["Messias"]["idade"]} anos e ministra as disciplinas'
      f' de {professores["Messias"]["disciplinas"]}')

# Adicionando novos dados
professores['Messias']['email'] = 'mrafaelbatista@gmail.com'
professores['Messias']['cpf'] = '000.000.000-00'

print(professores['Messias'])
print(f'O professor Messias tem {professores["Messias"]["idade"]} anos e '
      f'ministra a disciplina de {professores["Messias"]["disciplinas"][1]}'
      f' e possui o cpf {professores["Messias"]["cpf"]}')

# Adicionando endereço
professores['Messias']['endereco'] = {
    'Rua': 'Central',
    'Bairro': 'Bessa',
    'Cidade': 'João Pessoa'
}

print(professores['Messias'])
print(f'O professor Messias tem {professores["Messias"]["idade"]} anos e '
      f'ministra a disciplina de {professores["Messias"]["disciplinas"][1]}'
      f' e possui o cpf {professores["Messias"]["cpf"]} e reside em {professores["Messias"]["endereco"]["Bairro"]}')

# Removendo valores
del professores['Messias']['cpf']
print(professores['Messias'])

# Tipos primitivos: int, float, string, boolean
# Tipos novos: lista, tupla, dicionário
