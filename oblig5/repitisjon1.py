mineOrd = []

def slaaSammen(streng1, streng2):
    return streng1+streng2

def skrivUt(liste):
    for i in liste:
        print(i)

brukerinput = input("Skriv inn 'i', 'u', eller 's':")

while brukerinput != "s":
    if brukerinput == "i":
        mineOrd.append(slaaSammen(input("String1:"), input("String2: "))) #Kaller funksjonen slaaSammen med to input-verdier fra bruker.
        brukerinput = input("\nSkriv inn 'i', 'u', eller 's':")
    elif brukerinput == "u":
        skrivUt(mineOrd)
        brukerinput = input("\nSkriv inn 'i', 'u', eller 's':")
    else:
        brukerinput = input("\nSkriv inn 'i', 'u', eller 's':")
