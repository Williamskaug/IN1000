#Oppgavetekst
#Dette programmet kjører en quiz med 3 oppgaver. Hver og en oppgave starter hver for seg når den forrige oppgaven er ferdig.
# Starter med å skrive ut spørsmålet til brukeren og et inputfelt, hvor bruker kan skrive svaret sitt.
# Deretter tester jeg brukerens svar opp mot fasit med en if-setning, og legger til et poeng dersom svaret er korrekt, og gir melding til bruker.
# Dersom brukerens svar er feil, får brukeren melding "Feil svar."
# Når brukeren har svart på alle tre spørsmål, får brukeren vite totale poengscore, av totale oppgaver.
# Bruker funksjonen lower() på brukerens svar for å hindre at svaret blir feil fordi det er feil store og små bokstaver. Lower() setter alle bokstavene til små.

poeng = 0

#Quiz-oppgave. 1
print("Hva står forkortelsen .py for?")
svar = input("Svar: ")

if svar.lower() == "python":
    poeng = poeng + 1
    print("Korrekt. Du har nå", poeng, "poeng.")
    print("--------------")
else:
    print("Feil svar.")
    print("--------------")

#Quiz-oppgave. 2
print("Hva heter hovedstaden i Norge?")
svar = input("Svar: ")

if svar.lower() == "oslo":
    poeng = poeng + 1
    print("Korrekt. Du har nå", poeng, "poeng.")
    print("--------------")
else:
    print("Feil svar.")
    print("--------------")

#Quiz-oppgave. 3
print("Hva står UiO for?")
svar = input("Svar: ")

if svar.lower() == "universitetet i oslo":
    poeng = poeng + 1
    print("Korrekt. Du har nå", poeng, "poeng.")
    print("--------------")
else:
    print("Feil svar.")
    print("--------------")

print("Du fikk totalt", poeng, "av 3 poeng.")
