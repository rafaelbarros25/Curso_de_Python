# aprimore o exercicio anterior, mostrando no final:
# soma dos valores pares
# soma dos valores da terceira coluna
# o maior valor da segunda linha

matriz = [[0,0,0], [0,0,0],[0,0,0]] # ele ja criou as matrizes com a estruta e com elementos 0 paa depois ir substituindo.
spar=maior=scol=0
for l in range(0,3): #criou l para linha e c para coluna
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range (0,3): # esse outro for é para mostrar a estrutura na tela
    for c in range (0,3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c]%2==0:
            spar=spar+matriz[l][c] #para fazer a soma dos valores pares ele analisou a entrada de cada valor
    print() #toda vez q ele terminar um for, ele vai quebrar a linha
print('-='*30)
print(f'A soma dos elementos pares é {spar}')
for l in range(0,3):
    scol=scol+matriz[l][2] # para fazer a soma dos elementos da terceira coluna ele analisou a entrada dos elementos da terceira coluna [l][2] o [2] é fixo pois ja se sabe q é a terceira coluna
print(f'A soma dos elementos da terceira coluna é {scol}')
for c in range(0,3):
    if c==0:
        maior=matriz[1][c] # o [1] é fixo pois ele esta analisando apenas os elementos da segunda coluna
    elif matriz [1][c]>maior:
        maior=matriz[1][c]
print (f'O maior valor da segunda linha é {maior}')



