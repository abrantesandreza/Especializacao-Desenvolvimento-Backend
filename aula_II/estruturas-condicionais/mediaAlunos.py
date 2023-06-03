print("---Iniciando o cálculo da média---")
nota1 = float(input("Qual a sua primeira nota? "))
nota2 = float(input("Qual a sua segunda nota? "))
nota3 = float(input("Qual a sua terceira nota? "))
nota4 = float(input("Qual a sua quarta nota? "))

ma = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A sua média é {ma:0.2f}')

if ma >= 7.0:
    print("Você foi aprovado!")
else:
    print("Você ainda não foi aprovado!")
