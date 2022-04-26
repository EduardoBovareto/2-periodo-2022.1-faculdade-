def SomaDosnPrimeiros(numero):
    qtd = numero
    soma = 0
    for i in range(1, qtd + 1): # Percorrer cada laço fazendo a soma e a conta
        soma = (i*(i + 1)) / 2 # formula
    return ('O resultado da função s() em n primeiros termos é:', soma)
print(SomaDosnPrimeiros(3))
        # Se s(3) == 1 + 2 + 3 == 6
    
