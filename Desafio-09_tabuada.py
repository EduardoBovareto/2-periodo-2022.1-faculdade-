valor = int(input('Digite um valor para saber sua tabuada:'))
mult = int(input('Até quanto quer saber os múltiplos? 10, 20 ...?'))
i = 1
for i in range(mult):
    R = valor * i
    print(f'Este é o valor de {valor} sendo multiplicado por {i} , {R} ')
m = 'Obrigado!'
print(f'\n{m:=^45}')
