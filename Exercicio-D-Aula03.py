"""
Esse código lê 6 valores, e decidir qual deles é positivos, decidido isso, ele vai fazer a media entre os positivos

"""
media = 0
for i in range(6):
    digito = float(input('Informe um valor: '))
    if digito > 0:
        media = media + digito
    else:
        print(f'\nO valor digitado é negativo: {digito}\n')

media = media / 6
print(f'Este é o valor da média: {media:.1f}')
