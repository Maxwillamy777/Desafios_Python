print('''Analyzing the women´s Brasileirão championship!''')
times = 'PAL','GRE','CAM','FLA','BOT','RBB','FLU','CAP','INT','FOR','SÃO','COR','CRU','VAS','BAH','SAN','GOI','CFC','AME'
print(f'Os 5 primeiros colocados: {times[0:5]}')
print(f'Os 4 últimos colocados da tabela: {times[15:20]}')
print(f'OS times em ordem alfabetica: {sorted(times)}')
print(f'A posição do Vasco está em {times.index("VAS") + 1}.°')
