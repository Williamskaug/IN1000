# Oppretter en tom liste
liste = []
brukerinput = 1

# While løkke som tar inn brukerinput frem til brukeren skriver inn 0.
while brukerinput != 0:
    brukerinput = int(input("input: "))
    liste.append(brukerinput) #Setter tallet inn i listen

liste.pop() #Fjerner det siste tallet som er 0
print("\n", liste) #Printer listen

#For-løkke som printer ut listen, linje for linje.
for x in range(0, len(liste)):
    print("Du skrev inn tallene: ", liste[x])

print("\n")

#Setter minSum lik 0, og bruker en for-løkke for å travasjere gjennom listen, og addere sammen alle tallene.
minSum = 0
for y in range(0, len(liste)):
    minSum = minSum + liste[y]
print("Sum er lik ", minSum)

#Definerer en variabel for min- og maksverdi, setter dem lik liste[0], da vil ikke verdien påvirke maks- eller min.
min = liste[0]
maks = liste[0]

# Bruker en for-løkke som tester om neste tall i listen er mindre enn variabelen min.
for a in range(0, len(liste)):
    if liste[a] < min:
        min = liste[a]

# Bruker en for-løkke som tester om neste tall i listen er større enn variabelen maks.
for b in range(0, len(liste)):
    if liste[b] > maks:
        maks = liste[b]

# Printer min og maks.
print("Det minste tallet er ", min)
print("Det største tallet er", maks)
