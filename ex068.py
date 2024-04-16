import random
from time import sleep
computador = player = 0
PAR = IMPAR= 1
h = 0
print('-' * 30)
print('GAME PAR OR IMPAR!')
print('-' * 30)
while True:
    computador= random.randint(1,10)
    player = str(input('Whats you´ll choose Par or impar: ')).upper()
    if player == 'PAR':
        c = int(input('Choose a number: '))
        f = c + computador
        l = (f/2)*2-f
        if l == 0:
            print('AVAILABLE!')
            sleep(2)
            print('The soma deu {} logo deu par,YOU WIN!')
            h += 1
        else:
            break
    elif player == 'IMPAR':
        c = int(input('Choose a number: '))
        f = c + computador
        l = f % 3
        if l == 0:
            print('AVAILABLE!')
            sleep(2)
            print(f'The soma deu {f} logo deu ímpar,YOU WIN!')
            h += 1
        else:
            break
print('AVAILABLE!')
sleep(2)
print(f'The computer won and the your quantized of victories is {h}' )












