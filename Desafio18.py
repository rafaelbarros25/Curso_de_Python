# Crie um programa q leia um angulo qq e mostre na tela o valor do seno, conseno e tangente desse angulo.
import math
ang=float(input("Digite um angulo qualquer: "))
sen= math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tan= math.tan(math.radians(ang))
print("O seno de {} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}".format(ang, sen,cos,tan))
