evenodd = [[],[]]
for cont in range(1,8):
    num = int(input(f'Enter {cont}° number: '))
    if num % 2 == 0:
        evenodd[0].append(num)
    else:
        evenodd[1].append(num)
evenodd[0].sort()
evenodd[1].sort()
print(30 * '-=')
print(f'Numbers of even:{evenodd[0]}')
print(f'Numbers of odd:{evenodd[1]}')
