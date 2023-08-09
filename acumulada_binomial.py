import math
import plotly.express as px

n = 100
x = 0
teta = 1 / 3 #probabilidade de sucesso
lista = list()
a = 0

for i in range(1, n):
  a = ((math.factorial(n)) / (math.factorial(i) * math.factorial(n - i))) * (teta ** i) * ((1 - teta) ** (n - i)) 
  lista.append(a)
  

fig = px.scatter(lista, width=800, height=500, title = 'Função Acumulada de Probabilidade - Binomial', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable': 'Probabilidade'})
fig.update_traces(marker={'color': 'green'})
fig.show()