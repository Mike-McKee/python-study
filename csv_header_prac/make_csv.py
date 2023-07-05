#using pandas and numpy to create a csv file with incorrect headers
import numpy as np
import pandas as pd

headers = ['Header_1', 'Header_@', 'Header_3', 'haeder_4', 'Head_5']

np.random.seed(42)
data = np.random.randint(low=0, high=100, size=(10,5))

df = pd.DataFrame(data, columns=headers)

df.to_csv('change_headers.csv')
