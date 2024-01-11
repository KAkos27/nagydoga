import elsof
import masodikf
import harmadikf

elsof.harmadik()

lista=masodikf.veletlen_gen()
print(f"2. a) A lista: {lista}")
ketjegyuek=masodikf.ketjegyuek_szama(lista)
print(f"2. b) A kétjegyűek száma: {ketjegyuek}")
masodikf.kiiras(lista)


stadion_lista=harmadikf.file_olvasas()
harmadikf.csapat_szam(stadion_lista)
harmadikf.ny_csapatok(stadion_lista)