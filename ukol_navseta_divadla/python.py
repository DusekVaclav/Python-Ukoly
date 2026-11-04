print("Vítejte v divadle!")
print("Základní cena vstupenky je 500 Kč.")  
vek = float(input("Zadej svůj věk: ")) 
je_student = input("Jsi student? (ano/ne): ") .lower()
pocet_osob = int(input("Zadej počet osob: "))

if pocet_osob >=4:
    cena = 500 * pocet_osob * 0.25
elif je_student == "ano" and vek < 26:
    cena = 500 * pocet_osob * 0.7
elif vek > 65:
    cena = 500 * pocet_osob * 0.8
else:
    cena = 500 * pocet_osob

