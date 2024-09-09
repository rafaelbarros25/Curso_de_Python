#Crie um programa q tenha uma funçao chamada Escreva(), q receba um texto qq como parametro e mostre uma msg com tamanho adaptavel.
# exemplo:
#Olá Mundo
#---------
#Olá Mundo
#---------













def escreva(msg):
    tam=len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)


escreva('Olá tudo bem?!!!')
escreva('Vamos estudar')
escreva('Até amanha!!!')


