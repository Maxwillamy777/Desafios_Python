def ficha(nu='',gu=0):
    print(40 * '~')
    if nu=='':
        nu = ('<< Desconhecido >>')
    print(f'O jogado {nu} fez {gu} gol(s) na temporada.')


print(40 * '~')
n = (str(input('Jogador: ')))
g=(str(input('Gols:  ')))
if g.isnumeric():
    g = int()
else:
    g = 0
if n.strip() == '':
    ficha(gu=g)
else:
    ficha(n,g)