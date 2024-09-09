# crie um programa q leia varios numeros inteiros pelo teclado.
# o programa para qd o usuario digitar 999.
# no final mostre qtos numeros foram digitados e qual foi a soma entre eles (desconsideando o flag)
count=0
n=0
soma=0
n = int(input("Digite um numero inteiro (999 para parar): "))
while n!= 999:
    count=count+1
    soma=soma+n
    n = int(input("Digite um numero inteiro (999 para parar): "))

print("A Soma dos numeros digitados é {}".format(soma))
print("Vc digitou {} numeros diferentes".format (count))
