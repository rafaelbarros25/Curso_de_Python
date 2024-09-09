#Soluçao do Guanabara, Des 84
dados=[]
temp=[]
maior=menor=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(dados)==0:
        maior=menor=temp[1]    # ele pegou o primeiro peso (posiçao 1) para afirma q é o maior e menor dado para depois comparar com os futuros dados registrados
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]
    dados.append(temp[:]) # para cada dado registrado (nome e peso ele insere numa lsita principal)
    temp.clear() # e depois apaga a lista temp para começar outra
    resp=str(input('Quer continuar: (S/N) '))
    if resp in 'nN':
        break
print('-='*30)
print(f'Ao todo vc cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in dados:
    if p[1]==maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso for de {menor}Kgs. Peso de ', end='')
for p in dados:
    if p[1]==menor:
        print(f'{p[0]} ', end='')
print()
