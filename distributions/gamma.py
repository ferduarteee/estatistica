import plotly.express as px
from math import gamma, e



def func_gam(n, beta):
    alfa  = n / 2 
    eq = []
    for i in range(n):
        eq.append(((beta ** 2)/gamma(alfa)) * i **(alfa-1) * e ** (- beta * i))
    fig = px.line(eq, width=900, height=500, title = 'Função de Probabilidade Gamma', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape="spline")
    fig.update_traces(line_color='green')
    return fig 

def accum_gam(n, beta):
    alfa  = n / 2
    fx = 0 
    eq = []
    for i in range(n):
        fx = fx + ((beta ** 2)/gamma(alfa)) * i **(alfa-1) * e ** (- beta * i)
        eq.append(fx)
    fig = px.line(eq, width=900, height=500, title = 'Função de Distribuição Gamma', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(line_color='green')
    return fig