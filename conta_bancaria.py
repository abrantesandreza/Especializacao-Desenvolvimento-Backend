deposito = float(input('Quanto gostaria de depositar? '))
saque = float(input('Quanto gostaria de sacar? '))

saldo_final = deposito - saque

if saldo_final > 0:
  print('Saldo positivo!')
else:
  valor_quitar_debito = 0 - saldo_final
  print(f'Saldo negativo! Você pode quitar seu debito pagando a quantia de R${valor_quitar_debito}')
