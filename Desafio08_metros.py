m = 'METROS'
print(f'Conversor de unidade\n{m:=^30}')
value = float(input('Informe  o valor na unidade metros'))
cm = value * 100
mm = value * 1000
print(f'O seu valor em {m} \n  corresponde a: \n {cm} cm\n{mm} mm')
# Manipular os dados depois para aparecer com vírgula