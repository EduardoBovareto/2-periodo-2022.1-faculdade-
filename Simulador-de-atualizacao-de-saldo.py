palavra = "continuar"
# Variavel controle de while 
valorDin = float(0)
# Variavel para obtenção de valor em $
Lista_custos = []
# Array com os custos

saldo = float(input('Infome seu salário:'))
# Salário do cara e que será mudado de acordo com os custos digiados

Totalinicial = saldo 
# Variavel auxiliar para emissão de mensagem percentual de gastos

while palavra != 'Parar':
# Bloco de repetição para sempre receber os custos mediante a condição
  
  valorDin = float(input('Informe os custos: '))
  # Valor de custos
  
  saldo = saldo - valorDin
  #Atualização do saldo
  
  print('\nSaldo atual = {} \n'.format(saldo))
  # Informado o cliente sempre do saldo dele
  
  Lista_custos.append(valorDin)
  #Incrementação de valores ao Array
  
  print('\nEste é o valor de custos atual: {} \n'.format(Lista_custos))
  # Print dos custos em array (podendo ser matriz)
  
  palavra = input('Deseja continuar? [Parar/ Continuar]')
  # Condição de parada
  
  if saldo == 0:
    # Analise para terminar o while caso acabe o dinheiro, evitando dívidas
    print('O seu dinheiro acabou! Não pode gastar mais!')
    palavra = "Parar"
    
  if saldo <= ((Totalinicial * 45 ) / 100) and saldo >= ((Totalinicial * 28) / 100):
    # Condição financeira para emissão de mensagem
    
    print('\nO seu SALDO INICIAL é : {} '.format(Totalinicial))
    print('Favor analisar seus gastos, VOCÊ ATINGIU 45%')
    
 # Melhorar a condição de %, pois sempre que diminuímos um valor do total atual ele manda a msg de 45% e não é verdade pq 45% é muito mais do que se esta e tem.
    
print('O vetor com os custos feitos é: {}'.format(Lista_custos))
# Emissão dos custos totais do indivíduo

