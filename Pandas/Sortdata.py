import pandas as pd

data = {
    'Name': ['Aman', 'Ravi', 'Sita'],
    'Marks': [85, 67, 90]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by='Marks', ascending=False)
print(df_sorted)
