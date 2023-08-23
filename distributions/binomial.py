import math
import plotly.express as px

def binom(teta, n):
    values = list()
    a = 0

    for i in range(1, n):
        a = ((math.factorial(n)) / (math.factorial(i) * math.factorial(n - i))) * (teta ** i) * ((1 - teta) ** (n - i))
        values.append(a)

    fig = px.scatter(values, width=800, height=500, title = 'Função de Probabilidade Binomial', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable': 'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig


def binom_deg(teta, n):
    values = list()
    a = 0
    for i in range(1, n):
        a = a + ((math.factorial(n)) / (math.factorial(i) * math.factorial(n - i))) * (teta ** i) * ((1 - teta) ** (n - i))
        values.append(a)

    #Gráfico
    fig = px.line(values, width=800, height=500, title = 'Função de Distribuição Binomial', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable': 'Probabilidade'}, line_shape ='hv')
    fig.update_traces(line_color='green')
    return fig