import minhas_funcoes
from random import randint

while True:
    operacao = int(input('Menu:\n'
                         '1 - Somar\n'
                         '2 - Subtrair\n'
                         '3 - Sair\n'
                         'Escolha uma opção: '))

    match operacao:
        case 1:
            resultado = minhas_funcoes.somar(
                randint(1, 5), randint(1, 5))
            print(f'A soma foi {resultado}\n')
        case 2:
            resultado = minhas_funcoes.subtrair(
                randint(1, 5), randint(1, 5))
            print(f'A subtração foi {resultado}\n')
        case 3:
            break
        case _:
            print(f'Opção inválida. Escolha uma opção\n')
