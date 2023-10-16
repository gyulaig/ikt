henrik_kosarazik = input("Jön Henrik ma kosarazni? (igen/nem): ").strip().lower()
hanna_kosarazik = input("Jön Hanna ma kosarazni? (igen/nem): ").strip().lower()

if henrik_kosarazik == "igen" and hanna_kosarazik == "igen":
    print("Mindketten jönnek kosarazni.")
elif henrik_kosarazik == "igen" or hanna_kosarazik == "igen":
    print("Csak az egyikük jön kosarazni.")
else:
    print("Egyikük sem jön kosarazni.")
