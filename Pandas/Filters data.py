import pandas as pd

data = {
    'Name': ['Aman', 'Ravi', 'Sita', 'John', 'Neha'],
    'Marks': [85, 67, 90, 72, 88]
}

df = pd.DataFrame(data)

result = df[df['Marks'] > 75]
print(result)
