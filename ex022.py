n = str(input('Qual é seu nome completo ?:')).strip()
print('Seu nome completo em maiúscula:', n.upper())
print('Seu nome completo em minúscula:', n.lower())
print('O número de letras : {}'.format(len(n) - n.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n.find('  ')))
separa = n.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))


