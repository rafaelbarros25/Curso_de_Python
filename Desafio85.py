#Crie um programa q o usuario digite sete valores e cadastre-os em uma unica lista q mantenha separados os valores pares e impares.
# no final mostre os valores pares e impaers em ordem crescente
# " Digite o primeiro valor: "

# no final vai ter print com duas listas q pertecem a uma unica lista
lista=[[], []] # ja criamos uma lista com 2 sub listas
for c in range(0, 7):
    valor=int(input("Digite um valor: "))
    if valor%2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[1].sort()
lista[0].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')

