from datetime import date, datetime


# OBS: Como não foi informado a métrica da data adotei como uma string: datetime - ex: 2023-08-29 usando a
# diferença dos meses entre os 2 períodos informados

# Função responsável por retornar o valor presente
def valor_presente(valor_futuro, taxa_juros, data_futura):
    # Pegando a diferença entre a {data_atual} e a {data_futura}
    data_atual = date.today()
    d1 = datetime.strptime(f'{data_atual}', '%Y-%m-%d')
    d2 = datetime.strptime(f'{data_futura}', '%Y-%m-%d')
    quantidade_meses = abs((d1 - d2).days) // 30

    # Função Valor Presente: VP = VF / (1 + i)n
    resultado = valor_futuro / (1 + taxa_juros) ** quantidade_meses
    return resultado


# Função responsável por retornar o valor futuro
def valor_futuro(valor_presente, taxa_juros, data_futura):
    # Pegando a diferença entre a {data_atual} e a {data_futura}
    data_atual = date.today()
    d1 = datetime.strptime(f'{data_atual}', '%Y-%m-%d')
    d2 = datetime.strptime(f'{data_futura}', '%Y-%m-%d')
    quantidade_meses = abs((d1 - d2).days) // 30

    # Função Valor Futuro: VF = VP . (1 + i)n
    resultado = valor_presente * (1 + taxa_juros) ** quantidade_meses
    return resultado
