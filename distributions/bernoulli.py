import plotly.express as px

def bern_dist(teta):
    x = 0
    x2 = 1
    fx1 = (teta ** x) * ((1 - teta) ** (1 - x))
    fx2 = (teta ** x2) * ((1 - teta) ** (1 - x2))
    fx = [(fx1), (fx2)]
    fig = px.scatter(fx, width=800, height=500, range_y=[0, 1], range_x=[-0.5, 1.5], title = 'Função de Probabilidade Bernoulli', labels={'value': 'Probabilidade', 'index':'Eventos','variable': 'Probabilidade'})
    fig.update_traces(marker={'color': 'red'})
    return fig
