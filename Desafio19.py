# Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faca um programa q ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
n1=input("Digite o nome do primeiro aluno aluno: ")
n2=input("Digite o nome do segundo aluno aluno: ")
n3=input("Digite o nome do terceiro aluno aluno: ")
n4=input("Digite o nome do quarto aluno aluno: ")
lista = [n1,n2,n3,n4]
escolhido=random.choice(lista)
print("O aluno escolhido foi {}.".format(escolhido))


