import csv
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean(file, csv_name):
    print(str(file))
    # Load the data
    df = pd.read_csv(os.path.join(r'../data', file))

    # Drop rows with null values
    df = df.dropna()

    # Drop Columns for PassengerId, Cabin, Name
    df = df.drop(columns=['PassengerId', 'Cabin', 'Name'])

    # Creating labelEncoder
    le = LabelEncoder()

    # Converting string labels into numbers.
    df['HomePlanet'] = le.fit_transform(df['HomePlanet'])
    df['Destination'] = le.fit_transform(df['Destination'])

    df.to_csv(r'../data/'+str(csv_name))