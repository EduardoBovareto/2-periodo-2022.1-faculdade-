# qtd = int(input('Informe a quantidade e valores:'))
# i = qtd
# intervalo = []

# while i != 0:
#   number = int(input('O valor:'))  
#   intervalo.append(number)
#   i = i - 1 
# print(intervalo, end="  ")
# print(' Este é o nosso array!')
# #Podemos colcoar if e elif para os numero que podem ou nao estar dentro de um intervalo...

espaco = "true"
Vmax = float(input('Digite um valor de range máximo:'))
Vmin = float(input('Digite um valor de range mínimo:'))
Numeros = []
while espaco != "":
  valor = int(input('Digite um valor'))
  
  if (valor > Vmin) and (valor < Vmax):
    print('\nValor digitado esta de acordo com o range: {} - {}'.format(Vmin, Vmax))
    Numeros.append(valor)
    espaco = input('\nDeseja continuar ? [true] / [" "]')
  
  else:
    print('\n Seu valor digitado se encontra errado, digite um novo:\n\n')
    valor = int(input('\nDigite um valor'))
    Numeros.append(valor)
    
print('\nEste é o seu array construído: ', Numeros)