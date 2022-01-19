information = input('Digite alguma coisa: ')
print('É um número? ', format(information).isnumeric())
print('É uma informação vazia? ', format(information).isspace())
print('É uma informação capitalizada? (com a primeira letra em capslock)', format(information).istitle())
