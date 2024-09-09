#crie um programa q leia a idade, nome e sexo de 4 pessoas. No final mostre:
# a media de idade de todos
# o nome do homem mais velho
# qtas mulheres tem menos de 20 anos
total=0
velho=0
mulheres=0
nomevelho=""
for c in range(1, 5):
    print("{:=^40}".format("{}º PESSOA".format(c)))
    nome=str(input("Digite o seu nome: "))
    idade=int(input("Digite a sua idade: "))
    sexo=str(input("Digite o seu sexo(M/F): ")).upper()
    total=idade+total
    media=total/c
    if sexo=="F":
        if idade<20:
            mulheres=mulheres+1
    if sexo=="M":
        if c==1:
            velho=idade
            nomevelho=nome
        else:
            if idade>velho:
                velho=idade
                nome=nomevelho
print("A média de idade de todas as pessoas é de {}".format(media))
print("O nome do homem mais velho é {}".format(nomevelho))
print("Há {} mulher(es) com menos de 20 anos de idade".format(mulheres))
