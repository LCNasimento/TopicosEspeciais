"""Escreva um programa que recebe
sequencia e calcula a quantidade de letras
maiúsculas e minúsculas

Entrada: Hello world!"""


# Recebe a entrada do usuário (sequência de caracteres)
entrada = input("Digite uma sequência de caracteres: ")

# Inicializa contadores para letras maiúsculas e minúsculas
maiusculas = 0
minusculas = 0

# Itera sobre cada caractere na entrada
for caractere in entrada:
    if caractere.isupper():  # Verifica se é maiúscula
        maiusculas += 1
    elif caractere.islower():  # Verifica se é minúscula
        minusculas += 1

# Imprime os resultados
print("Maiúsculas:", maiusculas)
print("Minúsculas:", minusculas)