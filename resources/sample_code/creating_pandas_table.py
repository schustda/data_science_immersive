import pandas as pd

columns = ['page', 'Visitors', 'Registrations', 'Purchases']
data.append(['1', 998832, 331912, 18255 ])
data.append(['2', 1012285, 349643, 18531])
data.append(['3', 995750, 320432, 18585])
df = pd.DataFrame(data = data, columns = columns)
df.set_index(df['page'],inplace = True)
del df['page']
print("Observed data")
print(df)
