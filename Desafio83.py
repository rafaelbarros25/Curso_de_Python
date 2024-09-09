# crie um programa onde o usuario digite uma expressao matematica q use parenteses e seu app
# #devera analisar se a expressao esta com os parenteses abertos e fechados na ordem correta
lista=[]
expressao=str(input("Digite a expressão matematica: "))
for c in expressao:
    lista.append(c)
abertos=lista.count("(")
fechados=lista.count(")")
if abertos == fechados:
  print("Sua expressão está correta")
else:
    print("Sua expressão está errada.")

