#crie um programa q leia o peso de 5 pessoas. No final mostre o maior e o menor peso.
maior=0
menor=0
for c in range(1, 6):
    n=float(input("Digite o seu peso da {}º pessoa: ".format(c)))
    if c==1: #ele colocou isso para registrar a primeira ocorrencia e depois comparar com essa ocorrencia
        maior=n
        menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
print("O maior peso digitado foi {} e o menor peso foi {}".format(maior,menor))
