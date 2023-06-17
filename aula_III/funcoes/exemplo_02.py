def soma(*args):
    print(f'O tipo é {type(args)}')
    print(f'A tupla é {args}')
    resultado = 0
    for i in args:
        resultado += 1

    print(resultado)

soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

def dicionario(**kwargs):
    print(f'O tipo de kwargs é {type(kwargs)}')
    print(f'`{kwargs}')

    for i in kwargs:
        print(kwargs[i])

dicionario(nome = 'Messias', idade = 36, clube = 'Vasco', camisa = 10)
