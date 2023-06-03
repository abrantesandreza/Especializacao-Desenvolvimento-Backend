qntd_macas = int(input('Quantas maças deseja comprar? '))
preco_unidade_maca = 1.37
preco_unidade_maca_desconto = 1.24

if qntd_macas < 12:
    valor_total = qntd_macas * preco_unidade_maca
    print(valor_total)
else:
    valor_total = qntd_macas * preco_unidade_maca_desconto
    print(valor_total)
