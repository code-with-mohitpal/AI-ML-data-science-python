second_highest = df['salary'].drop_duplicates().nlargest(2).iloc[-1]
print(second_highest)
