from random import randint

list_num = []
for i in range(100):
    num_aleatorio = randint(0, 1000)
    print(f'O número escolhido foi: {num_aleatorio}')
    list_num.append(num_aleatorio)

print(list_num)
