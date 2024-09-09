# Crie um programa q simule o funcionamento de um caixa eletronico
#primeiro pergunte ao usuario qual o valor a ser sacado(inteiro) e o programa vai informar qtas cedulas de cada valor serao entregues
# considere q o caixa possui cedulas de 50 , 20 , 10 e 1
valor=int(input("Qual valor a ser sacado? R$ "))
ced50=valor//50
restode50=valor%50
ced20=restode50//20
restode20=restode50%20
ced10=restode20//10
restode10=restode20%10
ced1=restode10//1
print(f"Para o valor de R${valor} sacado, vc irá receber {ced50} cédulas de R$50.00, {ced20} cédulas de R$20.00, {ced10} cédulas de R$10.00 e {ced1} cédulas de R$1.00")


