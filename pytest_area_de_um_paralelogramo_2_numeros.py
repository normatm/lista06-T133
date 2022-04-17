import pytest

import main


tipo_teste_area_de_um_paralelogramo_2_numeros = [
    (10, 5, 5),
    (7, -7, 14),
    (-6, 0,-6)
]
@pytest.mark.parametrize('numero1,numero2,resultado_esperado', tipo_teste_area_de_um_paralelogramo_2_numeros)
def teste_tipo_teste_area_de_um_paralelogramo_2_numeros(numero1, numero2, resultado_esperado):
    # Configura - vira da lista

    # Executa
    resultado_obtido = main.area_de_um_paralelogramo_2_numeros(int(numero1), int(numero2))

    # Valida
    assert resultado_esperado == resultado_obtido
