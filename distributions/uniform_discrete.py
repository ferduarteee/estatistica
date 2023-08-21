import math 
import plotly.express as px


def udisc(n):
    x = 1 / n
    values = list()
    for i in range(n):
        values.append(x)
    fig = px.scatter(values, width=800, height=500, title = 'Função de Densidade Uniforme Discreta', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'})
    fig.update_traces(line_color='blue')
    return fig


def adisc(n):
    a = 10
    x = 10
    lista=list()
    fx=0
    for i in range(n):
        fx = fx + ((x + 1) - a) / n
        lista.append(fx)
    fig = px.line(lista, width=800, height=500, title = 'Função de Distribuição Uniforme Discreta',labels={'index': 'Evento', 'value':'Probabilidade', 'variable': 'Probabilidade'}, line_shape='hv')
    fig.update_traces(line_color='red')
    return fig 