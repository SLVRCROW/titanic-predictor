import pandas as pd
import os

print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir('.'))
pd.read_csv('Titanic-Dataset.csv')

