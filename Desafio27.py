# Crie um programa q leia o nome completo de uma pessoa e mostre o primeiro e ultimo.
# Ex clarissa candida Santos Rocha = Clarissa Rocha
n=str(input("Digite seu nome completo: ")).strip()
print(n)
nome = n.split()
print("O seu primeiro nome é: {}.".format(nome[0]))
print("O seu ultimo nome é: {}.".format(nome[len(nome)-1]))



