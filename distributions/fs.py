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
