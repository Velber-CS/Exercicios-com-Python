from math import ceil

altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area = altura * largura
print("Sua parede tem a dimensão de {:.2f}x{:.2f}".format(altura, largura))
print("A área da parede é de {}m²".format(area))

tintaLitro = 2
pintura = ceil(area/tintaLitro)

print("Para pintar a parede toda, é necessário {:.2f} litros de tinta".format(pintura))