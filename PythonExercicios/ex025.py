#Procurando uma string dentro de outra

nome = input("Digite seu nome completo: ").title()
if "Silva" in nome:
    print("Tem Silva no nome")
else:
    print("Não tem Silva no nome")