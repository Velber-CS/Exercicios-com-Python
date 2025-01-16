#Conversão de Temperatura

c = float(input("Digite a temperatura em celsius (ºC): "))
k = c + 273.15
f = (c * 9/5) + 32

print("{}ºC é {:.1f}ºF e {:.2f}K".format(c, f, k))