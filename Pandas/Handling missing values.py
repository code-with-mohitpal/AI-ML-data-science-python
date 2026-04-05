import pandas as pd
import numpy as np

data = {
    'Marks': [85, np.nan, 90, np.nan, 88]
}

df = pd.DataFrame(data)

df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print(df)
