from motorsykkel import Motorsykkel #Importerer klassen Motorsykkel

def hovedprogram():
    sykkel1 = Motorsykkel("Tesla", "BT6520", 13245)
    sykkel2 = Motorsykkel("Harley", "BS3249", 41530)
    sykkel3 = Motorsykkel("Yamaha", "AB9142", 90133)

    print(sykkel1.skrivUt())
    print(sykkel2.skrivUt())
    print(sykkel3.skrivUt())

hovedprogram()
