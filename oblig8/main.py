from spillebrett import Spillebrett
from celle import Celle

def main():

    #Oppretter brett1, som jeg gir klassen Spillebrett med brukerens input som parameterverdier.
    brett1 = Spillebrett(int(input("Bredde: ")),int(input("Høyde: ")))
    brett1.oppdatering()

    print("Dette er den ", brett1._generasjon, "generasjonen.")
    print(brett1.finnAntallLevende(), "levende celler.")
    brukerinput = int(input("Enter for nesten generasjon, q for å avslutte: "))

    #Oppdaterer til neste generasjon frem til brukeren klikker "q".
    while brukerinput != 10000:
        brett1.oppdatering()
        print("Dette er den ", brett1._generasjon, "generasjonen.")
        print(brett1.finnAntallLevende(), "levende celler.")

        brukerinput += 1


# Starter programmet
main()
