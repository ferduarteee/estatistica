import plotly.express as px
n = 5 #Número de eventos possíveis 
a = 10 
x = 10

""" Cria-se uma lista que é incrementada n vezes por meio
de um laço de repetição. O valor de incremento é o resultado
da função acumulada ao resultado anterior """

armazena_fx = list()
fx = 0
for i in range(n):
  fx = fx + ((x + 1) - a) / n 
  armazena_fx.append(fx)
fig = px.line(armazena_fx, width=800, height=500, title = 'Função Acumulada de Probabilidade',labels={'index': 'Evento', 'value':'Probabilidade', 'variable': 'Probabilidade'}, line_shape='hv')
fig.update_traces(line_color='red')
fig.show()
