

x1_oblast = 4
y1_oblast = 2
x2_oblast = 9
y2_oblast = 7

xb = int(input("zadej souřadnici X bodu: "))
yb = int(input("zadej souřadnici Y bodu: "))

lezi_na_1 = xb>=x1_oblast and xb<x2_oblast and yb=y1_oblast
lezi_na_2 = yb>=y1_oblast and yb<=y2_oblast and xb=x2_oblast
lezi_na_3 = xb>=x1_oblast and xb<x2_oblast and yb=y2_oblast
lezi_na_2 = yb>=y1_oblast and yb<=y2_oblast and xb=x1_oblast