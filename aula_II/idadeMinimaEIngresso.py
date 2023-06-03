print("--- Iniciando o programa ---")

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você não pode entrar na festa!")
else:
    tipo_ingresso = input("Ingresso VIP ou Pista? ")
    tipo_ingresso = tipo_ingresso.upper()

    if tipo_ingresso == "VIP":
        print("Siga para o primeiro andar...")
    elif tipo_ingresso == "PISTA":
        print("Siga pelo corredor...")
    else:
        print("Seu ingresso não é válido!")

print("--- Finalizando o programa ---")
