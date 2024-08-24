"""Escreva um programa que recebe dois
números inteiros (i,j) e gera um array 2D. O valor
de i é referente as linhas e j as colunas.

Entrada: 3,5"""


# Recebe as dimensões da matriz do usuário
i = int(input("Digite o número de linhas (i): "))
j = int(input("Digite o número de colunas (j): "))

# Cria uma matriz 2D (lista de listas) preenchida com zeros
matriz = [[0 for _ in range(j)] for _ in range(i)]

# Preenche a matriz com os valores desejados
for x in range(i):
    for y in range(j):
        matriz[x][y] = x * y

# Imprime a matriz resultante
print(matriz)