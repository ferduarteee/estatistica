import math
import plotly.express as px

def binomial(N, n):
  try:
    return ((math.factorial(N))/(math.factorial(n)*math.factorial(N - n)))
  except:
    return 0

def hdist(N, n, k, i, x):
    lista = list()
    for i in range(x):
        try:
          fx = (binomial(k, i) * binomial(N-k, n-i)) / binomial(N, n)
        except:
          fx = 0
        lista.append(fx)
    fig = px.scatter(lista, width=900, height=500, title = 'Função de Densidade Hipergeométrica', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig 

def accum_hdist(N, n, k, i, x):
    lista = list()
    fx = 0
    for i in range(x):
        fx = fx + (binomial(k, i) * binomial(N-k, n-i)) / binomial(N, n)
        lista.append(fx)
    fig = px.line(lista, width=900, height=500, title = 'Função de Distribuição Hipergeométrica', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(line_color='green')
    return fig