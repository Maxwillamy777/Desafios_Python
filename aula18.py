#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)
#galera = [['João',19],['Ana', 33],['Joaquim',13],['Maria',44]]
#print(galera[2][1])
#for p in galera:
    #print(f'{p[0]} tem {p[1]} anos de idade.')
#print(p[0])
galera = list()
dado = list()
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai = 0
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen = 0
        totmen += 1
print(f'Temos {totmai} mariores e {totmen} menores de idade.')