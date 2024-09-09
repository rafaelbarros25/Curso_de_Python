# crie um programa onde o usuario insira 5 valores numericos e cadastre em uma lista.
#Ja na posiçao correta de inserçao (sem usar o sort()).
# No final mostre a lista ordenada na tela.
#"Digite um valor"
# Adicionado ao final da lista
# Adicionado na posição 0
# Adicionado na posição 1
num=[]
for c in range (0,5):
    new = int(input("Digite um valor: "))
    if c==0: #n ==0 é referente a posiçao 0, ou seja, qd n for o primeiro valor lido
        num.append(new)
        print (f"Adicionado ao final da lista")
    elif new>num[len(num)-1]: # se o numero digitado for maior q o ultimo valor na lista ele vai adicionar na ultima posiçao q pode ser lida com a lenght - 1.
        num.append(new)
        print (f"Adicionado ao final da lista")
    else:
        pos=0
        while pos < len(num): #ele vai da posiçao 0 ate a ultima posiçao
            if new<=num[pos]: #ele vai verificar em cada posiçao se o numero q quer inserir é menor ou igual a ele
                num.insert(pos,new)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos=pos+1
print(f"Os valores digitados em ordem foram {num}")

#ele foi lendo os valores e analisando onde deve entrar, por isso usou os 3 "if"