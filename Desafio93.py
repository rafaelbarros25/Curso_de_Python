#faça um programa q gerencie o aproveitamento de um jogador de futebol.
# o programa vai ler o nome, qtas partidas ele jogou, qtos golss marcou em cada partida.
# no final, tudo sera guardado em um dicionario, incluindo o total de gols.
relatorio={}
gols=[]
total=0
relatorio['Nome']=str(input('Nome: '))
relatorio['N de Partidas']=npartidas=int(input(f'Quantas partidas {relatorio["Nome"]} jogou? '))
for c in range(1, npartidas+1):
    gols.append(int(input(f'     Quantos gols {relatorio["Nome"]} marcou na {c} partida? ')))
relatorio['Gols']=gols
relatorio['Total de Gols']=total=sum(gols)

print('*-'*30)
print(relatorio)
print('*-'*30)
for k, v in relatorio.items():
    print(f'O campo {k} tem o valor {v}')
print('*-'*30)
print(f'O jogador {relatorio["Nome"]} jogou {npartidas} partidas.')

for i, v in enumerate(gols):
    print(f'     Na {i+1} partida, {relatorio["Nome"]} marcou {v} gols')
print(f'{relatorio["Nome"]} marcou um total de {total} gols')
print('*-'*30)

print(relatorio)
print(gols)



