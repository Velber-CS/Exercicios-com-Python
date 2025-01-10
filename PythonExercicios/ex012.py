valorProduto = float(input("Qual valor do produto? "))
desconto = valorProduto * 0.05
valorDesconto = valorProduto - desconto

print("O produto originalmente custa R${}, com desconto de 5% o valor fica R${}".format(valorProduto, valorDesconto))