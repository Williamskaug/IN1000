from celle import Celle
import random
import os

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjon = 0
        self._rutenett = []

        #Oppretter en nøstet liste og "legger til" en celle i hver plass.
        for x in range(self._rader):
            self._rutenett.append([])
            for y in range(self._kolonner):
                self._rutenett[x].append(Celle())


        #Generer tilfeldig antall levende celler.
        self.generer()

        #Printer ut første generasjon av brettet til
        self.tegnBrett()

    #Setter 1/3 av cellene til levende. Bruker tilfeldig metode.
    def generer(self):
        for x in self._rutenett:
            for y in x:
                if random.randint(0,2) == 1:
                    y.settLevende()

    #Tegnbrett går igjennom rutenettet og skriver ut brettet med levende og døde objekter.
    def tegnBrett(self):
        os.system("clear") #Denne funksjonen fungerer kun for linux, gjør at den tømmer konsollen for hver oppdatering. Bruk "cls" for windows-os.
        for x in self._rutenett:
            print("")
            for y in x:
                print(y.tegnrepresentasjon(), end="")
        print("")

    #Finn nabo tar inn koordinatene til en celle, og returnerer en liste med alle naboer til cellen.
    def finnNabo(self, rad, kolonne):
        nabo = []
        bredde = kolonne +1
        høyde = rad +1

        for x in range(3):
            if (self._rader-1) >= høyde >= 0:
                for y in range(3):
                    if (self._kolonner-1) >= bredde >= 0:
                        if bredde != kolonne or høyde != rad:
                            nabo.append(self._rutenett[høyde][bredde])
                    bredde = bredde-1
            høyde = høyde -1
            bredde = kolonne + 1

        return nabo

    #Oppdatering benytter funksjonen finnNabo og bruker den til å avgjøre om celler skal dø eller leve
    def oppdatering(self):
        dødeceller = []
        levendeceller = []
        rad = 0


        for x in self._rutenett:
            kolonne = 0
            for y in x:
                naboer = 0

                for i in self.finnNabo(rad, kolonne):
                        if i.erLevende():
                            naboer += 1

                if y.erLevende():
                    if naboer != 2 and naboer != 3:
                        dødeceller.append(y)

                if not y.erLevende():
                    if naboer == 3:
                        levendeceller.append(y)

                kolonne += 1
            rad += 1

        for a in dødeceller:
            a.settDoed()

        for b in levendeceller:
            b.settLevende()


        #Øker generasjonstelleren
        self._generasjon += 1

        #Printer ut det oppdaterte brettet.
        self.tegnBrett()


    #Funksjon som returnerer antall levende celler i rutenettet
    def finnAntallLevende(self):
        antall = 0
        for x in self._rutenett:
            for i in x:
                if i.erLevende():
                    antall += 1
        return antall
