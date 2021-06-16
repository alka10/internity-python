import numpy as np
import pandas as pd
from matplotlib import pylot as plt
data = pd.read_csv('../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv')
print(df)

data.describe()
data.hist(figsize=(20,18), bins= 50)
data.corr()
plt.figure(figsize=(15,12))

data.isnull().sum()
print(data.shape)
data['quality'].value_counts()

