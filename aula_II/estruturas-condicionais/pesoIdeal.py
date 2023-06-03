print("--- Iniciando o programa ---")
sexo = input("Qual o seu sexo? M/F ").lower()
altura = float(input("Qual a sua altura? "))

if sexo == "m":
    pesoIdeal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {pesoIdeal:0.2f}kg')
elif sexo == "f":
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {pesoIdeal:0.2f}kg')
else:
    print("Entrada inválida!")

print("--- Finalizando o programa ---")
