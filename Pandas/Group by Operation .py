import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance'],
    'Salary': [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].mean()
print(result)
