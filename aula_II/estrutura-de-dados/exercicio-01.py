# Declarando uma lista
nomes = ['Messias', 'Verônica', 'Miguel', 'Gabriela']

print(nomes)
print(f"O tipo do dado é: {type(nomes)}")

print(f"Imprimindo a posição 0: nomes[0]")
print(f"Imprimindo a posição 3: nomes[3]")
print(f"Imprimindo a posição 1: nomes[1]")

print("--- Frutas")

frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print(frutas)
frutas[1] = 'abacate'
print(frutas)

frutas.insert(2, "morango")
frutas.insert(4, "graviola")
frutas.insert(1, "pitanga")
print(frutas)

del frutas[1]
del frutas[4]
print(frutas)

frutas.insert(5, "melancia")
indice_melancia = frutas.index("melancia")
print(indice_melancia)
indice_abacate = frutas.index("abacate")
print(indice_abacate)
frutas.remove("kiwi")
print(frutas)
print(len(frutas))
frutas.insert(2, 'abacaxi')

indice_abacaxi = frutas.index('abacaxi')
abacaxi_pop = frutas.pop(indice_abacaxi)
print(frutas)
print(f"A fruta deletada foi a: {abacaxi_pop}")
