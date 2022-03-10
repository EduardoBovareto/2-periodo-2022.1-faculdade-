qtdTestes = int(input('Informe a quantidade de Testes desejados:'))
qtdValoresTeste = int(input('Informe a quantidade de valores participantes de cada teste:'))
valorMin = float(input('Informe um valor minimo dentro do intervalo:'))
valorMax = float(input('Informe o valor máximo do seu intervalo: '))
i = 1
j = 1
valor_p = []
valor_intervalo = []
valor_menor = []
valor_maior = []

for j in range(qtdTestes):
    print('\nTeste {}:'.format(i))
    print('Intervalo: [{}, {}]'.format(valorMin, valorMax))
    valor = int(input('Informe o valor dentro do intervalo:'))
    valor_p.append(valor)

    for i in range(qtdValoresTeste):
        if i == 2:
            tamanho1 = 0
            tamanho2 = 0
            tamanho3 = 0
            valor_p.clear()

        if (valor > valorMin) and (valor < valorMax):
            valor_intervalo.append(valor)
            print('E valido no intervalo')

        elif valor < valorMin:
            valor_menor.append(valor)
            print('Não é valido e esta fora do minimo')

        elif valor > valorMax:
            valor_maior.append(valor)
            print('É um valor fora do máximo')

tamanho1 = len(valor_menor)
tamanho2 = len(valor_intervalo)
tamanho3 = len(valor_maior)
print(f'Abaixo do Intervalo: {tamanho1},  No intervalo: {tamanho2},\n Acima do intervalo: {tamanho3}')

