num =int(input('Digite um número para mostrar a sua tabuada:  '))
valor = 0
for c in range(0, 10):
      valor += 1
      base = valor * num
      print('{} * {} = {}'.format(num, valor,  base))


     
