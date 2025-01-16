#Calculando a hipotenusa de um triângulo retângulo

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))
