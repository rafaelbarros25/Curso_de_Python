# crie um programa q pergunte o salario de um funcionario e calcule o valor do seu aumento.
# para salarios superiores a £1250.00 o aumento de 10%.
# para salarios inferioes a £1250.00 aumento de 15%.

salario=float(input("Digite seu salario atual: "))
if salario >1250.00:
    aumento=salario*10/100
else:
    aumento=salario*15/100
novo=salario+aumento
print ("Vc tera um aumento de {:.2f} reais, e seu novo salario sera de {:.2f} reais.". format(aumento,novo))
