from datetime import date, datetime


# OBS: Como não foi informado a métrica da data adotei como uma string: datetime

# Função responsável por retornar o valor presente
def calc_valor_presente(valor_futuro, taxa_juros, data_futura):
    # Pegando a diferença entre a {data_atual} e a {data_futura}
    qtd_meses = _calc_meses(data_futura)

    # Função Valor Presente: VP = VF / (1 + i)n
    resultado = valor_futuro / (1 + taxa_juros) ** qtd_meses
    return round(resultado, 2)


# Função responsável por retornar o valor futuro
def calc_valor_futuro(valor_presente, taxa_juros, data_futura):
    # Pegando a diferença de dias entre a {data_atual} e a {data_futura} convertendo em meses
    qtd_meses = _calc_meses(data_futura)

    # Função Valor Futuro: VF = VP . (1 + i)n
    resultado = valor_presente * (1 + taxa_juros) ** qtd_meses
    return round(resultado, 2)


# Função que retorna a diferença de meses entre duas datas
def _calc_meses(data_futura):
    data_atual = date.today()
    d1 = datetime.strptime(f'{data_atual}', '%Y-%m-%d')
    d2 = datetime.strptime(f'{data_futura}', '%Y-%m-%d')
    meses = abs((d1 - d2).days) // 30
    return meses
