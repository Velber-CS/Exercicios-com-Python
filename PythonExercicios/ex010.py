valor = float(input("Quanto valor você tem? R$"))
dolar = 3.27

compra = valor / dolar

print("Com R${}, você pode comprar US${:.2f}".format(valor, compra))