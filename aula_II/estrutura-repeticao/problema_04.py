from random import randint

list_num = []
for i in range(100):
    num_aleatorio = randint(0, 1000)
    list_num.append(num_aleatorio)

# Contador
n_impar = 0
n_par = 0

impares = []
pares = []

for numero in list_num:
    if (numero % 2) == 0:
        pares.append(numero)
        n_par += 1
    else:
        impares.append(numero)
        n_impar += 1

print(list_num)
print(pares)
print(impares)
print(f'A lista possui {n_par} números pares e {n_impar} números ímpares')
