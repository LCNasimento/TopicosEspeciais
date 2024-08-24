"""Escreva um programa que recebe
sequencia e calcula a quantidade de letras e
dígitos.

Entrada:hello world! 123"""



# Recebe a entrada do usuário (sequência de caracteres)
entrada = input("Digite uma sequência de caracteres: ")

# Inicializa contadores para letras e dígitos
letras = 0
digitos = 0

# Itera sobre cada caractere na entrada
for caractere in entrada:
    if caractere.isalpha():  # Verifica se é uma letra
        letras += 1
    elif caractere.isdigit():  # Verifica se é um dígito
        digitos += 1

# Imprime os resultados
print("Letras:", letras)
print("Dígitos:", digitos)