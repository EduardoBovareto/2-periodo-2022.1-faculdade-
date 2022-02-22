"""
Esse código vai ler 3 palavras e definir que tipo é esse animal, através de parâmetros estabelecidos com condições, ao
final vai dizer qual é o ser vivo.
Teremos variáveis:
    forma == se é vertebrado ou invertebrado (X2)
    classe == se é ave, mamífero, inseto, anelídeo (X4)
    alim == se é carnívoro, onívoro, herbívoro ou hematófago (X4)
Os tipos estão em colchetes só para visualização do usuário.


Vale ressaltar que as perguntas ao usuário podem ser respectivas ao que a cara escolher,
se o cara escolher vertebrado, só devem aparecer opções de vertebrados.(no futuro)

"""
forma = input('Informe a forma do animal: [Vertebrado] [Invertebrado] ')
classe = input('Informe a classe do animal: [ave], [mamífero], [ inseto], [anelídeo]')
alim = input('Informe a sua alimentação: [carnívoro], [onívoro], [herbívoro], [hematófago]')

if forma == 'vertebrado':
    if classe == 'ave':
        if alim == 'carnívoro':
            print('É UMA ÁGUIA')

        else:
            print('É UM POMBO E É ONÍVORO')

    if classe == 'mamífero':
        if alim == 'onívoro':
            print('É um HOMEM !')

        else:
            print('É uma VACA!')
else:

    if forma == 'invertebrado':
        if classe == 'inseto':
            if alim == 'hematófago':
                print('É uma PULGA!')

            else:
                print('É uma LAGARTA!')

        if classe == 'anelídeo':
            if alim == 'hematófago':
                print('É uma SANGUESSUGA !')
            else:
                print('É uma MINHOCA!')
