""" Bruker oppgavetekst fra eksempelet:
Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal
konstruktøren ha en tom liste hobbyer. Skriv en metode leggTilHobby som tar imot
en tekststreng og legger den til i hobbyer-listen. Skriv også en metode skrivHobbyer.
Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter
Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på
metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt
med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så
mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal
statistikk om brukeren skrives ut.
"""

class Person:
    def __init__(self, navn, alder): #Oppretter konstruktør
        self._navn = navn
        self._alder = alder
        self._hobby = []

    def leggTilHobby(self, tekst):
        self._hobby.append(tekst) #Legger til hobbier fra parameter til listen hobby

    def skrivHobbyer(self):
        print(self._hobby)

    def skrivUt(self):
        print("Navn:", self._navn, "Alder:",self._alder)
        self.skrivHobbyer()

def hovedprogram():
    person1 = Person(input("Navn:"), input("Alder:")) #Oppretter objektet

    print("Når du er ferdig å skrive inn hobbier, press enter")
    x = input("Skriv inn en hobby:")
    while x: #Går helt til brukeren trykker enter. (Så lenge input = True.)
        person1.leggTilHobby(x)
        x = input("Skriv inn en hobby:")

    person1.skrivUt()


hovedprogram()
