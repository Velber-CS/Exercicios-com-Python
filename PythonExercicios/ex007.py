#Cálculo de Média e Verificação de Desempenho do Aluno

print("Cálculo de média")
n1 = int(input("Digite a nota do 1º Bimestre: "))
n2 = int(input("Digite a nota do 2º Bimestre: "))
n3 = int(input("Digite a nota do 3º Bimestre: "))
n4 = int(input("Digite a nota do 4º Bimestre: "))

media = (n1+n2+n3+n4)/4
print("A nota final foi: {}".format(media))

if media < 5:
    print("O aluno reprovou!")
elif media == 10:
    print("O aluno passou com maestria!")
else:
    print("O aluno passou!")

