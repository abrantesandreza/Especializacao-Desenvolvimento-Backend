diretorio = 'teste\\'
arquivo = 'arquivo02.txt'
file_path = diretorio + arquivo

with open(file_path, 'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(conteudo)
