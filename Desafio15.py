# Escreva um programa q pergunte a quantidade de Km rodados por um carro e a qtd de diass alugados.
# Calcule o preco a pagar, sabendo q o carro custa R§60.00 por dia e R$ 0.15 por kn rodado.
km=float(input("Digite q quantidade de kms rodados: "))
dias=float(input("Digite a quantidade de dias alugados: "))
preco = (0.15*km)+(60*dias)
print("O preco total a pagar, com {}km percorridos e alugando por {:.0f} dias é {}".format(km,dias,preco))

