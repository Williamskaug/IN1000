#Programmet finnre ut om personene tåler maten.
#Programmet er også dynamisk slik at man kan legge til nye matretter og nye personer med allergier.

#Starter med å opprette to ordbøker, en for hver av personene som har allergier, og hvilke allergier de har.
allergier = {"Anne": "gluten", "Ola": "melk", "Kari": "laktose"}

#Denne ordboken inneholder måltidene, og det dem inneholder som allergikere kan reagere på.
mat = {"brød": {"gluten"}, "grøt": {"melk"}, "pannekaker": {"gluten", "melk"}}

#Bruker en for-løkke for å traversjere gjennom alle matrettene i ordboken.
for x in mat:
    print("----------------------")
    print("Det er", x, "til mat. ")

    #For hver matrett kjører denne for-løkken. Denne for-løkken tester om noen av personene ikke tåler matrett x.
    for i in allergier:
        if allergier[i] in mat[x]:
            print(i,"kan ikke spise", x, ". Personen tåler ikke", allergier[i], ".")
