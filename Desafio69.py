# Crie um programa q leia a idade e sexo de varias pessoas
# # A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar.
#No final mostre
#a- qtas pessoas tem mais de 18 anos
#b- qtos homens foram cadastrados
#c- qtas mulher tem menos de 20 anos
mulheres = countH = maiores = 0
while True:
    print("##### CADASTRE UMA PESSOA #####")
    idade=int(input("Digite a idade da pessoa: "))
    sexo=" "
    while sexo not in "MF":
        sexo = input("Digite o sexo dessa pessoa (M/F): ").strip().upper()[0]
    if sexo=="F" and idade<20:
        mulheres=mulheres+1
    if idade>18:
        maiores=maiores+1
    if sexo=="M":
        countH=countH+1
    print("-"*20)
    continuar=" "
    while continuar not in "SN":
        continuar=str(input("Deseja cadastrar mais pessoas? (S/N): ")).strip().upper()[0]
        print("-"*20)
    if continuar=="N":
        break
print(f"Vc cadastrou {countH} homens")
print(f"Vc cadastrou {maiores} pessoas com mais de 18 anos.")
print(f"Vc cadastrou {mulheres} mulher com menos de 20 anos.")
