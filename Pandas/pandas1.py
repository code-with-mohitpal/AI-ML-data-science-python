import pandas as pd

data = {
    "Name": ["Ashutosh", "Rahul", "Neha"],
    "Age": [20, 21, 19],
    "Branch": ["CSE", "ECE", "IT"]
}

df = pd.DataFrame(data)
print(df)




import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 21]
})
print(df)
