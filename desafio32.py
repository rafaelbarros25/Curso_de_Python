# crie um programa q leia um ano qq e mostre se ele é bissexto.
ano=int(input("Digite um ano: "))
if ano%4 ==0 and ano%100 !=0 or ano%400==0:
    print("O ano {} é bisexto".format(ano))
else:
    print("O ano {} nao é bisexto".format(ano))

# adicionei ano%100 !=0 or ano%400==0: pq para ser ano bissexto tem mais regras