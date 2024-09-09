#Crie um programa q leia nome e peso de varias pessoas e guarde numa lista.
# No final mostre:
#A- Quantas pessoas foram cadastradas
#b- uma listagems com as pessoas mais pesadas > 90kilos
#c- lista com pessoas mais leves <90kilos
#

dados=[]
pessoas=0
pesadas=[]
leves=[]
while True:
    nome=(str(input("Nome: ")))
    peso=(float(input("Peso: ")))
    dados.append(peso)
    dados.append(nome)
    pessoas=pessoas+1
    if peso>90:
        pesadas.append(nome)
    else:
        leves.append(nome)
    cont=str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if cont=="N":
        break
print(f"Foram cadastradas {pessoas} pessoas")
print(f'As pessoas acima do peso são: {pesadas}')
print(f'As pessoas leves são: {leves}')

# GUANABARA
# para contar qtas pessoas foram cadastradas ele usou o len da lista:

#print(f'Ao todo vc cadastrou {len(dados)} pessoas') # na minha soluçao a resposta é 8 pois eu criei uma só lista
# o guanabara criou uma lista dentro da outra ([[nome, peso], [nome, peso]]), entao usando o len da lista principal a resposta dele é 2

