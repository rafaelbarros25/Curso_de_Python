# crie um programa q leia um numero inteiro e mostre na tela se ele é par ou impar.

n=int(input("Digite um numero inteiro: "))
resto=n%2
if resto == 0:
    print("É PAR")
else:
    print("É IMPAR")