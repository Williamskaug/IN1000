from hund import Hund #Importerer klassen fra hund.py

def hovedprogram():
    hund1 = Hund(8,4)

    hund1.spring()
    hund1.spring()
    print("Vekt", hund1.hentVekt(), "kg")

    hund1.spis()
    hund1.spis()
    print("Vekt", hund1.hentVekt(), "kg")

hovedprogram()
