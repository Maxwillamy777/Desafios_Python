from datetime import date
atual = date.today().year
nasc = int(input('Por favor , digite o ano de seu nascimento para saber quê categoria voce está: '))
idade = atual - nasc
if idade >= 9 and idade < 14:
    print('Categoria: Mirim')
elif idade >= 14  and idade < 19:
    print('Categoria: Infantil')
elif idade == 19:
    print('Categoria: Junior')
elif idade == 20:
    print('Categoria: Senior')
elif idade > 20:
    print('Categoria: Master')
elif idade < 9:
    print('Vc não tem idade suficiente para a sua primeira categoria !')