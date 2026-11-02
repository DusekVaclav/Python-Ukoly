import random
tajne_cislo = random.randint(1, 20)
pokusy = 0
max_pokusy = 5

print(f"Hádej číslo mezi 1 a 20. Máš {max_pokusy} pokusů.")

tip = 0 
while tip != tajne_cislo and pokusy <= max_pokusy:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1
    if tip > tajne_cislo:
        print("moje cislo je menší")
    elif tip < tajne_cislo:
        print("moje cislo je větší")
if tip == tajne_cislo:
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
else:
    print(f"Prohrál jsi! Moje číslo bylo {tajne_cislo}.")
