import pandas as pd

data = {
    'employee_id': [1,2,3,4,5,6],
    'department': ['IT','IT','HR','HR','IT','HR'],
    'salary': [50000,60000,40000,45000,70000,48000]
}

df = pd.DataFrame(data)

result = df.sort_values(['department','salary'], ascending=[True, False]) \
           .groupby('department') \
           .head(3)

print(result)
