from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador: int = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada?  '))
print('Jo')
sleep(1)
print('KEN')
sleep(1)
print('PÕ!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
       print('Empate')
    elif jogador==1:
        print('jogador vence!')
    elif jogador ==2:
        print('Co utador vence!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador ==0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada inváli')









