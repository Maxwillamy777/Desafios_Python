def voto(n):
    from datetime import datetime
    age =  datetime.now().year - n
    print(f'Com {age} anos:',end='')
    if  60 > age >= 18 :
        print(' VOTO OBRIGATÓRIO.')
    elif age >= 60:
        print(' VOTO OPCIONAL.')
    elif age < 18:
        print(' VOTO NEGADO.')

print(40 * '~')
nasc = int(input(('Em que ano voce nasceu? ')))
voto(nasc)



