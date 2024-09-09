# crie um programa para aprovar o emprestimo bancario para compra de uma casa.
# o Programa vai perguntar o valor da casa, o salario do comprador e em qtos anos ele vai pagar.
#Calcule o valor da prestacao mensal, sabendo q ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
valor=float(input("Digite o valor da casa: R$: "))
salario=float(input("Digite o seu salario: R$ "))
duracao=float(input("Em quantos anos deseja pagar a casa? "))
prestacao=valor/(duracao*12)
if prestacao>=30*salario/100:
    print("Desculpe mas o seu credito nao foi aprovado pois a prestacao de R${:.2f} é muito alta.".format(prestacao))
else:
    print("Parabens, seu credito foi aprovado. \nO valor mensal da sua prestaçao será de R${:.2f}".format(prestacao))
