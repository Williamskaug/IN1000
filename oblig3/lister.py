#1, Tolker oppgaven som at jeg skal skrive ut det tredje elementet, altså elementet med index lik 2.
print("--- Første og tredje element i listen ---")
liste = [1,2,3,3,4,5] #Definerer en liste
liste.append(4) #Legger til et element i listen
print(liste[0], liste[2])


# 2,3
print("")
print("--- Liste med 4 navn ---")
navn = [] #Oppretter en tom liste
navn.append(input("1. Skriv inn et navn: "))  #Her legger jeg til navnene i listen navn.
navn.append(input("2. Skriv inn et navn: "))
navn.append(input("3. Skriv inn et navn: "))
navn.append(input("4. Skriv inn et navn: "))

if "William" in navn: #Tester om mitt navn William er inkludert i listen navn.
    print("Du husket meg!")
else:
    print("Du glemte meg!")

#4
print("")
print("--- Flere lister ---")
produkt = 1 #Definerer variabelen produkt
sum = 0 #Definerer variabelen sum
for x in liste: # Bruker en for-løkke for å traversjere gjennom listen.
    sum = sum + liste[x-1] #Legger til alle verdiene i listen til en sum.
    produkt = produkt * liste[x-1] #Multipliserer alle verdiene til et produkt.
nyliste = [sum, produkt] #Legger til sum og produkt til en ny liste.
print("Sum og produkt av liste: ", nyliste)

nyliste2 = liste + nyliste #Legger sammen to lister
print("To lister lagt sammen", nyliste2)

nyliste2.pop() #Her fjerner jeg det siste elementet i listen.
nyliste2.pop()

print("Ny liste med de to siste variablene fjernet:", nyliste2)
