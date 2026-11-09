import math
print("Test prvočísla")
cislo = int(input("Zadej Přirozené číslo: "))

je_prvocislem = True
delitel = 3
if cislo < 2:
    je_prvocislem = False
elif cislo == 2:
    je_prvocislem = True
elif cislo % 2 == 0:
    je_prvocislem = False
else:
    while delitel < math.sqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislem = False
            break
        delitel += 2

if je_prvocislem:
    print(f"Číslo{cislo} je prvocislem.")
else:
    print(f"číslo {cislo} není prvocislem")

