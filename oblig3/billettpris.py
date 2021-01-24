#lager en prosedyre som lar brukeren skrive inn alder, deretter beregner og skriver ut pris som avhenger av om brukeren er barn, voksen, eller honnør.
def pris():
    alder = int(input("Skriv inn alderen din: "))
    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50

    print("Det blir ", billettpris ," kroner")

#Kaller prosedyren 4 ganger.
pris()
pris()
pris()
pris()



#Dersom brukeren skriver inn en ugyldig alder, altså ikke et tall, eller eller et tall med desimaler, vil programmet få en feil, da ikke brukerens input blir testet før beregningene skjer.
