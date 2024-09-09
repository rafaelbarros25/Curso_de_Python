# Crie um programa q leia o nome e preço de varios produtos.
# o programa deve perguntar se o usuario quer continuar.
# No final mostre
# a- qual o total gasto
# b- qtos produtos custam mais de R$100.00
#c- qual o nome do produto mais barato
total=0
count = 0
menor=0
contador=0 #para contaar qtos produtos
barato=""
while True:
    nome=str(input("Digite o nome do produto: "))
    preço=int(input("Digite o preço do produto comprado: R$"))
    total=total+preço
    contador=contador+1
    if preço>100:
        count=count+1
    if contador==1: #criou essa linha para já deixa o primeiro produto como mais barato
        menor=preço
        barato=nome
    else:
        if preço<menor:
            menor=preço
            barato=nome
    continuar=" "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar (S/N)?")).strip().upper()[0]
    if continuar == "N":
        break

print (f"O valor total de produtos comprados foi de R$ {total}")
print (f"Vc comprou {count} produtos que custaram mais de R$100.00.")
print (f"O produto mais barato q voi comprou foi o/a {barato}")
