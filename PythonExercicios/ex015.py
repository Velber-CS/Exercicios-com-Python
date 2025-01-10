#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos KM o carro percorreu? "))
dias = int(input("Por quantos dias ele foi alugado? "))

custoDia = 60.00
custoKm = 0.15

valorCobrado = (custoKm * km) + (custoDia * dias)

print("O carro rodou {}km, e foi alugado por {} dias. Considerando os dados, será cobra um valor de R${:.2f}".format(km, dias, valorCobrado))
