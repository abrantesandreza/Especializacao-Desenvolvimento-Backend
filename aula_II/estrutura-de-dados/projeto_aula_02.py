# condição para cada função
# 1 - Adicionar pessoas
# 2 - Pesquisar uma pessoa
# 3 - Listar os nomes
# 4 - Remover uma pessoa da lista
# 5 - Alterar
# 5 - Parar o programa

lista = []

while True:

    print("\n1 - Adicionar\n"
          "2 - Pesquisar\n"
          "3 - Listar os nomes\n"
          "4 - Remover uma pessoa da lista\n"
          "5 - Alterar\n"
          "6 - Encerrar o programa\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome_pessoa = input("Digite o nome da pessoa: ")
        lista.append(nome_pessoa)
    elif opcao == 2:
        nome_pesquisa = input("Digite o nome que deseja pesquisar: ")
        if nome_pesquisa in lista:
            print(f"O nome {nome_pesquisa} está na lista")
        else:
            print("Nome não encontrado.")
    elif opcao == 3:
        for nome in lista:
            print(f'-> {nome}')
    elif opcao == 4:
        nome_remover = input("Quem você quer remover? ")
        if nome_remover in lista:
            lista.remove(nome_remover)
        else:
            print("Nome não encontrado.")
    elif opcao == 5:
        pesquisar_nome = input("Quem você quer alterar? ")
        if pesquisar_nome in lista:
            print(f"O nome {pesquisar_nome} foi encontrado.")
            nome_alterado = input("Digite o novo nome: ")
            posicao_nome = lista[lista.index(pesquisar_nome)] = nome_alterado
            print("O nome foi alterado com sucesso!")
        else:
            print("O nome não foi encontrado!")
    elif opcao == 6:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida!")
        print("Tente novamente!!")
