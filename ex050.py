soma = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        count += 1
print('Voce informou {} números PARES e a soma foi {}'.format(count, soma))
