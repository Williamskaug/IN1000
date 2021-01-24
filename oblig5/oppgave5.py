# 1. Starter med å definere en variabel som henter fra fil.
# 2. Oppretter en funksjon som går gjennom filen linje for linje, og ved hjelp av funksjonen .split() finner den navnet og verdien og putter disse inn i en ordbok.
# 3. Bruker funksjonen fra tidligere oppgave til å omgjøre fra tommer til cm.
# 4. Oppretter en prosedyre som leser gjennom ordboken målinger, og kaller funksjonen tommerTilCm for å omgjøre verdien til cm. Deretter skriver den ut resultatet på en linje.


file = open("fil.txt", "r")
målinger = {}

for i in file: #Denne funksjonen leser linje for linje av filen fil.txt og skriver inn verdiene i en ordbok.
    navn = i.split()[0]
    verdi = i.split()[1]
    målinger[navn] = float(verdi)

def tommerTilCm(antallTommer): #Funksjon fra tidligere oppgave som omgjør fra tommer til cm.
    assert antallTommer > 0
    cm = antallTommer * 2.54
    return(cm)

def skrivUt():
    for a in målinger:
        print(a,": ", tommerTilCm(målinger[a]), "cm.")  #Kaller funksjonen tommerTilCm med parameterverdien målinger[a], som omgjør verdien fra tommer til cm.


skrivUt()
