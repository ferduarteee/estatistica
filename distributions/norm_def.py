import math
import plotly.express as px
import numpy as np
from scipy.stats import norm

def norm_pad(mean, devPad):
    if mean > 0:
        x = np.arange((mean - (2 * mean)), (mean + (2 * mean)), 0.01)
    elif mean < 0:
        x = np.arange((mean + (2 * mean)), (mean - (2 * mean)), 0.01)        
    media = mean      # média
    var   = (devPad ** 2)       # variância
    dp    = np.sqrt(var) # desvio padrão 
    # função de densidade
    dx  = norm.pdf(x, loc=media, scale=np.sqrt(var))
    fig = px.line(x=x,y=dx, width=800, height=500, title = 'Função de Probabilidade Normal Padrão', labels={'y': 'Probabilidade', 'x':'Eventos', 'variable': 'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig 

def norm_pad_accum( mean, devPad):
    if mean > 0:
        x = np.arange((mean - (2 * mean)), (mean + (2 * mean)), 0.01)
    elif mean < 0:
        x = np.arange((mean + (2 * mean)), (mean - (2 * mean)), 0.01)        
    media = mean      # média
    var   = (devPad ** 2)       # variância
    dp    = np.sqrt(var) # desvio padrão 
    # função de densidade
    dx  = norm.pdf(x, loc=media, scale=np.sqrt(var))
    soma = 0
    y=[]
    
    for i in dx:
        soma+=i
        y.append(soma)

    fig = px.line(x=x,y=y, width=900, height=500, title = 'Função de Distribuição Normal Padrão', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(line_color='green')
    return fig
