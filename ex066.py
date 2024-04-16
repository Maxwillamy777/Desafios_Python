n = 1
t = 1
soma = 0
s = 0
while True:
    n = int(input(f'Digite {t}° número: '))
    t += 1
    s += 1
    if n == 999:
        break
    else:
        soma += n
s -= 1
print(f'A quantidade de números somados: {s} e o seu resultado: {soma}.')


