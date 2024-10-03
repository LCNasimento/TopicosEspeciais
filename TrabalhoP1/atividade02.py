# Lista para armazenar os produtos
produtos = []
codigo_incremental = 1

# Função para cadastrar produto
def cadastrar_produto():
    global codigo_incremental
    nome = input("Nome do produto: ")
    valor_compra = float(input("Valor de compra: "))
    quantidade = int(input("Quantidade em estoque: "))
    
    valor_venda = valor_compra + (valor_compra * 25 / 100)  # Acresce 25% ao valor de compra
    
    # Criando produto manualmente sem dicionários ou bibliotecas
    produto = {
        "codigo": codigo_incremental,
        "nome": nome,
        "valor_compra": valor_compra,
        "valor_venda": valor_venda,
        "quantidade": quantidade
    }
    
    produtos.append(produto)  # Adiciona o produto à lista
    codigo_incremental += 1
    print(f"Produto '{nome}' cadastrado com sucesso!\n")

# Função para exibir relatório de produtos
def relatorio_produtos():
    if len(produtos) == 0:
        print("\nNenhum produto cadastrado ainda.\n")
    else:
        print("\n--- Relatório de Produtos ---")
        
        # Ordenação manual pelo nome do produto
        for i in range(len(produtos)):
            for j in range(i + 1, len(produtos)):
                if produtos[i]["nome"] > produtos[j]["nome"]:
                    produtos[i], produtos[j] = produtos[j], produtos[i]
        
        # Exibe os produtos
        for produto in produtos:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Valor Compra: R${produto['valor_compra']:.2f}, Valor Venda: R${produto['valor_venda']:.2f}, Quantidade: {produto['quantidade']}")
        print("\n")

# Função para exibir relatório de produtos com estoque baixo
def relatorio_estoque_baixo():
    estoque_baixo = []  # Lista para armazenar produtos com estoque baixo
    
    # Verificação manual dos produtos
    for produto in produtos:
        if produto["quantidade"] <= 5:
            estoque_baixo.append(produto)
    
    if len(estoque_baixo) == 0:
        print("\nNenhum produto com estoque baixo.\n")
    else:
        print("\n--- Relatório de Estoque Baixo ---")
        for produto in estoque_baixo:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")
        print("\n")

# Função para exportar dados de forma simples (exibe no console)
def exportar_dados():
    print("\n--- Exportando Dados ---")
    print("[")
    for produto in produtos:
        print(f'    {{ "codigo": "{produto["codigo"]}", "nome": "{produto["nome"]}", "valor_compra": "{produto["valor_compra"]:.2f}", "quantidade": "{produto["quantidade"]}" }},')
    print("]\n")
    print("Dados exportados (exibidos no console).\n")

# Função principal para exibir o menu
def menu():
    while True:
        print("\nVarejão do João")
        print("[1] Cadastrar Produto")
        print("[2] Relatório de Produtos")
        print("[3] Relatório de Estoque Baixo")
        print("[4] Exportar Dados")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            relatorio_produtos()
        elif opcao == '3':
            relatorio_estoque_baixo()
        elif opcao == '4':
            exportar_dados()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o menu
menu()
