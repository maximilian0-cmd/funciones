"""
Módulo de funciones numéricas básicas.

Contiene funciones simples para clasificar números enteros.

Funciones:
    par_impar(num): indica si un número es par, impar o cero.
"""


def par_impar(num):
    """
    Clasifica un número entero como "par", "impar" o "cero".

    Reglas:
        - Si el número es 0, devuelve "cero".
        - Si es divisible por 2 (resto 0), devuelve "par".
        - En cualquier otro caso, devuelve "impar".

    Args:
        num (int): Número entero a evaluar.

    Returns:
        str: "cero", "par" o "impar" según corresponda.

    Examples:
        >>> par_impar(0)
        'cero'
        >>> par_impar(4)
        'par'
        >>> par_impar(7)
        'impar'
        >>> par_impar(-3)
        'impar'
    """
    if num == 0:
        return "cero"
    if num % 2 == 0:
        return "par"
    if num % 2 != 0:
        return "impar"

def lista_par_impar(lista_nums):
        lista_resultados=[]
        for numero in lista_nums:
            lista_resultados.append(par_impar(numero))
        return lista_resultados

print(lista_par_impar([2,5,7,13,8,9,25]))