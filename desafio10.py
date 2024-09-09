# desafio 10: crie um programa q leia qto dinheiro ela tem e mostre qtos dolares ela pode comprar. Considere 1 dolar = 3.27
din = input("Quantos dinheiro vc tem em reais? ")
dol = float(din)/3.27
print("Com {} reais, voce consegue comprar {:.2f} dolares:".format(din,dol))

