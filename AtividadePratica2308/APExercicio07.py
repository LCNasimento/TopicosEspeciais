from datetime import date

"""Escreva um programa Python para
manipulação de datas e apresente na tela:
– Data atual
– Ano atual
– Mês atual
– Dia atual
– Data atual formatada dia/mês/ano
– Data atual no formato:
dia de mês_por_extenso de ano"""


# Obtém a data atual
data_atual = date.today()

# Extrai componentes da data
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

# Formata a data
data_formatada = data_atual.strftime("%d/%m/%Y")

# Nomes dos meses por extenso
meses_extenso = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]
mes_extenso = meses_extenso[mes_atual - 1]

# Formata a data com mês por extenso
data_extenso = f"{dia_atual} de {mes_extenso} de {ano_atual}"

# Imprime os resultados
print("Data atual:", data_atual)
print("Ano atual:", ano_atual)
print("Mês atual:", mes_atual)
print("Dia atual:", dia_atual)
print("Data atual formatada:", data_formatada)
print("Data atual com mês por extenso:", data_extenso)