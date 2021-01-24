class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    def spill(self):
        print('\t Spiller av', self._tittel, 'av', self._artist)

    def sjekkArtist(self, navn):
        liste = navn.split()
        for i in liste:
            if i in self._artist:
                return True
        return False

    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    def sjekkArtistogTittel(self, artist, tittel):
        liste = artist.split()
        for i in liste:
            if i in self._artist and tittel.lower() == self._tittel.lower():
                return True
        return False
