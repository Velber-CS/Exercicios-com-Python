# Calculando Seno, Cosseno e Tangente

import math

angulo = int(input("Digite o valor do ângulo: "))
rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print("O valor do seno é {}, do cosseno é {} e da tangente é {}".format(seno, cosseno, tangente))