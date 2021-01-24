class Motorsykkel:
    def __init__(self, merke, regnr, km): #Oppretter konstruktøren
        self._merke = merke
        self._regnr = regnr
        self._km = km

    def kjor(self, km):
        self._km += km

    def hentKilometerstand(self):
        return self._km

    def skrivUt(self):
        return (self._merke, "Regnr:",self._regnr,  "km:",self._km) #Returnerer alle egenskapene til motorsykkelen
