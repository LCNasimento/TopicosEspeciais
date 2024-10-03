"""Exercicio slide 26"""

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

while True:
    try:
        peso = float(input("Informe o peso (kg): "))
        altura = float(input("Informe a altura (m): "))
        imc = calcular_imc(peso, altura)
        print(f"O IMC é: {imc:.2f}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
    
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break
"""Exercicio slide 33"""


def contar_pares(numeros):
    return len([n for n in numeros if n % 2 == 0])

def listar_impares(numeros):
    return [n for n in numeros if n % 2 != 0]

def maior_numero(numeros):
    return max(numeros)

def menor_numero(numeros):
    return min(numeros)

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

numeros = []
while True:
    try:
        num = float(input("Informe um número: "))
        numeros.append(num)
    except ValueError:
        print("Erro: Por favor, insira um valor numérico.")
    
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break

print(f"Quantidade de números pares: {contar_pares(numeros)}")
print(f"Números ímpares: {listar_impares(numeros)}")
print(f"Maior número: {maior_numero(numeros)}")
print(f"Menor número: {menor_numero(numeros)}")
print(f"Média dos números: {calcular_media(numeros):.2f}")


"""Exercicio slide 34"""

def gerar_curriculo(nome, endereco, telefone, email, escolaridade, experiencia):
    html = f"""
    <html>
    <head>
        <title>Currículo de {nome}</title>
    </head>
    <body>
        <h1>{nome}</h1>
        <p><strong>Endereço:</strong> {endereco}</p>
        <p><strong>Telefone:</strong> {telefone}</p>
        <p><strong>E-mail:</strong> {email}</p>
        <h2>Escolaridade</h2>
        <p>{escolaridade}</p>
        <h2>Experiência Profissional</h2>
        <p>{experiencia}</p>
    </body>
    </html>
    """
    with open("curriculo.html", "w") as file:
        file.write(html)
    print("Currículo gerado com sucesso!")

nome = input("Informe seu nome: ")
endereco = input("Informe seu endereço: ")
telefone = input("Informe seu telefone: ")
email = input("Informe seu e-mail: ")
escolaridade = input("Informe sua escolaridade: ")
experiencia = input("Informe sua experiência profissional: ")

gerar_curriculo(nome, endereco, telefone, email, escolaridade, experiencia)
