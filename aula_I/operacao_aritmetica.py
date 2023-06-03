primeiro_valor = int(input('Qual o primeiro numero? '))
segundo_valor = int(input('Qual o segundo numero? '))
operacao = input('Qual operacao deseja realizar? (+)(-)(*)(/)(**) ')

if operacao == '+':
    resultado = primeiro_valor + segundo_valor
    print(resultado)
elif operacao == '-':
    resultado = primeiro_valor - segundo_valor
    print(resultado)
elif operacao == '*':
    resultado = primeiro_valor * segundo_valor
    print(resultado)
elif operacao == '/':
    resultado = primeiro_valor / segundo_valor
    print(resultado)
elif operacao == '**':
    resultado = primeiro_valor ** segundo_valor
    print(resultado)
