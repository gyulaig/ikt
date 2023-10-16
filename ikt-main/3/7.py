import random

veletlenszam = random.randint(1, 3)

felhasznalo_szam = int(input("Kérem adjon meg egy számot 1 és 3 között: "))

if felhasznalo_szam == veletlenszam:
    print(f"A generált szám ({veletlenszam}) egyezik a beírt számmal ({felhasznalo_szam}).")
else:
    print(f"A generált szám ({veletlenszam}) nem egyezik a beírt számmal ({felhasznalo_szam}).")
