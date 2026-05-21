import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

import pandas as pd
df = pd.read_csv("5000.csv")

print(df.head())

yes_no_cols = ['existingFault', 'suspendedAsset', 'dataLimitExceed',
               'extraGBAdded', 'enteredQueue', 'isAnswered']
df[yes_no_cols] = df[yes_no_cols].fillna('NO')

print(df.head())
print(df.tail())

# enteredQueue vs isAnswered
print(pd.crosstab(df['enteredQueue'], df['isAnswered']))
print(df[
    (df['enteredQueue'] == 'NO') &
    (df['isAnswered'] == 'YES')
])

print(df[
    (df['enteredQueue'] == 'NO') &
    (df['isAnswered'] == 'YES')
].shape[0])
