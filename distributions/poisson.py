import math
import plotly.express as px



def dpoisson(n, p):
    lamb = n*p
    e = math.e
    lista=list()
    for i in range(1, n):
        fx = ((lamb ** i) * e**(-lamb)) / math.factorial(i)
        lista.append(fx)
    fig = px.scatter(lista, width=900, height=500, title = 'Função de Densidade Poisson', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig