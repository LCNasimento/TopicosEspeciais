# Função para verificar se o ano é bissexto
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Função para obter o número de dias de um mês específico
def dias_do_mes(mes, ano):
    if mes == 2:  # Fevereiro
        if eh_bissexto(ano):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]:  # Abril, Junho, Setembro, Novembro
        return 30
    else:  # Janeiro, Março, Maio, Julho, Agosto, Outubro, Dezembro
        return 31

# Função para obter o nome do mês por extenso
def nome_mes_por_extenso(mes):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return meses[mes - 1]

# Função que retorna a data atual de maneira manual (simulação de data atual)
def obter_data_atual():
    # Simulação de data atual (fixa para o exemplo)
    dia_atual = 3
    mes_atual = 10
    ano_atual = 2024
    
    return dia_atual, mes_atual, ano_atual

# Função para formatar a data atual
def formatar_data(dia, mes, ano):
    return f"{dia}/{mes}/{ano}"

# Função para exibir a data no formato: "dia de mês_por_extenso de ano"
def data_por_extenso(dia, mes, ano):
    mes_extenso = nome_mes_por_extenso(mes)
    return f"{dia} de {mes_extenso} de {ano}"

# Função principal para exibir todas as informações de data
def manipular_data():
    dia_atual, mes_atual, ano_atual = obter_data_atual()
    
    print("Data atual:", formatar_data(dia_atual, mes_atual, ano_atual))
    print("Ano atual:", ano_atual)
    print("Mês atual:", mes_atual)
    print("Dia atual:", dia_atual)
    print("Data atual formatada:", formatar_data(dia_atual, mes_atual, ano_atual))
    print("Data por extenso:", data_por_extenso(dia_atual, mes_atual, ano_atual))

# Executar a função principal
manipular_data()
