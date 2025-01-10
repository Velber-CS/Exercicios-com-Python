# Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ela.

item = input("Digite algo: ")
print("Você digitou: {}".format(item))
print(type(item))
print("O item é numérico?", item.isnumeric())
print("O item é alfabético?",item.isalpha())
print("O item é alfa-numérico?",item.isalnum())
print("O item só tem espaços?",item.isspace())
print("O item está em maiúculo?",item.isupper())
print("O item está em minúsculo?",item.islower())
print("O item está capitalizado?",item.istitle())