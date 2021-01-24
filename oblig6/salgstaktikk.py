salg = {}
def innlesning(filnavn):
    file = open(filnavn, "r") #Åpner fil
    for i in file:
         salg[i.split()[0]] = int(i.split()[1]) #Legger linjevis til verdiene fra filen til ordboken.
    return salg

def maanedensSalgsperson(ordbok):
    topp = 0
    leder = ""
    for x,y in ordbok.items(): # Henter ut nøkkel og verdi som x og y i hvert par i ordboken.
        if y > topp:
            leder = x
            topp = y
    print("Månedens salgsperson:", leder, "med antall salg: ",ordbok[leder])

def totalAntallSalg(ordbok):
    sum = 0
    for a in ordbok:
        sum += ordbok[a]
    return sum

def gjennomsnittSalg(ordbok):
    sum = 0
    antall = 0
    for f in ordbok:
        sum += ordbok[f]
        antall = antall + 1
    print("\nAktive selgere denne måneden: ", antall)
    return sum/antall

def hovedprogram(): #Hovedprogram - kaller alle funksjonene over.
    innlesning("salgstall.txt")
    maanedensSalgsperson(salg)
    print("Totalt antall salg: ",totalAntallSalg(salg))
    print("Gjennomsnitt antall salg: ",gjennomsnittSalg(salg))

hovedprogram()
