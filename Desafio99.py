#Crie um programa q tenha uma funçao chamada maior(), q receba varios paramentro com valores inteiros
# o programa tem q analisar todos os elementos e mostrar qual foi o maior.
from time import sleep


















def maior(*num):
    cont = maior= 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont=cont+1
    print(f'Foram analisados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')





maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()