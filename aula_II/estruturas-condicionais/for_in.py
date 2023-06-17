# Definição de uma tupla
dimensoes = (200, 50)
frutas = (200, 50, 100, 1500, 3245)

# Utilizamos um For
for dimensao in dimensoes:
    print(dimensao)
# Percorrendo uma tupla
for abacate in frutas:
    print(abacate)
# Percorrendo outra tupla
for i in frutas:
    print(f'Neste ciclo o valor de i é {i}')

# Alterando o valor de uma tupla - forma incorreta
# dimensoes[0] = 123456

# Sobescrevendo o valor
dimensoes = (400, 20)
