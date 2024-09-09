# Um professor quer sortear a ordem de apresentacao de trabalhos dos alunos.
# Faca um programa q leia o nome dos quatro alunos e sorteie a ordem.
import random
n1=input("Digite o nome do primeiro aluno aluno: ")
n2=input("Digite o nome do segundo aluno aluno: ")
n3=input("Digite o nome do terceiro aluno aluno: ")
n4=input("Digite o nome do quarto aluno aluno: ")
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A orden de apresentacao será {}.".format(lista))