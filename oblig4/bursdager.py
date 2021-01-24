# Dette programmet lar brukeren legge til venners navn og bursdag, og lar brukeren se bursdagene som er lagt til.
# 1. Starter med å opprette en ordbok for bursdager, denne skal inneholde navn som nøkkel og datoer som verdi.
# 2. Videre opprettes en prosedyre start(), som lar brukeren velge om en skal legge til en bursdag, vise bursdagene, eller stoppe programmet.
# 3. Videre opprettes prosedyre vis(), som skriver ut bursdagene gjennom en for-løkke. Dette gjør at vi får personens navn og bursdag på samme linje.
# 4. Så har vi en prosedyre leggtil() som lar bruker legge til navn og bursdager.
# 5. Prosedyrene kaller alltid tilbake til prosedyren start(), slik at brukeren alltid vil få valget om å legge til flere bursdager, vise listen, eller stoppe programmet.
# 6. Kjører programmet ved å kalle prosedyren start().

bursdager = {} #Oppretter ordbok

def start():
    print("1. Vis bursdager, 2. Legg til, 0. stopp")
    valg = input("")
    if valg == "1":
        vis()
    elif valg == "2":
        leggtil()
    elif valg == "0":
        print("Stopper program")
    else:
        start() #Kaller tilbake til den opprinnelige prosedyren, dersom brukeren har skrevet inn en ugyldig verdi.

def vis():
    if not bursdager: #Tester om ordboken er tom
        print("Du har ikke lagt til noen bursdager.")
    else:
        print("Bursdager:")
        for i in bursdager:
            print(i,"har bursdag", bursdager[i])
    start() #Kaller tilbake til den opprinnelige prosedyren.

def leggtil():
    navn = input("Navn: ")
    dato = input("Dato: ")
    bursdager[navn] = dato #Legger til navn og bursdag i ordboken.
    start() #Kaller tilbake til den opprinnelige prosedyren.

start()
