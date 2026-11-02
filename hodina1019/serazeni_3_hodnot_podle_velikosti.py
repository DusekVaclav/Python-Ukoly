print("zadej tři hodnoty")
a=input(int(""))
b=input(int(""))
c=input(int(""))

if a>b:
    p = a
    a = b
    b = p
if b>c:
    p = b
    b = c
    c = p
if a>b:
    p = a
    a = b
    b = p
print(f"{a}, {b}, {c}")
