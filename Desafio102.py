# Crie um programa q tenha uma funçao chamada factorial() q receba 2 parametros:
# o primeiro q indica o numero a calcular e
# o segundo chamado show, q sera um valor logico (opcional) indicando se será mostrado ou nao na tela o processo de calculo do factorial


def factorial(n, show=False): #qd mete o igual é pra avisar q caso nao inform o num será igual a 1
    """
    - Calcula o Factorial de um número.
    :param n: O número a ser calculado
    :param show: (Opcinal) - Mostrar ou não a conta
    :return: O valor do Factorial de um número n
    """
    f=1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='' )
            else:
                print(' = ', end='')
        f=f*c
    return f

n=int(input('Digite um numero: '))
print (factorial(n,show=True))
#help(factorial)

