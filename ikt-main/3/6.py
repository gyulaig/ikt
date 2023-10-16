import random

gep_gondolt_szam = random.randint(1, 5)
felhasznalo_szam = int(input("Kérlek, adj meg egy számot 1 és 5 között: "))

if felhasznalo_szam == gep_gondolt_szam:
    print("Egyezik a szám! Gratulálok!")
elif felhasznalo_szam < gep_gondolt_szam:
    print("A gondolt szám nagyobb.")
else:
    print("A gondolt szám kisebb.")
