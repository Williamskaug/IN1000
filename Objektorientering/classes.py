class Student:
    def __init__(self, navn):
        self._antMott = 0
        self._navn = navn

    def registrer(self):
        self._antMott = self._antMott + 1

    def hentOppmøte(self):
        return self._antMott

    def hentNavn(self):
        return self._navn

class Rom:

    def __init__(self, nr, navn, opsys, ant):
        self._nr = nr
        self._navn = navn
        self._opsys = opsys
        self._maxAnt = ant

    def passer(self, antP, opsys):
        return (self._maxAnt >= antP and self._type == opsys)

    def skrivLinje(self):
        print("%d %-15s %-15s%d" % (self._nr, self._navn, self._type, self._maxAnt))
