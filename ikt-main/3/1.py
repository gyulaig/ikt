szam = int(input("Kérem adjon meg egy egész számot: "))

if szam > 0 and szam % 2 == 0:
    print("A megadott szám pozitív és páros.")
elif szam < 0 and szam % 2 != 0:
    print("A megadott szám negatív és páratlan.")
else:
    print("A megadott szám nem felel meg a feltételeknek.")
