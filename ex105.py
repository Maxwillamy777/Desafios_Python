def boletim(*notas, sit=False):
    """
    -> Cria um dicionario onde adiciona os valores...
    :param notas:que forma boletim que por sua vez o analisa
    :param sit:é mostra ou não a situaçã0
    :return:com retorno com objetivo de mostrar boletins diversos
    """
    analise = dict()
    analise['Total'] = len(notas)
    analise['Maior'] = max(notas)
    analise['Menor'] = min(notas)
    analise['Média'] = sum(notas) / len(notas)
    if sit:
        if analise['Média'] >= 7:
            analise['Situação'] = 'Boa'
        elif analise['Média'] >= 5:
            analise['Situação'] = 'Razoável'
        else:
            analise['Situação'] = 'Ruim'

    return analise



r2 = boletim(10,10,10,10, sit=True)
print(r2)
help(boletim)