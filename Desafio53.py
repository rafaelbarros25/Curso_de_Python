# crie um programa q leia uma frase qq e diga se ela é um palindromo, desconsiderando os espaços.
frase=str(input("Digite um frase: ")).strip().upper() #leu a frase, ja cortou os esçapos e jogou tudo pra maiusculo
palavras=frase.split() # separou as palavras para criar uma lista
junto= "".join(palavras) # eliminou os espaços para juntar todas as palavras
inverso = "" #criou o inverso vazio
for letra in range(len(junto) -1, -1, -1): #começou da ultima letra, q ele pegou da len -1 (pois as posiçoes começam do 0) ate a primeira letra (q seria 0), mas meteu -1 pq nao pega a ultima, o ultimo -1 foi para ir de traz pra frente.
    # print(junto[letra]) # mandou print do junto na lista letra
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print("A frase digitada é um palindromo")
else:
    print("A frase digitada nao é um palindromo")