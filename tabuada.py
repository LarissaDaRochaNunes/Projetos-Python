#Programa para calcular a tabuada de um número digitado pelo usuário
n1=int(input("Digite um número para descobrir sua tabuada: "))
a=0
resultado=0
for a in range(0,11):
    resultado=n1*a
    print("{} X {} = {}".format(n1,a,resultado))