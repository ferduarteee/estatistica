import plotly.express as px
teta = 0.65
x = 1
x2 = 0

fx1 = (teta ** x) * ((1 - teta) ** (1 - x))
fx2 = (teta ** x2) * ((1 - teta) ** (1 - x2))
fx = [fx1, fx2]

fig = px.scatter(fx, width=800, height=500, range_y=[0, 1], range_x=[-0.5, 1.5], title = 'Função Acumulada de Probabilidade - Bernoulli', labels={'value': 'Probabilidade', 'index':'Eventos','variable': 'Probabilidade'})
fig.update_traces(marker={'color': 'red'})
fig.show()
