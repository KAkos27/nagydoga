from Stadionok import Stadionok


def file_olvasas():
    stadion_lista = []
    fajl = open("stadionok.txt", "r", encoding="utf-8")
    fajl.readline()
    elso_lista = fajl.readlines()
    fajl.close()

    for i in range(0, len(elso_lista), 1):
        sor_lista = elso_lista[i].strip()
        sor_lista = sor_lista.split(";")

        stadion = Stadionok(
            sor_lista[0],
            sor_lista[1],
            sor_lista[2],
            sor_lista[3],
            sor_lista[4],
        )

        stadion_lista.append(stadion)

    return stadion_lista


def csapat_szam(lista):
    szamlalo = 0
    for i in range(0, len(lista), 1):
        szamlalo += int(lista[i].csapatok_szama)
    print(f"3. e) A csapatok száma: {szamlalo}")


def ny_csapatok(lista):
    print("3. f)\n")
    for i in range(0, len(lista), 1):
        if lista[i].varos == "New York":
            print(f"Stadion neve: {lista[i].stadion}")
            print(f"Csapatok száma: {lista[i].csapatok_szama}")
