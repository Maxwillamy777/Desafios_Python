def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalnum():
            print(f'ERRO: \"{entrada}" é um preço inválido!')
        else:
            valido = True
            return float(entrada)
