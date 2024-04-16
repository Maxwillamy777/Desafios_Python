n = 1
r = 1
i = 1
c = 0
d = 0
w = 0
print('-' * 30)
print('{:^30}'.format('Analisador de dados!'))
print('-' * 30)
while True:
    age = int(input('Whats is your age? '))
    sex = str(input('Whats is your sex male or female? ')).upper()
    per = str(input('Finished!.You want continue yes or no? ')).upper()
    if age > 18:
        c += n
        if per == 'NO':
            break
    elif sex == 'MALE':
        d += r
        if per == 'No':
            break
    elif sex == 'FEMALE' and age < 20:
        w += i
        if per == 'NO':
            break
print(f'How many people are over 18: {c}')
print(f'How many men were registered: {d}')
print(f'How many women are under 20: {w}')
