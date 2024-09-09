#Crie um programa q tenha um Tupla totalmente preenchida com um contagem por extenso de zero até vinte.
#Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
lista=("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "desesseis", "desessete", "desoito", "desenove", "vinte")
while True:
    num=int(input("Digite um número entre 0 e 20: "))
    if num >=0 and num <=20:
        print(f"O número escolhido por extenso será {lista[num]}")
        break