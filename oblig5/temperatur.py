def snitt(fil):
    file = open(fil, "r") #Åpner fil
    temp = []
    for i in file:
        temp.append(int(i)) #Legger linjevis til verdiene fra filen i en tom liste.
    print("Gjennomsnittstemperaturen blir ",sum(temp)/len(temp), "grader") #Deler listens lengde på summen av alle elementene for å finne gjennomsnitt


snitt("temperatur.txt")
