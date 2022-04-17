import pytest

import main

lista_para_area_do_cubo_2_numeros = [
    (10, 5, 15),
    (7, 0, 0),
    (5, 7, 35),
    (6, 0, 'area por zero')
]
@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_area_do_cubo_2_numeros)
def test_rea_do_cubo_2_numeros(numero1, numero2, resultado_esperado):
    # Configura     # vem da lista
    numero1 = 10
    numero2 = 5
    resultado_esperado = 15

    # Executa
    resultado_obtido = main.area_de_um_cubo_2_numeros(numero1, numero2)

    # Valida
    assert resultado_obtido == resultado_esperado
