# 1. Først kalles funksjonen hovedprogram()
# 2. Variabelen a og b defineres, b printes. Deretter defineres b lik a, og a lik returverdien til funksjonen minFunksjon().
# 3. Deretter printes variabelen a og b, men her vil man få en feilmelding, fordi a ikke er definert, fordi det skulle være en global variabel, ikke en lokal.

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)


def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()
