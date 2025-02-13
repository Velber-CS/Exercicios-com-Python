#Manipulação de strings: Maiúsculas, Minúsculas e Contagem de Caracteres em um Nome

nome = input("Digite seu nome completo: ").strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
primeiroNome = nome.split()
print(len(primeiroNome[0]))