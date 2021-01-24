# Oppretter en tom liste
steder = []

# Bruker en for-løkke for å la brukeren skrive inn 5 reisemål.
for x in range(0,5):
    steder.append(input("Reisemål:"))

# Oppretter en tom liste
klesplagg = []

# Bruker en for-løkke for å la brukeren skrive inn 5 klesplagg.
for x in range(0,5):
    klesplagg.append(input("Klesplagg:"))

# Oppretter en tom liste
avreisedatoer = []

# Bruker en for-løkke for å la brukeren skrive inn 5 avreisedatoer.
for x in range(0,5):
    avreisedatoer.append(input("Avreisedatoer:"))

# Oppretter en ny liste som inneholder de øvre listene.
reiseplan = [steder, klesplagg, avreisedatoer]

# Printer listene listevis.
for x in reiseplan:
    print(x)

i1 = int(input("Velg fra liste 1, 2 eller 3: "))
i2 = int(input("Velg element fra listen: "))

# Tester om brukerens verdier er gyldige, hvis de er gyldide prites reiseplan[brukerverdi][brukerverdi]
if i1 <= len(reiseplan) and i1 >= 0:
    if i2 <= len(reiseplan[i1]) and i2 >= 0:
        print(reiseplan[i1-1][i2-1])
    else:
        print("Ugyldig input!")
else:
    print("Ugyldig input!")
