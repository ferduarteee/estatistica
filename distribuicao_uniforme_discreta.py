import plotly.express as px
n = 5 #Número de eventos
a = 10 
x = 10
lista=list()
fx=0

for i in range(n):
  fx = fx + ((x + 1) - a) / n 
  lista.append(fx)

fig= px.line(lista, width=800, height=500, title = 'Função de Distribuição Uniforme Discreta',labels={'index': 'Evento', 'value':'Probabilidade', 'variable': 'Probabilidade'}, line_shape='hv')
fig.update_traces(line_color='red')
fig.show()