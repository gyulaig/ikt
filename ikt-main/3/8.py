import random

felhasznalo_valasztas = input("Kérem válasszon: 'fej' vagy 'írás': ")

pénzfeldobas = random.choice(["fej", "írás"])

if felhasznalo_valasztas == pénzfeldobas:
    print(f"A pénzfeldobás eredménye: {pénzfeldobas}. Ön eltalálta!")
else:
    print(f"A pénzfeldobás eredménye: {pénzfeldobas}. Ön nem találta el.")
