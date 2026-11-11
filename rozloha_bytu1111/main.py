def vypocet_obsahu(a, b):
    #kontrola zadaných hodnot
    if a < 0 or b < 0:
        return None
    obsah = a * b
    return obsah 

print("Výpočet rozlohy bytů")

pocet_mistnosti = int(input("Zadej počet místností"))
mistnost = 1
obsah = 0
while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost} místností")
    strana_a = float(input("Zadej rozměr a"))
    strana_b = float(input("Zadej rozměr b"))
    obsah_mistnosti = vypocet_obsahu(strana_a, strana_b)
    if obsah_mistnosti != None:
        obsah += obsah_mistnosti
        mistnost += 1

if pocet_mistnosti > 0:
    print(f"Celková rozoha bytu je {obsah}")
else:
    print("Zadej kladný počet místností")