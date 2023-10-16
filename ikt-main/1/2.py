import datetime

userAge = input("Hany eves vagy? ")
print(f'Te most {userAge} eves vagy.')
userAge = int(userAge)
born = datetime.date.today().year - userAge
print(f'Ekkor szulettel: {born}')

userAge = str(userAge)
ilyen = input(f"Es milyen {userAge} evesnek lenni?") 