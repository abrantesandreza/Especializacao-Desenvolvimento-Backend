print("--- Iniciando o programa ---")

altura_cilindro = float(input("Qual a altura do cilindro? "))
raio_cilindro = float(input("Qual o raio do cilindro? "))
PI = 3.14

area_lateral = (2 * PI * raio_cilindro * altura_cilindro)
area_base = PI * (pow(raio_cilindro, 2))
area_cilindro = area_base + area_lateral
total_litros = area_cilindro / 3
total_latas = total_litros / 5

custo_total = total_latas * 50.0

print(f"Área Lateral: {area_lateral}")
print(f"Área base: {area_base}")
print(f"Área Cilindro: {area_cilindro}")
print(f"Total em litros: {total_litros}")
print(f"Total de Latas: {total_latas}")
print(f"O custo total da pintura será: R${custo_total:.2f}")
