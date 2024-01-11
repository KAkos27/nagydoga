import math
import random


def veletlen_gen():
    lista = []
    for i in range(0, 13, 1):
        szam = math.floor(random.random() * 191 - 40)
        lista.append(szam)

    return lista


def ketjegyuek_szama(lista):
    osszegzo = 0
    for i in range(0, len(lista), 1):
        if 100 > lista[i] > 9 or -100 < lista[i] < -9:
            osszegzo += 1
    return osszegzo


def paratlan_osszege(lista):
    osszegzo = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 2 != 0:
            osszegzo += lista[i]
    return osszegzo


def par_osszeg(lista):
    osszegzo = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 2 == 0:
            osszegzo += lista[i]
    return osszegzo


def kiiras(lista):
    paratlanok = paratlan_osszege(lista)
    parosak = par_osszeg(lista)
    paratl_str: str = f"A páratlanok összege: {paratlanok}"
    paros_str: str = f"2. e) A párosak összege: {parosak}"
    if parosak > paratlanok:
        print(f"{paros_str} > {paratl_str}")
    elif parosak < paratlanok:
        print(f"{paros_str} < {paratl_str}")
    else:
        print(f"{paros_str} = {paratl_str}")
