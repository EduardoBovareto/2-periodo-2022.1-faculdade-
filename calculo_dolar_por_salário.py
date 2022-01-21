salario = float(input('Informe seu salário:'))
dollar = float(input('Cotação do dollar:'))
texto = 'DOLLAR'
print(f'\n {texto:=^20} \n R${dollar:^15} \n {texto:=^20}')
comprar = salario / dollar
print(f'\nIsso é  quanto você consegue comprar: {comprar:.2f} ')
