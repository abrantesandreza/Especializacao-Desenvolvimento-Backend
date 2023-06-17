def calculadora(n1, n2):
    resultado_soma = n1 + n2
    resulado_subtracao = n1 - n2
    resultado_multiplicacao = n1 * n2
    resultado_divisao = n1 / n2

    return resultado_soma, resulado_subtracao, resultado_multiplicacao, resultado_divisao

# print(calculadora(10, 20))
soma, subtracao, multiplicacao, divisao = calculadora(10, 20)

print(f'Soma: {soma}')
print(f'Subtracao: {subtracao}')
print(f'Multiplicacao: {multiplicacao}')
print(f'Divisao: {divisao}')
