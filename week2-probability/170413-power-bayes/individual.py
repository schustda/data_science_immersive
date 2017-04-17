import pandas as pd
import numpy as np
df = pd.read_csv('mtcars.csv')

#  km / liter = 1.61 / 3.79

df['lp100km'] = 1/(df['mpg'] * 1.61/3.79) * 100

bins = [0,df.hp.median(),len(df)]
