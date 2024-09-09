# crie um programa q calcule o valor a ser pago por um produto considerando o seu preço normal e a forma de pagamento:
# 1 a vista: 10% de desconto
# 2 a vista no cartao: 5% de desconto"
# 3 ate 2 x : preco normal
# 4 3x ou mais parcelas: 20% de juros
print("{:=^40}".format("LOJAS BARROCAS"))
valor=float(input("Digite o valor do produto: R$ "))
print("""FORMAS DE PAGAMENTO
[1] a vista em dinheiro ou cheque
[2] a vista no cartao
[3] ate 2x
[4] 3x ou mais parcelas""")
forma=int(input("Digite a forma de pagamento: "))
if forma == 1:
    print("O preço total a pagar será de R${:.2f}.".format(valor - (10*valor)/100))
elif forma == 2:
    print("O preço total a pagar será de R${:.2f}.". format(valor - (5*valor)/100))
elif forma == 3:
    print("O preço total a pagar será de R${:.2f}.".format(valor))
elif forma == 4:
    print("O preço total a pagar será de R${:.2f}.".format(valor + (20*valor)/100))
