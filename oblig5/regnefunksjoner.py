def addisjon(x,y):
    return x+y

#print("Sum er lik", addisjon(5,3))

def subtraksjon(x,y):
    return x-y

def divisjon(x,y):
    return x/y

#Tester at funksjonene gir riktige resultater
assert subtraksjon(2,2) == 0
assert subtraksjon(-2,-2) == 0
assert subtraksjon(-2,2) == -4
assert divisjon(2,2) == 1
assert divisjon(-2,-4) == 0.5
assert divisjon(-2,1) == -2

# Prosedyre som omgjør fra tommer til cm.
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    cm = antallTommer * 2.54
    print("Resultat: ",cm, "cm")

def skrivBeregninger():
    tall1 = float(input("Tall 1: "))
    tall2 = float(input("Tall 2: "))

    print("\nResultat av summering: ", addisjon(tall1, tall2))
    print("Resultat av subtraksjon: ", subtraksjon(tall1, tall2))
    print("Resultat av divisjon: ", divisjon(tall1, tall2), "\n")

    print("Konvertering fra tommer til cm.")
    tommerTilCm(float(input("Skriv inn et tall: "))) #Kaller omgjøringsfunksjonen


skrivBeregninger()
