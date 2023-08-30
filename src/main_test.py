import main
from faker import Faker

faker = Faker()


def teste_calc_meses():
    # Variáveis de teste na função privada
    esperado = 12
    resultado = main._calc_meses("2024-08-30")

    # Deve retornar True
    assert resultado == esperado


def teste_calc_valor_presente():
    # Geração de valores aleatórios
    valor_futuro_aleatorio = faker.random_int(1000, 10000)
    data_futura_aleatorio = faker.future_date("+1y")
    qtd_meses = main._calc_meses(data_futura_aleatorio)

    # Variáveis de teste
    resultado = main.calc_valor_presente(valor_futuro_aleatorio, 0.5, data_futura_aleatorio)
    esperado = valor_futuro_aleatorio / (1 + 0.5) ** qtd_meses

    # Deve retornar True
    assert resultado == round(esperado)


def teste_calc_valor_futuro():
    # Geração de valores aleatórios
    valor_presente_aleatorio = faker.random_int(1000, 10000)
    data_futura_aleatorio = faker.future_date("+1y")
    qtd_meses = main._calc_meses(data_futura_aleatorio)

    # Variáveis de teste
    resultado = main.calc_valor_futuro(valor_presente_aleatorio, 0.5, data_futura_aleatorio)
    esperado = valor_presente_aleatorio * (1 + 0.5) ** qtd_meses

    # Deve retornar True
    assert resultado == round(esperado, 2)
