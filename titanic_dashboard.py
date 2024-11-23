import os
import pandas as pd
print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir('.'))
pd.read_csv('Titanic-Dataset.csv')

