# desafio 13: faca um algoritmo q leia o salario de um funcionario e mostre novo salario com 15% de aumento.

sal = float(input("Digite seu salario atual em reais: "))
aum = sal + sal*15/100
print("O seu novo salario com aumento de 15% é {:.2f}".format(aum))
