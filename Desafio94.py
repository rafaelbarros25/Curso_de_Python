#faça um programa q leia nome, sexo e idade de varias pessoas.
# guarde os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
#no final mostre:
#a- Total de pessoas cadastradas
#b- media de idade do grupo
#c-lista com todas as mulhers
#d lista com todas as pessoas com idade acima da media
dados={}
listadedados=[]
mulheres=[]
idade=0
total=0
while True:
    dados.clear()
    dados['Nome']=str(input('Nome: '))
    while True:
        dados['Sexo']=str(input('Sexo (M/F): ')).strip().upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    listadedados.append(dados.copy())
    total=total+1
    idade=idade+dados['Idade']
    #if dados['Sexo']=='F':
    #mulheres.append(dados['Nome'])
    while True:
        cont = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if cont=='N':
        break
print('-='*30)
media=idade/total
print(f'A) Foram cadastradas {total} pessoas.') # poderia tb ao inves de fazer total + 1, calcular pelo len da listadadedados.
print(f'A) Foram cadastradas {len(listadedados)} pessoas.')
print(f'B) A média de idade do grupo é {media:.2f} anos')
print('C) As mulheres cadastradas foram: ', end='')
for p in listadedados:
    if p['Sexo'] == 'F': #analisou cada dicionario dentro da lista e se tivesse mulher imprime o nome
        print(p["Nome"], end='')
print()
print(f'D) Lista das pessoas que estão acima da média de idade:')
for p in listadedados:
    if p['Idade']>=media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end ='')
