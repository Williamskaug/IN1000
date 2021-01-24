#Oppretter en dictionary med mattypen som nøkkel og prisen som verdi.
vare = {"melk" : 14.90, "brød" : 24.90, "yoghurt" : 21.90, "pizza" : 39.90}
print(vare) #Printer hele ordboken.

#Lager en prosedyre for å legge til nye produkter i ordboken.
def leggtil():
    print("--- Legg til en vare ---")
    navn = input("Varenavn: ")
    pris = float(input("Varens pris: "))
    vare[navn] = pris #Her legges verdiene til i slutten av ordboken.

#Kaller prosedyren leggtil() to ganger to å legge til to produkter.
leggtil()
leggtil()

#Printer til slutt hele ordboken med de to nye produktene.
print(vare)
