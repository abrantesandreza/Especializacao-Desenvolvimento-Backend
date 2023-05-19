qntd_maxima = int(input('Informe a quantidade maxima do estoque do produto: '))
qntd_minima = int(input('Informe a quantidade minima do estoque do produto: '))
qntd_real = int(input('Informe a quantidade real do estoque do produto: '))

media = (qntd_maxima + qntd_minima) / 2

if qntd_real < media:
    print('Precisamos de mais produto em estoque!')
elif qntd_real > media:
    print('Estamos com bastante produto em estoque!')
elif qntd_real == media:
    print('Em breve precisaremos de mais produto em estoque!')