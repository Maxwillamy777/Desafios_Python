from datetime import date
n = int(input('Qual é seu ano ou qualquer outro para saber de é bissexto!: '))#Digitar 0 vai dar o ano atual !
n2 = (n//4) * 4 - n
n3 = (n//100) * 100 - n
n4 = (n//400) * 400 - n
n5 = n2 - n3 - n4
if n == 0:
    n = date.today().year
if n5 >= 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano é bissexto !')
else:
    print('O ano não é bissexto !')