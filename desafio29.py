# Escreva um programa q leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre a msg dizendo q ele foi multado.
# A multa vai custar £7.00 por cada km acima do limite.

vel=float(input("Qual a velocidade do carro? "))
if vel > 80.0:
    print("Vc foi multado.")
    multa=(vel-80)*7
    print("Sua multa é de {:.2f} reais.".format(multa))
else:
    print("vc nao foi multado.")
