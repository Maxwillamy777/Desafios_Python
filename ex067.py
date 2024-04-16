n = 1
n2 = 0
print('-' * 30)
print('The multiplication table!')
print('-' * 30)
while True:
    print('=' * 30)
    n = int(input('whats is your number to show the your multiplication table: '))
    print('=' * 30)
    if n < 0:
        break
    for n2 in range (1, 11):
        t = n * n2
        print(f'{n} x {n2} = {t}')
print('Programa encerrado !')
