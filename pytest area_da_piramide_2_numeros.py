import pytest
import csv
import main


def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'Vendors/massa_area_piramide_2_numeros.csv'

    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo nao encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha nao prevista: {fail}')


@pytest.mark.parametrize('id, numero1, numero2, resultado_esperado, tipo_teste', ler_dados_csv())
def teste_massa_area_piramide_2_numeros(id, numero1, numero2, resultado_esperado, tipo_teste):
    # Configura - virá da lista

    # Executa
    resultado_obtido = main.area_da_piramide_2_numeros(int(numero1), int(numero2))

    # Valida
    if tipo_teste == 'negativo':
        # Se o teste é do tipo negativo vai comparar os valores
        # Por isso converte o resultado_esperado para numero (float)
        assert float(resultado_esperado) == resultado_obtido
    else:
        # Senão, o teste é negativo e vai comparar as mensagens de falha
        # Por isso não precisa converter
        assert resultado_esperado == resultado_obtido


