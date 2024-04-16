v = int(input('Digite um valor: '))
print(' Agora escolha um conversor através do número, para seu valor  , abaixo !')
print(' 1 para binário')
print(' 2 para octal ')
print(' 3 para hexadecimal')
e = int(input('Então , qual conveçor voce deseja: '))
if e == 1:
    a = (v/2) * 1 and 0
    print('Seu número {} e a sua converção {}'.format(v, a))
