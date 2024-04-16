n3 = 0
n = 0
n2 = 0
while n3 != 5:
   n = int(input('Digite o primeiro valor: '))
   n2 = int(input('Digite o segundo valor: '))
   print('Agora escolha uma das opçaoes abaixo!')
   print('[1]Somar')
   print('[2]Multiplicador')
   print('[3]Maior')
   print('[4]Novos números')
   print('[5]Sair do programa!')
   n3 = int(input('Opcão: '))
   if n3 == 1:
    r1 = n + n2
    print('{} + {} = {}! '.format(n,n2,r1))
   elif n3 == 2:
      r2 = n * n2
      print('{} * {} = {}'.format(n, n2 , r2))
   elif n3 == 3:
        if n > n2:
           print('O número maior é {}'.format(n))
        elif n2 > n:
           print('O numero maior é {}'.format(n2))
        else:
           print('Nenhum, os números são iguais !')
   elif n3 == 4:
      print('Certo !')
print('Programa encerrado !')



