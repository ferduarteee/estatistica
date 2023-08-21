import math
def hdist(N, n):
    try:
        return ((math.factorial(N))/(math.factorial(n)*math.factorial(N - n)))
    except:
        return 0
    k = 25
    x = 25
    lista = list()
    for i in range(x):
        try:
            fx = (binomial(k, i) * binomial(N-k, n-i)) / binomial(N, n)
        except:
            fx = 0
        lista.append(fx)
    return lista

