"""

Código lê um DDD pelo usuário, e dependendo do DDD, printaremos uma cidade.

Futuramente, colocar um if-else para confirmar o DDD

"""
digitos = int(input('Informe seu DDD de sua região:'))

if (digitos > 1) and (digitos < 100):
    verifica = input('Seu DDD está correto?')
    if verifica == 'nao':
        digitos = int(input('Digite novamente:'))
    else:
        print('Seu DDD é {}'.format(digitos))

    if digitos == 61:
        print('Sua cidade é Brasilia')

    elif digitos == 71:
        print('Sua cidade é Salvador ')

    elif digitos == 11:
        print('Sua cidade é São paulo ')

    elif digitos == 21:
        print('Sua cidade é Rio de Janeiro ')

    elif digitos == 32:
        print('Sua cidade é Juiz de Fora ')

    elif digitos == 19:
        print('Sua cidade é Campinas ')

    elif digitos == 27:
        print('Sua cidade é Vitoria')

    elif digitos == 31:
        print('Sua cidade é Belo Horizonte')

    else:
        print('Favor emitir um número válido')
else:
    print('Informe um valor de DDD valido')
