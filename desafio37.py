# crie um programa q leia um numero inteiro qq e peça para o usuario escolher qual sera a basa de conversao:
# 1 para binario
# 2 para octal
# 3 para hexadecimal
num=int(input("Digite um numero inteiro: "))
print("""Escolha uma das bases para conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
# ele meteu 3 aspas para fazer essa quebra de opçoes
opcao=int(input("Digite sua opçao: "))
if opcao == 1:
    print("{} convertido para BINáRIO é igual a {}.".format(num,bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}.".format(num,oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}.".format(num,hex(num)[2:]))
#ele colocou [2:] para fatiar a resposta, pois a resposta vem com o codigo da base de conversao

