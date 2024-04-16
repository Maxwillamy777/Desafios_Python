a = 'Amigo', 'Tataravo', 'Vaca', 'Quente','Santo', 'aurelio'.upper()
for p in a:
    print(f'\nNa palavra: {p} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')


