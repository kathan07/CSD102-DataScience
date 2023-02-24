
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt


df = pd.read_excel (r'C:\Notes\Bank Aggregated Details.xlsx', sheet_name='Bank_AggregatedData')

#Q1
d1 = df.sort_values("Total amount Withdrawn",ascending = False)
d2 = d1[["ATM Name","Total amount Withdrawn"]]
print(d2)