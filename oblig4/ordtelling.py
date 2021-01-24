# Oppretter en prosedyren som tar inn en string som argument og returnerer lengden til stringen.
def teller(x):
    print("Ordet", x, "har", len(x), "bokstaver.")

# Kaller prosedyren med ordet "abc"
teller("abc")

# Oppretter en funksjon som ber brukeren skrive inn en setning, deretter deler programmet opp setningen, teller om antall ord, ord skriver ut ord og antall ganger de repeteres.
def ordteller():
    setning = input("Skriv inn en setning: \n")

    # Deler opp setningen til en lste med ord.
    liste = setning.split()

    ord = {}

    # En for-løkke travasjerer listen med ord og tester om ordet allerede finnes eller må leggges til på nytt.
    for x in liste:
        if x not in ord:
            ord[x] = 1
        else:
            ord[x] += 1



    print("\n Det er ", len(liste), "ord i setningen din. \n")
    # Bruker en for-løkke for å printe ut ordene i setningen, linje for linje.
    for x in ord:
        print("Ordet '", x ,"' forekommer", ord[x] , "gang(er), og har", len(x), "bokstaver.")

# Kaller funksjonen
ordteller()
