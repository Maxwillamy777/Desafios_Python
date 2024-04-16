nome = str(input('Qual é seu nome completo ?: ')).strip()
d = nome.split()
print(('Seu primeiro nome é {}'.format(nome[0])))
print('Seu último nome é {}'.format(d[len(d)-1]))
