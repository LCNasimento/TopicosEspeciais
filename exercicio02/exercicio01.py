import os
os.system('cls')

"""
> Elabore uma aplicação que receba o nome de um produto 
e o seu valor. O desconto deve ser calculado de acordo 
com o valor fornecido conforme a Tabela. 
> Apresente em tela o nome do produto, valor original do 
produto e o novo valor depois de ser realizado o desconto. 
Caso o valor digitado seja menor que zero, deve ser 
emitida uma mensagem de aviso. """

# Entrada de dados do usuário
nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto(R$): "))

if valor_produto > 0:
    desconto = 0
    if valor_produto >= 50 and valor_produto < 200:
        desconto = 0.95
    elif valor_produto >= 200 and valor_produto < 500:
        desconto = 0.94
    elif valor_produto >= 500 and valor_produto < 1000:
        desconto = 0.93
    elif valor_produto >= 1000:
        desconto = 0.92
           
    #Exibição Resultados
    print("\n---Resultado---")
    print(f"Produto: {nome_produto}")
    print(f"Valor Original: {round(valor_produto,2)}")
    print(f"Valor com desconto: R$ {round(valor_produto*desconto,2)}")

else:
    print("O valor do produto deve ser maior que zero!")

    

    
    
    

