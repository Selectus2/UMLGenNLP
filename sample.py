import pandas as pd

list1 = [1,2,3,4,5]
df = pd.DataFrame(list1)

csv_data = df.to_csv(index=False)
df.to_csv('filename.csv', index=False)