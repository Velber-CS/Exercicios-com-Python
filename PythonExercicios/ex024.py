#Verificando as primeiras letras de um texto

cidade = input("Digite o nome de uma cidade: ").title()
cidadeSanta = cidade.split()

if cidadeSanta[0] == "Santo":
    print("A cidade {} começa com a palavra Santo".format(cidade))
else:
    print("A cidade {} não começa com a palavra Santo".format(cidade))