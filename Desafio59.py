# crie um programa q leia 2 valores e mostre o menu na tela:
# 1- somar, 2 multiplicar, 3 maior (mostrar qual o maior), 4 novos numeros, 5 sair do programa
# seu programa devera realizar a opearçao solicitada em cada caso.
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))
opçao=0
while opçao !=5:
    print("""Suas opções: 
[1] Somar
[2] Multiplicar
[3] Mostrar o Maior valor 
[4] Digitar novos números 
[5] Sair do programa""")
    opçao=int(input("O que pretende fazer: "))
    if opçao == 1:
        resultado=valor1+valor2
        print("A soma entre os valores é de {}".format(resultado))
    elif opçao ==2:
        resultado=valor1*valor2
        print("O produto entre os valores é de {}".format(resultado))
    elif opçao ==3:
        if valor1<valor2:
            maior=valor2
        else:
            maior=valor1
        print("O maior valor digitado foi de {}".format(maior))
    elif opçao ==4:
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
    else:
        print("Valor incorreto. Digite novamamente.")
if opçao == 5:
    print("Obrigado")

