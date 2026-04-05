import pandas as pd

data = {
    'Name': ['Aman', 'Ravi', 'Sita'],
    'Marks': [85, 67, 90]
}

df = pd.DataFrame(data)

df['Grade'] = df['Marks'].apply(lambda x: 'A' if x >= 80 else 'B')
print(df)
