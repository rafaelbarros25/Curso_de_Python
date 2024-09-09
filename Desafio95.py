# aprimore o desafio 93 para q ele funcione com varios jogadores
#
#Nome do jogador:
#Quantas partidas XX jogou:
#Quantos gols na primeira partida:
#Quantos gols na segunda partida:
#Quer continuar: (S/N):
#Mostrar dados de qual jogador?
relatorio={}
listadejogadores=[]
gols=[]
total=0
while True:
    relatorio.clear()
    relatorio['Nome']=str(input('Nome: '))
    relatorio['N de Partidas']=npartidas=int(input(f'Quantas partidas {relatorio["Nome"]} jogou? '))
    gols.clear()
    for c in range(1, npartidas+1):
        gols.append(int(input(f'     Quantos gols {relatorio["Nome"]} marcou na {c} partida? ')))
    relatorio['Gols']=gols[:]
    relatorio['Total de Gols']=total=sum(gols)
    listadejogadores.append(relatorio.copy())
    while True:
        cont = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if cont == 'N':
        break
print('*-'*30)
print('Cod ', end='') # esse codigo é para fazer o cabeçalho
for i in relatorio.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(listadejogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca==999:
        break
    if busca >=len(listadejogadores):
        print(f'ERRO! Não existe jogador com esse código {busca}')
    else:
        print(f'---LEVANTAMENTO DO JOGADOR {listadejogadores[busca]["Nome"]}:')
        for i, g in enumerate(listadejogadores[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<VOLTE SEMPRE>>')