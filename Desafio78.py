# crie um programa q leia 5 valores numericos e os guarde numa lista.
# no final mostre o maior e o menos valor ad lista, mostrando suas posiçoes na lista.

#Digite um valor para a Posição 0:
# O maior valor digitado foi X, na posição X

num=[]
maior=0
for n in range (0,5):
    valor=int(input(f"Digite um valor para posiçao {n}: "))
    num.append(valor)
print (f"O maior valor digitado foi {max(num)}, na posição {num.index(max(num))}")
print (f"O menor valor digitado foi {min(num)}, na posição {num.index(min(num))}")