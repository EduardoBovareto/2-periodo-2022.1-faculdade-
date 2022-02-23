number = int(input('Informe seu número de identificação:'))
horas = int(input('Informe suas horas trabalhadas:'))
s_h = float(input('Informe seu salário-hora:'))
salario = s_h * horas
print('O funcionário de identificação {},com {} horas trabalhadas tem um salário de:${}'.format(number, horas, salario))