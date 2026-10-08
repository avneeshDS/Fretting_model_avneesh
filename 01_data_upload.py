import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("/workspaces/Fretting_model_avneesh/ML_fretting_screening.csv", sep=",", encoding='cp1252')
#print(df.head())
print(df.columns.to_list())
feature_column = ['P','D','µ','µP','µPD','P^(1/3)','Q','D/a']
df_features = df.loc[:, feature_column]
# .loc for selecting data using rows and columns
df_DE = df['DE(N-mm)']
df_ER = df['Energy_ratio']
df_R = df['Regime']
print(df_DE.head())