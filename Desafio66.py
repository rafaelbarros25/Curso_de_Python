# Crie um programa q leia varios numeros inteiros pelo teclado. O programa so vai parar qd o usuario digitar 999.
# No final mostre qtos numeros foram digitados e a soma entre eles.
count=0
soma=0
while True:
    n = int(input("Digite um numero inteiro (999 para parar): "))
    if n== 999:
        break
    count=count+1
    soma=soma+n
print(f"A Soma dos {count} numeros digitados é {soma}!!!")
# o q ele fez diferente do exercicio 64 foi de agora começar com o loop infinito e meter o break qd o usuario digitar 999
# ele jogou tudo pra dentro do loop