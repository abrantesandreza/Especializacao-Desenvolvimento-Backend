print("--- Iniciando o programa ---")

ano_nascimento = int(input("Qual o ano do seu nascimento? "))
ano_atual = 2023
idade = ano_atual - ano_nascimento

if 16 <= idade <= 18:
    print(f"Você tem {idade} anos, você pode votar, mas ainda não pode dirigir! Calma!")
elif idade >= 18:
    print(f"Você tem {idade} anos e pode votar e dirigir!")
else:
    print(f"Você tem {idade} anos e não pode votar e dirigir!")
    