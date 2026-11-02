# Zadání hodiny od uživatele
hodina = int(input("Zadejte hodinu (0–23): "))

if hodina < 0:
  print("Hodina nemůže být záporná.")
elif hodina >= 24:
  print("Zadávejte platné hodiny.")
  
else:
  if 5 <= hodina <= 8:
    print("Dobré ráno")
  elif 9 <= hodina <= 11:
    print("Dobré dopoledne")
  elif hodina == 12:
    print("Dobré poledne")
  elif 13 <= hodina <= 17:
    print("Dobré odpoledne")
  elif 18 <= hodina <= 21:
    print("Dobrý večer")
  else:
    print("Dobrou noc")