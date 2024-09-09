#Crie um programa q leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa progressao.
termo=int(input("Digite o primeiro de sua PA: "))
razao=int(input("Digite a razao de sua PA: "))
# para achar o decimo termo da razao ele usou uma formula, e depois jogou dentro do range
decimo=termo+(10-1)*razao
for c in range (termo, decimo, razao):
    print (c, end=" » ")