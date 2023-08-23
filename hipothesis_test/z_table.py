import scipy.stats as stats
import pandas as pd

index_search_v = []
index_search_h = []
v = 0.0
h = 0.0
for i in range(31):
  index_search_v.append(v)
  v = round(v + 0.1, 2)

for i in range(10):
  index_search_h.append(h)
  h = round(h + 0.01, 2)

def z_table_f():
    z_table = []
    for i in range(0, 31):
        z_row = []
        for j in range(0, 10):
            z_value = i / 10 + j / 100
            cumulative_prob = round(stats.norm.cdf(z_value), 4)
            z_row.append(cumulative_prob)
        z_table.append(z_row)
    df = pd.DataFrame(z_table)
    df.index = index_search_v
    df.columns = index_search_h
    df.columns.name = "Z"
    df.index.name = "Z"
    return df