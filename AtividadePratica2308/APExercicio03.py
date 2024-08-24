"""Escreva um programa que recebe
sequencia de palavras separados por vírgula e
apresenta na tela as palavras ordenadas.

Entrada: Carlos, Ana, Maria, Francisco, João"""


# Recebe a entrada do usuário (sequência de palavras separadas por vírgula)
entrada = input("Digite uma sequência de palavras separadas por vírgula: ")

# Divide a entrada em uma lista usando a vírgula como separador
palavras = entrada.split(',')

# Ordena a lista de palavras em ordem alfabética
palavras_ordenadas = sorted(palavras)

# Imprime as palavras ordenadas, juntando-as com vírgula e espaço
print(", ".join(palavras_ordenadas))