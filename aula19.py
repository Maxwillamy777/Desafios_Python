#pessoas = {'nome': 'Max','sexo':'M','idade': 15}
#print(pessoas['nome'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k in pessoas.keys():
    #print(k)
#for k in pessoas.values():
 #print(k)
#del pessoas['sexo']
#pessoas['nome'] = 'Maxwell'
#pessoas['peso'] = 98.5
#for k, v in pessoas.items():
 # print(f'{k} = {v}')
#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil)
#print(brasil[1])
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
#for k, v in e.items():
#print(f'O campo {k} tem valor {v}.')





