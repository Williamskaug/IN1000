#Oppretter en funksjon som beregner antall celsius fra fahrenheit som argument.
def celsius(fahrenheit):
    celsius = round((fahrenheit-32)*(5/9),1) #Beregner celsius og runder av til ett desimal.
    print(fahrenheit, "fahrenheit er lik ", celsius, "celsius.")

#Kaller funksjonen med brukerens input som argument.
celsius(int(input("Skriv inn antall fahrenheit: ")))
