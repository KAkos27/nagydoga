def elso(i):
    szam: int = int(input(f"Kérek a(z) {i+1}. páros számot! "))
    while szam % 2 != 0:
        szam: int = int(input(f"Ez nem páros! Kérem a(z) {i+1}. PÁROS számot kérem! "))
    return szam


def masodik():
    szam_lista = []
    for i in range(0, 3, 1):
        szam_lista.append(elso(i))
    return szam_lista


def harmadik():
    lista = masodik()
    helyzet_index = 0
    min = 99999999
    for i in range(0, len(lista), 1):
        if lista[i] < min:
            min = lista[i]
            helyzet_index = i + 1
    print(
        f"{helyzet_index}. lépésben adta meg a legkisebb páros számot, melynek értéke: {min}"
    )
