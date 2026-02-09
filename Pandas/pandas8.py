import pandas as pd
import numpy as np

data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)

print(ser[:5])
