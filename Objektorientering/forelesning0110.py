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

    stud1 = Student("William")
    stud1.registrer()
    ant = stud1.hentOppmøte()
    navn = stud1.hentNavn()

    print(ant)
    print(navn)
