#crie um programa q leia o sexo de uma pessoa, mas so aceita os valores M ou F.
#caso estajea errado, peça para digitar novamente ate o valor correcto
sexo="M" or "F"
sexo = str(input("Digite seu sexo (M/F): ")).upper().strip()
while sexo != "M" and sexo != "F":
    sexo=str(input("Digite novamente seu sexo (M/F): ")).upper()
print ("Obrigado")