# crie um programa onde o usuario possa digitar varios valores numericos e cadatre-os em uma lista.
# caso o numero ja exista la dentro, ele nao sera adicionado.
# No final serao exibidos todos os valores digitados em ordem crescente.

lista = []
while True:
    valor=int(input("Digite um valor: "))
    if valor in lista:
        int(input("Valor duplicado, digite novamente: "))
    else:
        lista.append(valor)
    cont=str(input("Quer continuar? (S/N): ")).strip().upper()[0]
    if cont=="N":
        break
lista.sort()
print(lista)
