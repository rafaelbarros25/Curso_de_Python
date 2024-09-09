#Crie um programa q tenha uma funçao chamada contador(), q receba tres paramentros:
# 1- inicio : de 1 ate 10, de 1 em 1
# 2- fim: de 10 ate 0, de 2 em 2
# 3- uma contagem personalizada (o usuario vai digitar o inicio o fim e e passo)


















from time import sleep
def contador(a, b, c):
    print('-='*20)
    print(f'Contar de {a} até {b} de {c} em {c}.')
    if c<0:
        c=c*-1 #desse jeito ele passa o c negativo para positivo, pois quando é negativo ele da erro
    if c==0:
        c=1

    if a < b:
        cont=a
        while cont<= b:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont=cont+c
        print('FIM!!!')
    else:
        cont=a
        while cont>=b:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont=cont-c
        print('FIM!!!')


contador(1, 10, 1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
ini=int(input('Inicio: '))
fim=int(input('Fim: '))
pas=int(input('Passo: '))
contador(ini,fim,pas)