#Here I'm changing a csv file's headers using pandas built in functions
import pandas as pd

df = pd.read_csv('dirty_csv.csv')

df.rename(columns={'Header_@': 'Header_2',
                   'haeder_4': 'Header_4',
                   'Head_5': 'Header_5'}, inplace=True)

df.to_csv('change_with_pandas.csv', index=False)