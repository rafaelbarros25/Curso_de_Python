# crie um programa q leia o peso e altura de uma pessoa e calcule seu IMC
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25 peso ideal
# 25 a 30 sobrepeso
# 30 a 40 obesidade
# acima de 40 obesidade morbida

peso=float(input("Digite os seu peso (Kg): "))
alt=float(input("Digite sua altura em metros (m): "))
imc=peso/(alt*alt)
print("O seu IMC é de {:.2f}.".format(imc))
if imc <18.5:
    print("Voce esta ABAIXO do peso")
elif imc<25:
    print("Voce esta no peso IDEAL")
elif imc <30:
    print("Voce esta com SOBREPESO")
elif imc<40:
    print("Voce esta com OBESIDADE")
else:
    print("Voce esta com OBESIDADE MORBIDA")
