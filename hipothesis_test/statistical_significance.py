import numpy as np
import streamlit as st 
import plotly.graph_objects as go
import scipy.stats as stats

def stats_sig(nivel_de_significancia):
    graus_de_liberdade = 10
    x = np.linspace(-4, 4, 100)
    pdf = stats.t.pdf(x, graus_de_liberdade)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=pdf, mode='lines', name='Distribuição t de Student'))
    valor_critico = stats.t.ppf(1 - (nivel_de_significancia / 2), graus_de_liberdade)
    x_fill = np.linspace(min(x), -valor_critico, 100)
    y_fill = stats.t.pdf(x_fill, graus_de_liberdade)
    fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]),
                            y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                            fill='toself', fillcolor='red', line=dict(color='red', width=0),
                            name='Zona de Rejeição'))
    x_fill = np.linspace(max(x), valor_critico, 100)
    y_fill = stats.t.pdf(x_fill, graus_de_liberdade)
    fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]),
                            y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                            fill='toself', fillcolor='red', line=dict(color='red', width=0),
                            name='Zona de Rejeição'))
    fig.update_layout(
        title='Distribuição t de Student com Zona de Rejeição',
        xaxis_title='Valores',
        yaxis_title='Probabilidade',
        showlegend=True
    )
    return fig