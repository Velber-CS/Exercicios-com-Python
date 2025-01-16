#Conversão de Reais para Dólares

valor = float(input("Quanto valor você tem? R$"))
dolar = 6.05

compra = valor / dolar

print("Com R${}, você pode comprar US${:.2f}".format(valor, compra))