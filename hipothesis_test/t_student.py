import pandas as pd
from scipy.stats import t as t_student

def t_table_f():
  tabela_t_student = pd.DataFrame(
      [], 
      index=[i for i in range(1, 45)],
      columns = [i / 100 for i in range(10, 0, -1)]
  )

  for index in tabela_t_student.index:
      for column in tabela_t_student.columns:
          tabela_t_student.loc[index, column] = t_student.ppf(1 - float(column) / 2, index)

  index=[('', i) for i in range(1, 45)]
  tabela_t_student.index = pd.MultiIndex.from_tuples(index)

  columns = [("{0:0.3f}".format(i / 100), "{0:0.3f}".format((i / 100) / 2)) for i in range(10, 0, -1)]
  tabela_t_student.columns = pd.MultiIndex.from_tuples(columns)

  tabela_t_student.rename_axis(['Bicaudal', 'Unicaudal'], axis=1, inplace=True)

  return tabela_t_student