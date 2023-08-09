import plotly.express as px 

n = 6 
x = 1 / n 
lista = list()
for i in range(n):
  lista.append(x)
fig = px.line(lista, width=800, height=500, title = 'Função Massa de Probablidade', labels={'value': 'Probabilidade', 'index':'Eventos','variable': 'Probabilidade'})
fig.update_traces(line_color='blue')
fig.show()