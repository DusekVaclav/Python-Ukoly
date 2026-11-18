import urllib.request 
URL = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.urlopen(URL) # odkaz na objekt odpovědi serveru
celkem_srazky = 0
pocet_dnu = 0
radek = odpoved.readline() # načtení jednoho řádku z odpovědi serveru

while bool(radek): # dokud je řádek neprázdný
    text = radek.decode("utf-8").strip() # vrati cisty text odpovidajici cislu
    srazka = float(text)
    if srazka >= 0:
        celkem_srazky += srazka
        pocet_dnu += 1
    radek = odpoved.readline()

odpoved.close() # ukončení komunikace se serverem

print(celkem_srazky / pocet_dnu)

