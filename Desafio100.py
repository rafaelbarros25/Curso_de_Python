#Crie um programa q tenha uma lista chamada numeros e duas funçoes chamadas sorteia() e somarPar().
# a primeira funçao vai sorter 5 numeros e vai coloca-los dentro da lista e a
# segunda funçao vai mostrar a soma entre todos os valores Pares sorteados pela funçao anterior
from random import randint

























def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1,10))



def somarpar(lista):
    soma=0
    for valor in lista:
        if valor % 2==0:
            soma=soma+valor
    print(f'A soma dos valores pares ´e {soma}')

numeros=[]
sorteia(numeros)
print(numeros)
somarpar(numeros)

