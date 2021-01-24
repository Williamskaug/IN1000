#Definerer en dictionary hvor hvert element inneholder pasientens navn som nøkkel og en ny dictionary som verdi. Den nye verdien inneholder også nøkkel og verdi som par, hvor hva slags måltid er nøkkel og måltidet er verdi.
matplan = {
    "Kari Nordmann": {"frokost": "brød", "lunch": "egg", "middag": "pølser"},
    "Ola Nordmann": {"frokost": "pannekaker", "lunch": "brød", "middag": "pasta"}
    }

#Lar brukeren skrive inn pasientens navn.
navn = input("Hvem sin matplan ønsker du å se? ")

#Dersom navnet bruker skrev inn er i ordboken, printer programmet ut deres matplan.
if navn in matplan:
    print("Frokost: ", matplan[navn]["frokost"])
    print("Lunch: ", matplan[navn]["lunch"])
    print("Middag: ", matplan[navn]["middag"])

#Dersom navnet mangler, skriver programmet ut en feilmelding.
else:
    print(navn, "er ikke registrert i matplanen.")

# 3
# a) Jeg ville brukt en liste for alle brukernavn.
# b) Jeg ville brukt en ordbok for brukernavn og antall poeng
# c) Jeg ville brukt mengde eller liste for navn til lottovinnere.
# d) Her ville jeg brukt ordbok, med personen som nøkkel og tingene personen er allergisk mot som verdier. 
