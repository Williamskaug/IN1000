# Lager en funksjon for å addere to tall.
def adder(tall1, tall2):
    sum = tall1 + tall2
    print("Summen av",tall1 ,"og", tall2  ,"er lik", sum)

# Kaller funksjonen med tallene som parameterverdi.
adder(10,11)
adder(5,10)


print("-------------------------------- ")

# Lager en funksjon som teller
def tellForekomst(minTekst, minBokstav):
    antall = 0
    for i in minTekst:
        if i == minBokstav:
            antall = antall + 1
    print("Bokstaven '", minBokstav, "' forekommer", antall, "ganger i tekststrengen '", minTekst, "'.")

# Kaller prosedyren med argumentene som input fra brukeren.
tellForekomst(input("Skriv inn en tekststreng: "), input("Skriv inn en bokstav: "))
