#Projeto de uma calculadora, no qual o usuário digita dois números e escolhe a operação que deseja realizar (subtração,multiplicação ou divisão), após o sitema realiza a operação e retorna o resultado.
print("-"*30)
print("CALCULADORA SIMPLES")
print("-"*30)
n1= int (input("Digite o 1° valor: "))
n2 = int (input("Digite o 2° valor: "))
while True:
    operacao = int (input ("[1] Adição \n" 
    "[2] Subtração \n" 
    "[3] Multiplicação \n" 
    "[4] Divisão \n" 
    "[5] Para sair \n"
    " Qual operação deseja realizar? \n"))
    if operacao == 1:
        soma = n1+n2
        print(f'O resultado da soma de {n1} com {n2} é igual a: {soma}')
        break
            
    if operacao == 2:
        subtracao = n1 - n2
        print(f'O resultado da subtração de {n1} por {n2} é igual a: {subtracao}')
        break
            
    if operacao == 3:
        multiplicacao = n1*n2
        print(f'O resultado da multiplicação entre {n1} e {n2} é igual a: {multiplicacao}')
        break
            
    if operacao == 4: 
        divisao = n1/n2
        print(f'O resultado da divisão entre {n1} e {n2} é igual a: {divisao}')
        break
            
    if operacao == 5:
        print("Operação cancelada")
        break
            
    else:
        print("Opção digitada inválida, tente novamente!")