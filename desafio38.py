# crie um programa q leia dois numeros inteiros e compare-os, mostrando na tela um mensagem:
# O primeiro valor é maior
# o segundo valor é maior
# nao existe valos maior, os dois sao iguais
n1=int(input("Digite um numero inteiro: "))
n2=int(input("Digite um numre inteiro:"))
if n1>n2:
    print("O primeiro valor é maior")
elif n2>n1:
    print("O segundo valor é maior")
elif n1==n2:
    print("Os valores sao iguais")
