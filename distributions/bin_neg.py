import math
import plotly.express as px

def binomial(N, n):
  try:
    return ((math.factorial(N))/(math.factorial(n)*math.factorial(N - n)))
  except:
    return 0
  

def bndist(r, x, teta):
    lista = list()
    for i in range(x):
        fx = ((binomial(r + i - 1, i)) * (teta ** r)) * ((1 - teta) ** i)
        lista.append(fx)
    fig = px.scatter(lista, width=900, height=500, title = 'Função de Densidade Binomial Negativa', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig 

def ac_bndist(r, x, teta):
    lista = list()
    fx = 0
    for i in range(x):
        fx = fx + ((binomial(r + i - 1, i)) * (teta ** r)) * ((1 - teta) ** i)
        lista.append(fx)
    fig = px.line(lista, width=900, height=500, title = 'Função de Distribuição Binomial Negativa', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(marker={'color': 'green'})
    return fig 