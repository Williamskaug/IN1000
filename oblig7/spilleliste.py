from sang import Sang # Importerer klassen fra sang.py

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        with open(filnavn) as fil: #Bruker "with open", da slipper jeg å lukke filen.
            for linje in fil:
                alleData = linje.strip().split(";")
                tittel = alleData[0]
                artist = alleData[1]
                self._sanger.append(Sang(tittel, artist)) #Legger til objektet Sang i spillelisten med argumentene tittel og artist.

    def leggTilSang(self, nySang):
        self._sanger.append(nySang) #Legger til nySang til den tomme listen.

    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang) #Remove() fjerner objektet fra listen _sanger.

    def spillSang(self, sang):
        if sang in self._sanger:
            sang.spill()

    def spillAlle(self):
        for i in self._sanger:
            i.spill()

    def finnSang(self, tittel):
        for i in self._sanger:
            if i.sjekkTittel(tittel):
                return i

    def hentArtistUtvalg(self, artistnavn):
        sanger = []
        for i in self._sanger:
            if i.sjekkArtist(artistnavn):
                sanger.append(i)
        return sanger #Returnerer alle sanger som er lagt til i listen for riktige artistnavn.
