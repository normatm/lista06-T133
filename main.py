def print_oi(name):
    print(f'oi, {name}')


def area_de_um_cubo_2_numeros(areatotal1, areatotal2):
    return areatotal1 + areatotal2

def area_de_um_paralelogramo_2_numeros(areatotal1, areatotal2):
    return areatotal1 - areatotal2

def area_de_uma_piramide_2_numeros(areatotal1, areatotal2):
    return areatotal1 * areatotal2

def area_do_cubo_2_numeros(numero1, numero2):
    try:                 # tente fazer
        return numero1 + numero2
    except ZeroDivisionError:
        return 'area por zero'

def area_de_um_paralelogramo(numero1, numero2):
    try:                 # tente fazer
        return areatotal1 + areatotal2
    except ZeroDivisionError:
        return 'area por zero'

def area_da_piramide_2_numeros(numero1, numero2):
    try:                 # tente fazer
        return numero1 + numero2
    except ZeroDivisionError:
        return 'area por zero'

if __name__ == '__main__':
    print_oi('Norma')

    """
        areatotal1 = 17
        areatotal2 = 90
        resultado = area_de_um_cubo_2_numeros(areatotal1, areatotal2)
        print(f'A soma de {areatotal1} e {areatotal2} é igual a {resultado}')
        print(f'{areatotal1}+{areatoal2}={resultado}')
    """

    # Area_de_um_cubo_2_numeros
    resultado = area_de_um_cubo_2_numeros(20, 30)
    print(f'O resultado da soma é  {resultado}')

    # Area_de_um_paralelogramo_2_numeros
    resultado = area_de_um_paralelogramo_2_numeros(50, 30)
    print(f' 0 resultado da subtração é {resultado}')

    # Area_de_uma_piramide
    resultado = area_de_uma_piramide_2_numeros(3, 6)
    print(f' 0 resultado da multiplicação é {resultado}')


