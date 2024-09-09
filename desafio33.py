# crie um programa q leia tres numeros e diga qual é o maior e qual é o menor
a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))
c=int(input("Digite o terceiro numero: "))
menor = a
maior=c
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
if a>b and a>c:
    maior=a
if b>a and b>c:
    maior=b
print("O maior numero é {}".format(maior))
print("O menor numero é {}".format(menor))


