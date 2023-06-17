# perguntar ao usuario seu nome até que
# adivinhe o nome correto

# nome_guess = input('Qual o nome correto? ')
# nome_correto = 'Maria'

# while nome_correto != nome_guess:
#    print('\nVocê não acertou...Tente novamente!\n')
#    nome_guess = input('Qual o nome correto? ')
#    if (nome_correto == nome_guess):
#        print('\nParabéns! Você acertou em cheio!')

while True:
    guess = input('Digite seu nome: ')
    print('\nVocê errou, tente novamente...\n')
    if guess.lower() == 'seu nome':
        print('Agora sim... Parabéns!!')
        break
