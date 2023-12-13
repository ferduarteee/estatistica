import numpy as np
import pandas as pd
from scipy.stats import chi2

def q_table_f():
    coluna = [0.005, 0.025, 0.05, 0.25, 0.5, 0.75, 0.9, 0.95, 0.975, 0.99, 0.995]
    linha = list(range(1, 31)) + list(range(40, 101, 10))

    # Initializing an empty matrix
    tabelaQ2 = np.full((len(linha), len(coluna)), np.nan)

    # Filling the matrix with chi-square values
    for i in range(len(linha)):
        for j in range(len(coluna)):
            p = coluna[j]
            dfq = linha[i]
            tabelaQ2[i, j] = round(chi2.ppf(p, dfq), 4)

    # Converting the matrix to a DataFrame
    tabelaQ2_df = pd.DataFrame(tabelaQ2, index=linha, columns=coluna)

    return tabelaQ2_df
