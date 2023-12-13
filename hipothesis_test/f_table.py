import pandas as pd
from scipy.stats import f


def f_table_f(p):
    # Definindo os graus de liberdade para as colunas e linhas
    graus_de_liberdade_colunas = [i for i in range(1, 11)] + [20, 30, 40, 50, 60]
    graus_de_liberdade_linhas = [i for i in range(1, 11)] + [20, 30, 40, 50, 60]

    # Criando uma matriz vazia para armazenar os valores da tabela F
    tabela_f_values = []

    # Preenchendo a matriz com os valores da tabela F
    for linha in graus_de_liberdade_linhas:
        row_values = []
        for coluna in graus_de_liberdade_colunas:
            row_values.append(round(f.ppf(p, coluna, linha), 4))
        tabela_f_values.append(row_values)

    # Criando um DataFrame com os valores da tabela F
    columns = [int(df) for df in graus_de_liberdade_colunas]
    index = [int(df) for df in graus_de_liberdade_linhas]
    tabela_f = pd.DataFrame(tabela_f_values, columns=columns, index=index)

    return tabela_f
