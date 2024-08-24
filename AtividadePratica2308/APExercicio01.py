"""Escreva um programa que recebe,
pelo console, uma sequencia de números
separados por vírgula e gera uma lista e uma tupla
contendo todos estes números.

Entrada: 34,67,55,33,12,98"""


# Recebe a entrada do usuário (sequência de números separados por vírgula)
entrada = input("Digite uma sequência de números separados por vírgula: ")

# Divide a entrada em uma lista usando a vírgula como separador
lista_numeros = entrada.split(',')

# Converte a lista em uma tupla
tupla_numeros = tuple(lista_numeros)

# Imprime a lista e a tupla
print(lista_numeros)
print(tupla_numeros)
