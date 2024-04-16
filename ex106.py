c = ('\033[m',         #0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'      # 6 - branco
     )
while True:
    def h(a=''):
        from time import sleep
        mostralinha(f'A acessando o manual  {a}')
        sleep(3)
        help(a)

    def mostralinha(msg):
         tam = len(msg) + 4
         print(tam * '~')
         print(f'  {msg}')
         print(tam * '~' )


    mostralinha('Sistema de ajuda PyHelp')
    resp = str(input('Função ou Biblioteca > '))
    if resp == 'fim':
        break
    else:
        h(resp)
mostralinha('Até logo!')
