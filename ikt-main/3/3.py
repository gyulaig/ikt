szam = int(input("Kérem adjon meg egy egész számot: "))

oszthato_3 = szam % 3 == 0
oszthato_4 = szam % 4 == 0

if oszthato_3 and oszthato_4:
    print("A megadott szám mind 3-mal, mind 4-gyel osztható.")
elif oszthato_3:
    print("A megadott szám csak 3-mal osztható.")
elif oszthato_4:
    print("A megadott szám csak 4-gyel osztható.")
else:
    print("A megadott szám sem 3-mal, sem 4-gyel nem osztható.")
