#crie um programa q um tupla unica com nomes dos produtos e preços.
#no final mostre uma listagem de preços organizando os dados em forma tabular
listagem=("Lapis", 3, "Caneta", 4, "Caderno", 6, "Livro", 12, "Grampeador", 8, "Canetinhas", 10)
print(listagem)
for pos in range(0,len(listagem)):
    if pos%2==0:
        print (f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")

    # a parte mais complicada desse desafio foi a formataçao de terxto,
    #