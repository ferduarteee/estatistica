from math import gamma 
import plotly.express as px

def f(n, d1, d2):
    results = []
    for x in range(0,n):
        try:
            numerator = (d1 * x) ** (d1 / 2) * d2 ** (d2 / 2)
            denominator = (d1 * x + d2) ** ((d1 + d2) / 2)
            beta_function = gamma(d1 / 2) * gamma(d2 / 2) / gamma((d1 + d2) / 2)
            r = (numerator / denominator) / (x * beta_function)
        except:
            r = 0
        results.append(r)
        
    fig = px.line(results, width=900, height=500, title = 'Função de Probabilidade F-Snaedecor', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape = "spline")
    fig.update_traces(line_color='green')
    return fig 


def ac_f(n, d1, d2):
    lista = list()
    fx = 0
    for i in range(n):
        try:
            numerator = (d1 * i) ** (d1 / 2) * d2 ** (d2 / 2)
            denominator = (d1 * i + d2) ** ((d1 + d2) / 2)
            beta_function = gamma(d1 / 2) * gamma(d2 / 2) / gamma((d1 + d2) / 2)
            fx = fx + (numerator / denominator) / (i * beta_function)
        except:
            fx = 0
        lista.append(fx)
    fig = px.line(lista, width=900, height=500, title = 'Função de Distribuição F-Snedecor', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(marker={'color': 'green'})
    return fig