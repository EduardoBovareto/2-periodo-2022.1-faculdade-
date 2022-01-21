"""
Os métodos em questão abaixo, são somente para manipulação de strings,
 com números já convertidos, não funciona
"""

entrada = input('Escreva alguma informação: ')
print(type(entrada))
print('O que você digitou pode ser convertido em números ? ', entrada.isnumeric())
print('O que você digitou em comparação a palavras é: ', entrada.isalpha())
print('A informação dentro do diagrama alpha numérico é:  ', entrada.isalnum())

nome = input('Fale seu nome, do modo que desejar: ')
print('Verificação de caixa alta: ', nome.isupper())
print('Verificação de caracter todo e caixa baixa ', nome.islower())
print('Prazer: ', nome.capitalize())
# A linha 15 coloca a primeira letra do seu nome em caixa alta, isso se chama palavra capitalizada aqui e pra isso
# tem um metodo de verificação: variavel.istitle()
# As variáveis usadas com os métodos no código são nossos objetos

numero = (input('Digite um número: '))
print('Isso é um número? ', numero.isnumeric())
print('Corresponde a tabela ASCII? ', numero.isascii())

# print(format(nome).isnumeric())
