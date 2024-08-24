import re

"""Um website necessita registrar
usuários e suas respectivas senhas. Escreva um
programa que verifique a validade das senhas a
partir dos seguintes critérios:
Pelo menos uma letra minúscula [a-z]
Pelo menos uma letra dígito [0-9]
Pelo menos uma letra maiúscula [A-Z]
Pelo menos um símbolo [$#@]
Tamanho mínimo da senha: 6
Tamanho máximo da senha: 12"""


# Função para validar a senha
def validar_senha(senha):
    # Critérios de validação usando expressões regulares
    criterios = [
        r"[a-z]",  # Pelo menos uma letra minúscula
        r"[0-9]",  # Pelo menos um dígito
        r"[A-Z]",  # Pelo menos uma letra maiúscula
        r"[$#@]",  # Pelo menos um símbolo
        r"^.{6,12}$"  # Tamanho entre 6 e 12 caracteres
    ]

    # Verifica se a senha atende a todos os critérios
    for criterio in criterios:
        if not re.search(criterio, senha):
            return False
    return True

# Recebe a senha do usuário
senha = input("Digite a senha: ")

# Valida a senha e imprime o resultado
if validar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")
